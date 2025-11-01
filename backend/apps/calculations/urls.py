"""
AWJ Calculations App - URL Configuration
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router pro ViewSets
router = DefaultRouter()
router.register(r'materials', views.MaterialViewSet, basename='material')
router.register(r'abrasives', views.AbrasiveMaterialViewSet, basename='abrasive')
router.register(r'calculations', views.AWJCalculationViewSet, basename='calculation')
router.register(r'optimization-presets', views.OptimizationPresetViewSet, basename='optimization-preset')
router.register(r'statistics', views.CalculationStatisticsView, basename='statistics')

app_name = 'calculations'

urlpatterns = [
    path('', include(router.urls)),
]
