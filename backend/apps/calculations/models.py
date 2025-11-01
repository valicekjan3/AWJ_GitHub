"""
AWJ Calculations App - Database Models
Databázové modely pro ukládání výpočtů a parametrů
"""

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import json


class Material(models.Model):
    """Model materiálu pro AWJ řezání"""

    MATERIAL_TYPES = [
        ('steel', 'Ocel (Steel)'),
        ('aluminum', 'Hliník (Aluminum)'),
        ('titanium', 'Titan (Titanium)'),
        ('granite', 'Žula (Granite)'),
        ('glass', 'Sklo (Glass)'),
        ('ceramic', 'Keramika (Ceramic)'),
        ('composite', 'Kompozit (Composite)'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=MATERIAL_TYPES)
    density = models.FloatField(help_text="Hustota [kg/m³]")
    tensile_strength = models.FloatField(help_text="Pevnost v tahu [MPa]")
    hardness = models.FloatField(help_text="Tvrdost [HV]", null=True, blank=True)

    # Koeficienty pro výpočty
    k_factor = models.FloatField(default=1.0, help_text="Korekční faktor pro výpočet rychlosti")
    surface_factor = models.FloatField(default=1.0, help_text="Faktor drsnosti povrchu")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Materiál"
        verbose_name_plural = "Materiály"

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class AbrasiveMaterial(models.Model):
    """Model abrazivního materiálu"""

    ABRASIVE_TYPES = [
        ('garnet', 'Granát (Garnet)'),
        ('aluminum_oxide', 'Oxid hlinitý (Aluminum Oxide)'),
        ('silicon_carbide', 'Karbid křemíku (Silicon Carbide)'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=ABRASIVE_TYPES)
    mesh_size = models.IntegerField(help_text="Velikost zrna [mesh]")
    particle_size = models.FloatField(help_text="Velikost částice [μm]")
    hardness = models.FloatField(help_text="Tvrdost [Mohs]")
    density = models.FloatField(help_text="Hustota [kg/m³]")

    # Nákladové parametry
    cost_per_kg = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cena za kg [Kč]")

    class Meta:
        ordering = ['mesh_size']
        verbose_name = "Abrazivo"
        verbose_name_plural = "Abraziva"

    def __str__(self):
        return f"{self.name} ({self.mesh_size} mesh)"


class AWJCalculation(models.Model):
    """Hlavní model pro uložení výpočtu AWJ parametrů"""

    # Reference
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    abrasive = models.ForeignKey(AbrasiveMaterial, on_delete=models.SET_NULL, null=True)

    # Vstupní parametry - Materiál
    thickness = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(500)],
        help_text="Tloušťka materiálu [mm]"
    )

    # Vstupní parametry - Řezání
    pressure = models.FloatField(
        validators=[MinValueValidator(100), MaxValueValidator(600)],
        help_text="Tlak vody [MPa]"
    )
    nozzle_diameter = models.FloatField(
        validators=[MinValueValidator(0.1), MaxValueValidator(2.0)],
        help_text="Průměr trysky [mm]",
        default=0.33
    )
    focus_diameter = models.FloatField(
        validators=[MinValueValidator(0.5), MaxValueValidator(2.0)],
        help_text="Průměr fokusační trubice [mm]",
        default=1.0
    )
    focus_length = models.FloatField(
        validators=[MinValueValidator(50), MaxValueValidator(150)],
        help_text="Délka fokusační trubice [mm]",
        default=76
    )

    # Vstupní parametry - Abrazivo
    abrasive_flow = models.FloatField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
        help_text="Hmotnostní tok abraziva [g/s]",
        default=8
    )

    # Vypočtené výsledky (uložené pro historii)
    cutting_speed = models.FloatField(null=True, blank=True, help_text="Řezná rychlost [mm/min]")
    hydraulic_power = models.FloatField(null=True, blank=True, help_text="Hydraulický výkon [kW]")
    water_flow = models.FloatField(null=True, blank=True, help_text="Průtok vody [l/min]")
    cut_depth = models.FloatField(null=True, blank=True, help_text="Hloubka řezu [mm]")
    surface_roughness = models.FloatField(null=True, blank=True, help_text="Drsnost Ra [μm]")
    cost_per_meter = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        help_text="Náklady na řez [Kč/m]"
    )

    # JSON pole pro rozšířené výsledky
    extended_results = models.JSONField(
        null=True, blank=True,
        help_text="Rozšířené výsledky a mezihodnoty"
    )

    # Metadata
    calculation_time = models.FloatField(null=True, blank=True, help_text="Čas výpočtu [ms]")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Poznámky
    notes = models.TextField(blank=True, help_text="Poznámky k výpočtu")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "AWJ Výpočet"
        verbose_name_plural = "AWJ Výpočty"
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['user', '-created_at']),
        ]

    def __str__(self):
        return f"Výpočet #{self.id} - {self.material} {self.thickness}mm"

    def get_input_parameters(self):
        """Vrátí všechny vstupní parametry jako dictionary"""
        return {
            'material_type': self.material.type if self.material else None,
            'thickness': self.thickness,
            'pressure': self.pressure,
            'nozzle_diameter': self.nozzle_diameter,
            'focus_diameter': self.focus_diameter,
            'focus_length': self.focus_length,
            'abrasive_flow': self.abrasive_flow,
            'abrasive_mesh': self.abrasive.mesh_size if self.abrasive else None,
        }

    def get_results(self):
        """Vrátí všechny výsledky jako dictionary"""
        results = {
            'cutting_speed': self.cutting_speed,
            'hydraulic_power': self.hydraulic_power,
            'water_flow': self.water_flow,
            'cut_depth': self.cut_depth,
            'surface_roughness': self.surface_roughness,
            'cost_per_meter': float(self.cost_per_meter) if self.cost_per_meter else None,
        }

        # Přidat extended results pokud existují
        if self.extended_results:
            results['extended'] = self.extended_results

        return results


class CalculationHistory(models.Model):
    """Historie změn výpočtů pro tracking optimalizací"""

    calculation = models.ForeignKey(AWJCalculation, on_delete=models.CASCADE, related_name='history')
    timestamp = models.DateTimeField(auto_now_add=True)

    # Co se změnilo
    changed_parameters = models.JSONField(help_text="Změněné parametry")
    old_results = models.JSONField(help_text="Staré výsledky")
    new_results = models.JSONField(help_text="Nové výsledky")

    # Kdo změnil
    changed_by = models.CharField(max_length=50, default='user', help_text="user/ai/system")

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Historie výpočtu"
        verbose_name_plural = "Historie výpočtů"

    def __str__(self):
        return f"Historie #{self.id} - Výpočet #{self.calculation.id}"


class OptimizationPreset(models.Model):
    """Přednastavené optimalizace pro různé scénáře"""

    OPTIMIZATION_TARGETS = [
        ('max_speed', 'Maximální rychlost'),
        ('min_cost', 'Minimální náklady'),
        ('best_quality', 'Nejlepší kvalita'),
        ('balanced', 'Vyvážené'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    target = models.CharField(max_length=50, choices=OPTIMIZATION_TARGETS)

    # Doporučené parametry
    recommended_params = models.JSONField(help_text="Doporučené parametry")

    # Pro jaký typ materiálu
    suitable_for_materials = models.JSONField(
        default=list,
        help_text="Seznam typů materiálů vhodných pro tento preset"
    )

    # Metadata
    success_rate = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Úspěšnost presetu [%]"
    )
    usage_count = models.IntegerField(default=0, help_text="Počet použití")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-success_rate', 'name']
        verbose_name = "Optimalizační preset"
        verbose_name_plural = "Optimalizační presety"

    def __str__(self):
        return f"{self.name} ({self.get_target_display()})"
