"""
AWJ Calculations App - Django Admin
Administrace pro AWJ výpočty
"""

from django.contrib import admin
from .models import Material, AbrasiveMaterial, AWJCalculation, CalculationHistory, OptimizationPreset


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'density', 'tensile_strength', 'created_at']
    list_filter = ['type']
    search_fields = ['name']
    ordering = ['name']


@admin.register(AbrasiveMaterial)
class AbrasiveMaterialAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'mesh_size', 'particle_size', 'cost_per_kg']
    list_filter = ['type']
    ordering = ['mesh_size']


@admin.register(AWJCalculation)
class AWJCalculationAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'material', 'thickness', 'pressure',
        'cutting_speed', 'cost_per_meter', 'created_at'
    ]
    list_filter = ['material', 'created_at']
    search_fields = ['notes']
    readonly_fields = [
        'cutting_speed', 'hydraulic_power', 'water_flow',
        'cut_depth', 'surface_roughness', 'cost_per_meter',
        'calculation_time', 'created_at', 'updated_at'
    ]
    fieldsets = (
        ('Základní informace', {
            'fields': ('user', 'material', 'abrasive', 'notes')
        }),
        ('Vstupní parametry - Materiál', {
            'fields': ('thickness',)
        }),
        ('Vstupní parametry - Řezání', {
            'fields': (
                'pressure', 'nozzle_diameter',
                'focus_diameter', 'focus_length'
            )
        }),
        ('Vstupní parametry - Abrazivo', {
            'fields': ('abrasive_flow',)
        }),
        ('Vypočtené výsledky', {
            'fields': (
                'cutting_speed', 'hydraulic_power', 'water_flow',
                'cut_depth', 'surface_roughness', 'cost_per_meter',
                'extended_results'
            )
        }),
        ('Metadata', {
            'fields': ('calculation_time', 'created_at', 'updated_at')
        }),
    )


@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'calculation', 'timestamp', 'changed_by']
    list_filter = ['changed_by', 'timestamp']
    ordering = ['-timestamp']


@admin.register(OptimizationPreset)
class OptimizationPresetAdmin(admin.ModelAdmin):
    list_display = ['name', 'target', 'success_rate', 'usage_count', 'created_at']
    list_filter = ['target']
    search_fields = ['name', 'description']
    ordering = ['-success_rate']
