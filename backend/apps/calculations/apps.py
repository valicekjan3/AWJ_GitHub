"""
AWJ Calculations App Configuration
"""

from django.apps import AppConfig


class CalculationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.calculations'
    verbose_name = 'AWJ Výpočty'

    def ready(self):
        """Inicializace při startu aplikace"""
        # Import signálů pokud budou potřeba
        pass
