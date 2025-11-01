# Backend Tests

## 📋 Účel
Unit a integrační testy pro Django backend

## 🧪 Struktura testů:
```
backend/
├── test_calculations.py      # Testy výpočtů
├── test_models.py            # Testy databázových modelů
├── test_api.py               # Testy API endpoints
├── test_services.py          # Testy business logiky
└── test_optimization.py      # Testy optimalizace
```

## 📝 Příklad: test_calculations.py

```python
# test_calculations.py
import pytest
from backend.apps.calculations.services import AWJCalculationService

class TestWaterFlowCalculation:
    """Testy výpočtu průtoku vody"""

    def test_basic_water_flow(self):
        """Test základního výpočtu průtoku"""
        flow = AWJCalculationService.calculate_water_flow(
            nozzle_diameter=0.33,
            pressure=380
        )
        assert flow > 0, "Průtok musí být kladný"
        assert flow < 10, "Průtok je nerealisticky vysoký"

    def test_water_flow_with_different_pressures(self):
        """Test průtoku při různých tlacích"""
        flow_low = AWJCalculationService.calculate_water_flow(0.33, 200)
        flow_high = AWJCalculationService.calculate_water_flow(0.33, 400)

        assert flow_high > flow_low, "Vyšší tlak by měl dát vyšší průtok"

    def test_water_flow_with_different_nozzles(self):
        """Test průtoku s různými průměry trysek"""
        flow_small = AWJCalculationService.calculate_water_flow(0.25, 380)
        flow_large = AWJCalculationService.calculate_water_flow(0.40, 380)

        assert flow_large > flow_small, "Větší tryska by měla dát větší průtok"

    @pytest.mark.parametrize("nozzle,pressure,expected_min,expected_max", [
        (0.33, 380, 3.0, 4.0),
        (0.25, 380, 2.0, 3.0),
        (0.40, 380, 4.0, 5.5),
    ])
    def test_water_flow_ranges(self, nozzle, pressure, expected_min, expected_max):
        """Test, že průtok je v očekávaném rozsahu"""
        flow = AWJCalculationService.calculate_water_flow(nozzle, pressure)
        assert expected_min <= flow <= expected_max


class TestCuttingSpeedCalculation:
    """Testy výpočtu řezné rychlosti"""

    def test_basic_cutting_speed_steel(self):
        """Test základního výpočtu pro ocel"""
        speed = AWJCalculationService.calculate_cutting_speed(
            material_type='steel',
            thickness=10,
            pressure=380,
            abrasive_flow=8,
            nozzle_diameter=0.33,
            focus_diameter=1.0
        )
        assert 100 < speed < 200, f"Rychlost {speed} je mimo očekávaný rozsah"

    def test_cutting_speed_aluminum_faster_than_steel(self):
        """Test, že hliník se řeže rychleji než ocel"""
        params = {
            'thickness': 10,
            'pressure': 380,
            'abrasive_flow': 8,
            'nozzle_diameter': 0.33,
            'focus_diameter': 1.0
        }

        speed_steel = AWJCalculationService.calculate_cutting_speed(
            material_type='steel', **params
        )
        speed_aluminum = AWJCalculationService.calculate_cutting_speed(
            material_type='aluminum', **params
        )

        assert speed_aluminum > speed_steel, \
            "Hliník by se měl řezat rychleji než ocel"

    def test_thicker_material_slower_cutting(self):
        """Test, že tlustší materiál se řeže pomaleji"""
        params = {
            'material_type': 'steel',
            'pressure': 380,
            'abrasive_flow': 8,
            'nozzle_diameter': 0.33,
            'focus_diameter': 1.0
        }

        speed_thin = AWJCalculationService.calculate_cutting_speed(
            thickness=5, **params
        )
        speed_thick = AWJCalculationService.calculate_cutting_speed(
            thickness=20, **params
        )

        assert speed_thin > speed_thick, \
            "Tenčí materiál by se měl řezat rychleji"

    def test_higher_pressure_faster_cutting(self):
        """Test, že vyšší tlak zvyšuje rychlost řezání"""
        params = {
            'material_type': 'steel',
            'thickness': 10,
            'abrasive_flow': 8,
            'nozzle_diameter': 0.33,
            'focus_diameter': 1.0
        }

        speed_low = AWJCalculationService.calculate_cutting_speed(
            pressure=200, **params
        )
        speed_high = AWJCalculationService.calculate_cutting_speed(
            pressure=400, **params
        )

        assert speed_high > speed_low, \
            "Vyšší tlak by měl zvýšit rychlost řezání"


class TestFullCalculation:
    """Testy kompletního výpočtu"""

    def test_full_calculation_returns_all_results(self):
        """Test, že kompletní výpočet vrací všechny výsledky"""
        results = AWJCalculationService.perform_full_calculation({
            'material_type': 'steel',
            'thickness': 10.0,
            'pressure': 380.0,
            'nozzle_diameter': 0.33,
            'focus_diameter': 1.0,
            'abrasive_flow': 8.0,
            'mesh_size': 80,
            'standoff_distance': 3.0
        })

        # Zkontrolovat, že všechny klíče jsou přítomny
        required_keys = [
            'water_flow',
            'hydraulic_power',
            'cutting_speed',
            'cut_depth',
            'surface_roughness',
            'cost_per_meter'
        ]

        for key in required_keys:
            assert key in results, f"Chybí klíč '{key}' ve výsledcích"
            assert results[key] > 0, f"Hodnota '{key}' musí být kladná"


class TestCostCalculation:
    """Testy výpočtu nákladů"""

    def test_cost_increases_with_abrasive_flow(self):
        """Test, že náklady rostou s průtokem abraziva"""
        params = {
            'material_type': 'steel',
            'thickness': 10,
            'pressure': 380,
            'nozzle_diameter': 0.33,
            'focus_diameter': 1.0,
            'mesh_size': 80,
            'standoff_distance': 3.0
        }

        results_low = AWJCalculationService.perform_full_calculation({
            **params, 'abrasive_flow': 5
        })
        results_high = AWJCalculationService.perform_full_calculation({
            **params, 'abrasive_flow': 12
        })

        assert results_high['cost_per_meter'] > results_low['cost_per_meter'], \
            "Vyšší průtok abraziva by měl zvýšit náklady"
```

## 📝 Příklad: test_api.py

```python
# test_api.py
import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class TestCalculationsAPI(TestCase):
    """Testy API pro výpočty"""

    def setUp(self):
        self.client = APIClient()
        self.valid_payload = {
            'material_type': 'steel',
            'thickness': 10.0,
            'pressure': 380.0,
            'nozzle_diameter': 0.33,
            'focus_diameter': 1.0,
            'abrasive_flow': 8.0,
            'mesh_size': 80,
            'standoff_distance': 3.0
        }

    def test_quick_calculate_success(self):
        """Test úspěšného výpočtu"""
        response = self.client.post(
            '/api/calculations/quick_calculate/',
            self.valid_payload,
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK
        assert 'results' in response.data
        assert 'cutting_speed' in response.data['results']

    def test_quick_calculate_invalid_pressure(self):
        """Test s neplatným tlakem"""
        invalid_payload = {**self.valid_payload, 'pressure': 1000}

        response = self.client.post(
            '/api/calculations/quick_calculate/',
            invalid_payload,
            format='json'
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_history(self):
        """Test získání historie výpočtů"""
        # Nejprve vytvořit výpočet
        self.client.post('/api/calculations/', self.valid_payload, format='json')

        # Pak získat historii
        response = self.client.get('/api/calculations/history/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) > 0

    def test_optimize_for_speed(self):
        """Test optimalizace pro rychlost"""
        payload = {
            'material_type': 'steel',
            'thickness': 10.0,
            'target': 'max_speed'
        }

        response = self.client.post(
            '/api/calculations/optimize/',
            payload,
            format='json'
        )

        assert response.status_code == status.HTTP_200_OK
        assert 'optimized_params' in response.data
```

## 🚀 Spuštění testů:

### Všechny testy:
```bash
pytest tests/backend/
```

### Konkrétní test soubor:
```bash
pytest tests/backend/test_calculations.py
```

### Konkrétní test třída:
```bash
pytest tests/backend/test_calculations.py::TestWaterFlowCalculation
```

### Konkrétní test metoda:
```bash
pytest tests/backend/test_calculations.py::TestWaterFlowCalculation::test_basic_water_flow
```

### S verbose výstupem:
```bash
pytest tests/backend/ -v
```

### S pokrytím kódu:
```bash
pytest tests/backend/ --cov=backend.apps.calculations --cov-report=html
```

## 📊 Coverage Report:
Po spuštění s `--cov-report=html` otevřete `htmlcov/index.html` pro vizuální report pokrytí kódu.

## 💡 Doporučení:
1. Pište testy PŘED implementací (TDD)
2. Každá funkce by měla mít alespoň jeden test
3. Testujte edge cases (hraniční hodnoty)
4. Používejte fixtures pro opakující se data
5. Cílte na 80%+ code coverage

## ⚠️ Status: 🚧 PŘIPRAVENO - Testy čekají na implementaci
Backend je funkční ✅, testy připraveny k psaní 🚧
