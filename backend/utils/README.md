# Backend Utils

## 📋 Účel
Pomocné Python funkce a utility sdílené napříč backend aplikací

## 📁 Budoucí struktura:
```
utils/
├── validators.py         # Validace dat
├── converters.py        # Konverze jednotek
├── decorators.py        # Custom dekorátory
├── exceptions.py        # Custom výjimky
└── helpers.py           # Obecné pomocné funkce
```

## 📝 Příklad validators.py:
```python
# validators.py
from django.core.exceptions import ValidationError

class AWJValidators:
    """Validátory pro AWJ parametry"""

    @staticmethod
    def validate_pressure(pressure):
        """Validace tlaku"""
        if not (100 <= pressure <= 600):
            raise ValidationError(
                f'Tlak musí být mezi 100-600 MPa, zadáno: {pressure}'
            )

    @staticmethod
    def validate_thickness(thickness):
        """Validace tloušťky materiálu"""
        if not (0.1 <= thickness <= 500):
            raise ValidationError(
                f'Tloušťka musí být mezi 0.1-500 mm, zadáno: {thickness}'
            )

    @staticmethod
    def validate_nozzle_diameter(diameter):
        """Validace průměru trysky"""
        if not (0.2 <= diameter <= 0.5):
            raise ValidationError(
                f'Průměr trysky musí být mezi 0.2-0.5 mm, zadáno: {diameter}'
            )

    @staticmethod
    def validate_abrasive_flow(flow):
        """Validace průtoku abraziva"""
        if not (0 <= flow <= 20):
            raise ValidationError(
                f'Průtok abraziva musí být mezi 0-20 kg/h, zadáno: {flow}'
            )

    @classmethod
    def validate_all_parameters(cls, params):
        """Validace všech parametrů najednou"""
        errors = {}

        try:
            cls.validate_pressure(params.get('pressure'))
        except ValidationError as e:
            errors['pressure'] = str(e)

        try:
            cls.validate_thickness(params.get('thickness'))
        except ValidationError as e:
            errors['thickness'] = str(e)

        try:
            cls.validate_abrasive_flow(params.get('abrasive_flow'))
        except ValidationError as e:
            errors['abrasive_flow'] = str(e)

        if errors:
            raise ValidationError(errors)

        return True
```

## 📝 Příklad converters.py:
```python
# converters.py
class UnitConverter:
    """Konverze jednotek"""

    # Tlak
    @staticmethod
    def mpa_to_psi(mpa):
        """MPa -> PSI"""
        return mpa * 145.038

    @staticmethod
    def psi_to_mpa(psi):
        """PSI -> MPa"""
        return psi / 145.038

    @staticmethod
    def mpa_to_bar(mpa):
        """MPa -> bar"""
        return mpa * 10

    # Délka
    @staticmethod
    def mm_to_inch(mm):
        """mm -> inch"""
        return mm / 25.4

    @staticmethod
    def inch_to_mm(inch):
        """inch -> mm"""
        return inch * 25.4

    # Rychlost
    @staticmethod
    def mm_min_to_m_min(mm_min):
        """mm/min -> m/min"""
        return mm_min / 1000

    @staticmethod
    def mm_min_to_inch_min(mm_min):
        """mm/min -> inch/min"""
        return mm_min / 25.4

    # Průtok
    @staticmethod
    def l_min_to_gpm(l_min):
        """l/min -> GPM (galons per minute)"""
        return l_min * 0.264172

    @staticmethod
    def gpm_to_l_min(gpm):
        """GPM -> l/min"""
        return gpm / 0.264172

    # Hmotnost
    @staticmethod
    def kg_to_lb(kg):
        """kg -> lb (libry)"""
        return kg * 2.20462

    @staticmethod
    def lb_to_kg(lb):
        """lb -> kg"""
        return lb / 2.20462
```

## 📝 Příklad decorators.py:
```python
# decorators.py
import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def timer(func):
    """Dekorátor pro měření času vykonání funkce"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logger.info(
            f"{func.__name__} took {end_time - start_time:.4f} seconds"
        )
        return result
    return wrapper

def cache_result(timeout=300):
    """Dekorátor pro cachování výsledků"""
    def decorator(func):
        cache = {}
        cache_time = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(kwargs)
            current_time = time.time()

            if key in cache and (current_time - cache_time[key]) < timeout:
                logger.debug(f"Returning cached result for {func.__name__}")
                return cache[key]

            result = func(*args, **kwargs)
            cache[key] = result
            cache_time[key] = current_time
            return result

        return wrapper
    return decorator

def validate_parameters(validator_class):
    """Dekorátor pro automatickou validaci parametrů"""
    def decorator(func):
        @wraps(func)
        def wrapper(cls, params, *args, **kwargs):
            validator_class.validate_all_parameters(params)
            return func(cls, params, *args, **kwargs)
        return wrapper
    return decorator
```

## 📝 Příklad exceptions.py:
```python
# exceptions.py
class AWJException(Exception):
    """Základní výjimka pro AWJ aplikaci"""
    pass

class InvalidParameterError(AWJException):
    """Neplatné parametry"""
    pass

class CalculationError(AWJException):
    """Chyba při výpočtu"""
    pass

class OptimizationError(AWJException):
    """Chyba při optimalizaci"""
    pass

class MaterialNotFoundError(AWJException):
    """Materiál nenalezen"""
    pass

class AbrasiveNotFoundError(AWJException):
    """Abrazivo nenalezeno"""
    pass
```

## 📝 Příklad helpers.py:
```python
# helpers.py
from decimal import Decimal, ROUND_HALF_UP

class AWJHelpers:
    """Obecné pomocné funkce"""

    @staticmethod
    def round_decimal(value, decimals=2):
        """Zaokrouhlení na dané desetinná místa"""
        if isinstance(value, (int, float)):
            value = Decimal(str(value))
        return float(value.quantize(
            Decimal(10) ** -decimals,
            rounding=ROUND_HALF_UP
        ))

    @staticmethod
    def clamp(value, min_val, max_val):
        """Omezení hodnoty do rozsahu"""
        return max(min_val, min(value, max_val))

    @staticmethod
    def interpolate(x, x0, x1, y0, y1):
        """Lineární interpolace"""
        if x1 == x0:
            return y0
        return y0 + (x - x0) * (y1 - y0) / (x1 - x0)

    @staticmethod
    def percentage_change(old_value, new_value):
        """Výpočet procentuální změny"""
        if old_value == 0:
            return 0
        return ((new_value - old_value) / old_value) * 100

    @staticmethod
    def format_duration(seconds):
        """Formátování času v sekundách na čitelný formát"""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)

        if hours > 0:
            return f"{hours}h {minutes}m"
        elif minutes > 0:
            return f"{minutes}m {secs}s"
        else:
            return f"{secs}s"
```

## 💡 Použití v aplikaci:
```python
# V services.py
from backend.utils.validators import AWJValidators
from backend.utils.converters import UnitConverter
from backend.utils.decorators import timer, validate_parameters
from backend.utils.helpers import AWJHelpers

class AWJCalculationService:
    @classmethod
    @timer
    @validate_parameters(AWJValidators)
    def perform_calculation(cls, params):
        # Konverze jednotek
        pressure_psi = UnitConverter.mpa_to_psi(params['pressure'])

        # Výpočet
        result = cls.calculate_cutting_speed(params)

        # Zaokrouhlení
        result = AWJHelpers.round_decimal(result, 2)

        return result
```

## ⚠️ Status: 🚧 PŘIPRAVENO - Vyžaduje implementaci
