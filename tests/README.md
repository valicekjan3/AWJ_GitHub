# Tests Folder

## 📋 Účel
Testy pro backend a frontend

## 🧪 Struktur a:
```
tests/
├── backend/      # Python testy (pytest, Django tests)
└── frontend/     # JavaScript testy (Jest)
```

## 🔧 Backend testy (pytest):

### Příklad: `tests/backend/test_calculations.py`
```python
import pytest
from backend.apps.calculations.services import AWJCalculationService

def test_water_flow_calculation():
    flow = AWJCalculationService.calculate_water_flow(
        nozzle_diameter=0.33,
        pressure=380
    )
    assert flow > 0
    assert flow < 10  # Realistická hodnota

def test_cutting_speed():
    speed = AWJCalculationService.calculate_cutting_speed(
        material_type='steel',
        thickness=10,
        pressure=380,
        abrasive_flow=8,
        nozzle_diameter=0.33,
        focus_diameter=1.0
    )
    assert speed > 0
```

## 🚀 Spuštění testů:
```bash
# Backend
pytest tests/backend/

# Frontend
npm test
```

## 💡 Doporučení:
Začněte s testy hlavních výpočetních funkcí!
