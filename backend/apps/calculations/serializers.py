"""
AWJ Calculations App - DRF Serializers
REST API serializery pro calculations modely
"""

from rest_framework import serializers
from .models import Material, AbrasiveMaterial, AWJCalculation, CalculationHistory, OptimizationPreset


class MaterialSerializer(serializers.ModelSerializer):
    """Serializer pro Material model"""

    class Meta:
        model = Material
        fields = [
            'id', 'name', 'type', 'density', 'tensile_strength',
            'hardness', 'k_factor', 'surface_factor',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AbrasiveMaterialSerializer(serializers.ModelSerializer):
    """Serializer pro AbrasiveMaterial model"""

    class Meta:
        model = AbrasiveMaterial
        fields = [
            'id', 'name', 'type', 'mesh_size', 'particle_size',
            'hardness', 'density', 'cost_per_kg'
        ]
        read_only_fields = ['id']


class AWJCalculationSerializer(serializers.ModelSerializer):
    """Hlavní serializer pro AWJ výpočty"""

    # Nested serializers pro materiály (read-only)
    material_details = MaterialSerializer(source='material', read_only=True)
    abrasive_details = AbrasiveMaterialSerializer(source='abrasive', read_only=True)

    # Computed fields
    input_parameters = serializers.SerializerMethodField()
    results = serializers.SerializerMethodField()

    class Meta:
        model = AWJCalculation
        fields = [
            'id', 'user',
            # Input parameters
            'material', 'material_details',
            'abrasive', 'abrasive_details',
            'thickness', 'pressure',
            'nozzle_diameter', 'focus_diameter', 'focus_length',
            'abrasive_flow',
            # Results
            'cutting_speed', 'hydraulic_power', 'water_flow',
            'cut_depth', 'surface_roughness', 'cost_per_meter',
            'extended_results',
            # Computed
            'input_parameters', 'results',
            # Metadata
            'calculation_time', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'user', 'cutting_speed', 'hydraulic_power',
            'water_flow', 'cut_depth', 'surface_roughness',
            'cost_per_meter', 'extended_results', 'calculation_time',
            'created_at', 'updated_at'
        ]

    def get_input_parameters(self, obj):
        """Vrátí vstupní parametry"""
        return obj.get_input_parameters()

    def get_results(self, obj):
        """Vrátí výsledky"""
        return obj.get_results()


class AWJCalculationCreateSerializer(serializers.ModelSerializer):
    """Serializer pro vytvoření nového výpočtu"""

    class Meta:
        model = AWJCalculation
        fields = [
            'material', 'abrasive', 'thickness', 'pressure',
            'nozzle_diameter', 'focus_diameter', 'focus_length',
            'abrasive_flow', 'notes'
        ]

    def validate_thickness(self, value):
        """Validace tloušťky"""
        if value <= 0:
            raise serializers.ValidationError("Tloušťka musí být větší než 0")
        if value > 500:
            raise serializers.ValidationError("Maximální tloušťka je 500 mm")
        return value

    def validate_pressure(self, value):
        """Validace tlaku"""
        if value < 100:
            raise serializers.ValidationError("Minimální tlak je 100 MPa")
        if value > 600:
            raise serializers.ValidationError("Maximální tlak je 600 MPa")
        return value

    def validate_abrasive_flow(self, value):
        """Validace toku abraziva"""
        if value < 1:
            raise serializers.ValidationError("Minimální tok je 1 g/s")
        if value > 20:
            raise serializers.ValidationError("Maximální tok je 20 g/s")
        return value


class CalculationHistorySerializer(serializers.ModelSerializer):
    """Serializer pro historii výpočtů"""

    class Meta:
        model = CalculationHistory
        fields = [
            'id', 'calculation', 'timestamp',
            'changed_parameters', 'old_results', 'new_results',
            'changed_by'
        ]
        read_only_fields = ['id', 'timestamp']


class OptimizationPresetSerializer(serializers.ModelSerializer):
    """Serializer pro optimalizační presety"""

    class Meta:
        model = OptimizationPreset
        fields = [
            'id', 'name', 'description', 'target',
            'recommended_params', 'suitable_for_materials',
            'success_rate', 'usage_count',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'usage_count', 'created_at', 'updated_at']


class QuickCalculationSerializer(serializers.Serializer):
    """
    Serializer pro rychlý výpočet bez uložení do databáze
    Použití pro real-time výpočty v UI
    """

    # Input
    material_type = serializers.ChoiceField(choices=[
        'steel', 'aluminum', 'titanium', 'granite',
        'glass', 'ceramic', 'composite'
    ])
    thickness = serializers.FloatField(min_value=0.1, max_value=500)
    pressure = serializers.FloatField(min_value=100, max_value=600)
    nozzle_diameter = serializers.FloatField(min_value=0.1, max_value=2.0, default=0.33)
    focus_diameter = serializers.FloatField(min_value=0.5, max_value=2.0, default=1.0)
    focus_length = serializers.FloatField(min_value=50, max_value=150, default=76)
    abrasive_flow = serializers.FloatField(min_value=1, max_value=20, default=8)
    mesh_size = serializers.IntegerField(default=80)

    # Optional parameters
    material_strength = serializers.FloatField(required=False, allow_null=True)
    save_to_history = serializers.BooleanField(default=False)

    def validate(self, data):
        """Cross-field validation"""

        # Kontrola poměru trysky a fokusační trubice
        if data['nozzle_diameter'] >= data['focus_diameter']:
            raise serializers.ValidationError({
                'focus_diameter': 'Průměr fokusační trubice musí být větší než průměr trysky'
            })

        # Kontrola rozumnosti parametrů pro daný materiál
        if data['material_type'] in ['glass', 'ceramic']:
            if data['pressure'] > 400:
                raise serializers.ValidationError({
                    'pressure': 'Pro křehké materiály se doporučuje tlak max 400 MPa'
                })

        return data


class BatchCalculationSerializer(serializers.Serializer):
    """
    Serializer pro batch výpočty (více variant najednou)
    Použití pro optimalizaci a porovnání parametrů
    """

    base_parameters = QuickCalculationSerializer()
    variations = serializers.ListField(
        child=serializers.DictField(),
        max_length=50,
        help_text="Seznam variací parametrů pro porovnání"
    )

    def validate_variations(self, value):
        """Validace variací"""
        if len(value) == 0:
            raise serializers.ValidationError("Musí být alespoň jedna variace")

        # Kontrola validnosti každé variace
        for i, variation in enumerate(value):
            if not isinstance(variation, dict):
                raise serializers.ValidationError(
                    f"Variace {i} musí být dictionary"
                )

        return value
