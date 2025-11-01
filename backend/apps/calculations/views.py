"""
AWJ Calculations App - API Views
Django REST Framework ViewSets pro AWJ výpočty
"""

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from django.utils import timezone
import time

from .models import (
    Material, AbrasiveMaterial, AWJCalculation,
    CalculationHistory, OptimizationPreset
)
from .serializers import (
    MaterialSerializer, AbrasiveMaterialSerializer,
    AWJCalculationSerializer, AWJCalculationCreateSerializer,
    CalculationHistorySerializer, OptimizationPresetSerializer,
    QuickCalculationSerializer, BatchCalculationSerializer
)
from .services import AWJCalculationService, AWJOptimizationService


class MaterialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint pro materiály
    GET /api/materials/ - seznam materiálů
    GET /api/materials/{id}/ - detail materiálu
    """

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def types(self, request):
        """Vrátí seznam typů materiálů"""
        types = Material.MATERIAL_TYPES
        return Response({
            'types': [{'value': t[0], 'label': t[1]} for t in types]
        })


class AbrasiveMaterialViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint pro abrazivní materiály
    GET /api/abrasives/ - seznam abraziv
    GET /api/abrasives/{id}/ - detail abraziva
    """

    queryset = AbrasiveMaterial.objects.all()
    serializer_class = AbrasiveMaterialSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def mesh_sizes(self, request):
        """Vrátí dostupné velikosti zrn"""
        mesh_sizes = [
            {'value': 50, 'label': '50 mesh (297 μm)'},
            {'value': 80, 'label': '80 mesh (177 μm)'},
            {'value': 120, 'label': '120 mesh (125 μm)'},
        ]
        return Response({'mesh_sizes': mesh_sizes})


class AWJCalculationViewSet(viewsets.ModelViewSet):
    """
    Hlavní API endpoint pro AWJ výpočty

    GET /api/calculations/ - seznam výpočtů
    POST /api/calculations/ - vytvoření nového výpočtu
    GET /api/calculations/{id}/ - detail výpočtu
    PUT /api/calculations/{id}/ - aktualizace výpočtu
    DELETE /api/calculations/{id}/ - smazání výpočtu
    """

    queryset = AWJCalculation.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        """Vrátí správný serializer podle akce"""
        if self.action == 'create':
            return AWJCalculationCreateSerializer
        return AWJCalculationSerializer

    def get_queryset(self):
        """Filtrování podle uživatele"""
        queryset = AWJCalculation.objects.all()

        # Pokud je uživatel přihlášený, zobraz jen jeho výpočty
        if self.request.user.is_authenticated:
            queryset = queryset.filter(user=self.request.user)

        # Filtrování podle materiálu
        material = self.request.query_params.get('material', None)
        if material:
            queryset = queryset.filter(material__type=material)

        return queryset.order_by('-created_at')

    def perform_create(self, serializer):
        """Při vytváření výpočtu provede výpočet a uloží výsledky"""

        start_time = time.time()

        # Získání instance (ještě neuložená)
        instance = serializer.save(
            user=self.request.user if self.request.user.is_authenticated else None
        )

        # Provedení výpočtu
        params = {
            'material_type': instance.material.type if instance.material else 'steel',
            'thickness': instance.thickness,
            'pressure': instance.pressure,
            'nozzle_diameter': instance.nozzle_diameter,
            'focus_diameter': instance.focus_diameter,
            'focus_length': instance.focus_length,
            'abrasive_flow': instance.abrasive_flow,
            'mesh_size': instance.abrasive.mesh_size if instance.abrasive else 80,
        }

        results = AWJCalculationService.perform_full_calculation(params)

        # Uložení výsledků
        instance.water_flow = results['water_flow']
        instance.hydraulic_power = results['hydraulic_power']
        instance.cutting_speed = results['cutting_speed']
        instance.cut_depth = results['cut_depth']
        instance.surface_roughness = results['surface_roughness']
        instance.cost_per_meter = results['cost_per_meter']
        instance.extended_results = results.get('extended', {})

        # Čas výpočtu
        calc_time = (time.time() - start_time) * 1000  # ms
        instance.calculation_time = round(calc_time, 2)

        instance.save()

    @action(detail=False, methods=['post'])
    def quick_calculate(self, request):
        """
        Rychlý výpočet bez uložení do databáze
        POST /api/calculations/quick_calculate/

        Použití pro real-time výpočty v UI
        """

        serializer = QuickCalculationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        start_time = time.time()

        # Provedení výpočtu
        results = AWJCalculationService.perform_full_calculation(
            serializer.validated_data
        )

        calc_time = (time.time() - start_time) * 1000

        # Pokud chce uživatel uložit
        if serializer.validated_data.get('save_to_history', False):
            # TODO: Implementovat uložení do historie
            pass

        return Response({
            'success': True,
            'results': results,
            'calculation_time_ms': round(calc_time, 2),
            'input_parameters': serializer.validated_data
        })

    @action(detail=False, methods=['post'])
    def batch_calculate(self, request):
        """
        Batch výpočet pro porovnání variant
        POST /api/calculations/batch_calculate/
        """

        serializer = BatchCalculationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        base_params = serializer.validated_data['base_parameters']
        variations = serializer.validated_data['variations']

        results_list = []

        # Základní výpočet
        base_results = AWJCalculationService.perform_full_calculation(base_params)
        results_list.append({
            'variant': 'base',
            'parameters': base_params,
            'results': base_results
        })

        # Výpočty variací
        for i, variation in enumerate(variations):
            # Merge base params s variation
            variant_params = {**base_params, **variation}

            variant_results = AWJCalculationService.perform_full_calculation(variant_params)

            results_list.append({
                'variant': f'variation_{i+1}',
                'parameters': variant_params,
                'results': variant_results
            })

        return Response({
            'success': True,
            'total_variants': len(results_list),
            'results': results_list
        })

    @action(detail=False, methods=['post'])
    def optimize(self, request):
        """
        AI Optimalizace parametrů
        POST /api/calculations/optimize/

        Body:
        {
            "material_type": "steel",
            "thickness": 10,
            "target": "max_speed" | "min_cost"
        }
        """

        material_type = request.data.get('material_type', 'steel')
        thickness = float(request.data.get('thickness', 10))
        target = request.data.get('target', 'max_speed')

        if target == 'max_speed':
            optimized = AWJOptimizationService.optimize_for_speed(
                material_type=material_type,
                thickness=thickness
            )
        elif target == 'min_cost':
            min_speed = float(request.data.get('min_speed', 50))
            optimized = AWJOptimizationService.optimize_for_cost(
                material_type=material_type,
                thickness=thickness,
                min_speed=min_speed
            )
        else:
            return Response(
                {'error': 'Invalid target. Use "max_speed" or "min_cost"'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response({
            'success': True,
            'target': target,
            'material_type': material_type,
            'thickness': thickness,
            'optimized_parameters': optimized
        })

    @action(detail=True, methods=['get'])
    def history(self, request, pk=None):
        """
        Historie změn výpočtu
        GET /api/calculations/{id}/history/
        """

        calculation = self.get_object()
        history = calculation.history.all()
        serializer = CalculationHistorySerializer(history, many=True)

        return Response({
            'calculation_id': calculation.id,
            'history': serializer.data
        })


class OptimizationPresetViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint pro optimalizační presety
    GET /api/optimization-presets/ - seznam presetů
    GET /api/optimization-presets/{id}/ - detail presetu
    """

    queryset = OptimizationPreset.objects.all()
    serializer_class = OptimizationPresetSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def for_material(self, request):
        """
        Vrátí presety vhodné pro daný materiál
        GET /api/optimization-presets/for_material/?material=steel
        """

        material_type = request.query_params.get('material', None)
        if not material_type:
            return Response(
                {'error': 'Parameter "material" is required'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filtruj presety které obsahují tento materiál
        presets = self.queryset.filter(
            suitable_for_materials__contains=[material_type]
        )

        serializer = self.get_serializer(presets, many=True)

        return Response({
            'material_type': material_type,
            'presets': serializer.data
        })


class CalculationStatisticsView(viewsets.ViewSet):
    """
    API endpoint pro statistiky výpočtů
    """

    permission_classes = [AllowAny]

    @action(detail=False, methods=['get'])
    def summary(self, request):
        """
        Celkové statistiky
        GET /api/statistics/summary/
        """

        total_calculations = AWJCalculation.objects.count()
        total_materials = Material.objects.count()

        # Nejpoužívanější materiál
        from django.db.models import Count
        top_material = AWJCalculation.objects.values(
            'material__name'
        ).annotate(
            count=Count('id')
        ).order_by('-count').first()

        # Průměrné hodnoty
        from django.db.models import Avg
        averages = AWJCalculation.objects.aggregate(
            avg_speed=Avg('cutting_speed'),
            avg_power=Avg('hydraulic_power'),
            avg_cost=Avg('cost_per_meter')
        )

        return Response({
            'total_calculations': total_calculations,
            'total_materials': total_materials,
            'most_used_material': top_material,
            'averages': {
                'cutting_speed': round(averages['avg_speed'] or 0, 2),
                'hydraulic_power': round(averages['avg_power'] or 0, 2),
                'cost_per_meter': round(float(averages['avg_cost'] or 0), 2)
            }
        })
