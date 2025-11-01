# Modules Documentation

## 📋 Účel
Detailní dokumentace pro každý modul aplikace

## 📁 Doporučená struktura:
```
modules/
├── calculations_module.md      # Dokumentace calculations app
├── analysis_module.md          # Dokumentace analysis app
├── ai_optimization_module.md   # Dokumentace AI app
├── chatbot_module.md           # Dokumentace chatbot app
└── frontend_modules.md         # Dokumentace frontend modulů
```

## 📝 Vzor: calculations_module.md

### Calculations Module - Dokumentace

#### Přehled
Modul pro výpočty AWJ parametrů. Obsahuje fyzikální modely, empirické vzorce a optimalizační algoritmy.

#### Umístění
- Backend: `backend/apps/calculations/`
- Frontend: `static/js/modules/calculator/calculations.js`

#### Moduly a třídy

##### 1. AWJCalculationService
**Umístění:** `backend/apps/calculations/services.py`

**Metody:**

```python
@classmethod
def calculate_water_flow(cls, nozzle_diameter: float, pressure: float) -> float:
    """
    Výpočet průtoku vody

    Args:
        nozzle_diameter (float): Průměr trysky [mm]
        pressure (float): Tlak [MPa]

    Returns:
        float: Průtok [l/min]

    Vzorec:
        Q = C_d × A × √(2P/ρ)
        kde:
        - C_d = 0.65 (výtokový koeficient)
        - A = π(d/2)² (plocha trysky)
        - P = tlak v Pa
        - ρ = 1000 kg/m³ (hustota vody)

    Příklad:
        >>> AWJCalculationService.calculate_water_flow(0.33, 380)
        3.45
    """
```

```python
@classmethod
def calculate_cutting_speed(
    cls,
    material_type: str,
    thickness: float,
    pressure: float,
    abrasive_flow: float,
    nozzle_diameter: float,
    focus_diameter: float
) -> float:
    """
    Výpočet řezné rychlosti

    Args:
        material_type (str): Typ materiálu ('steel', 'aluminum', ...)
        thickness (float): Tloušťka [mm]
        pressure (float): Tlak [MPa]
        abrasive_flow (float): Průtok abraziva [kg/h]
        nozzle_diameter (float): Průměr trysky [mm]
        focus_diameter (float): Průměr fokusační trysky [mm]

    Returns:
        float: Řezná rychlost [mm/min]

    Empirický model:
        V = k × (P^a × m_a^b) / (t^c × σ^d)
        kde:
        - k = koeficient materiálu
        - P = tlak
        - m_a = průtok abraziva
        - t = tloušťka
        - σ = pevnost materiálu
        - a,b,c,d = empirické exponenty

    Materiálové koeficienty:
        - Ocel: k=1.0, σ=400 MPa
        - Hliník: k=1.3, σ=200 MPa
        - Titan: k=0.7, σ=900 MPa
    """
```

##### 2. AWJOptimizationService
**Umístění:** `backend/apps/calculations/services.py`

**Metody:**

```python
@classmethod
def optimize_for_speed(cls, base_params: dict) -> dict:
    """
    Optimalizace parametrů pro maximální rychlost řezání

    Args:
        base_params (dict): Základní parametry (materiál, tloušťka)

    Returns:
        dict: Optimalizované parametry

    Algoritmus:
        1. Grid search přes možné kombinace parametrů
        2. Výpočet řezné rychlosti pro každou kombinaci
        3. Výběr kombinace s nejvyšší rychlostí

    Omezení:
        - Tlak: 100-600 MPa
        - Průtok abraziva: 0-20 kg/h
        - Průměr trysky: 0.2-0.5 mm
    """
```

#### Datové modely

##### Material Model
```python
class Material(models.Model):
    name = models.CharField(max_length=100)
    material_type = models.CharField(max_length=50, choices=MATERIAL_TYPES)
    tensile_strength = models.FloatField()  # [MPa]
    k_factor = models.FloatField()          # Koeficient řezání
    density = models.FloatField()           # [kg/m³]
```

##### AWJCalculation Model
```python
class AWJCalculation(models.Model):
    # Vstupní parametry
    material_type = models.CharField(max_length=50)
    thickness = models.FloatField()         # [mm]
    pressure = models.FloatField()          # [MPa]
    nozzle_diameter = models.FloatField()   # [mm]
    focus_diameter = models.FloatField()    # [mm]
    abrasive_flow = models.FloatField()     # [kg/h]

    # Vypočtené výsledky
    water_flow = models.FloatField()        # [l/min]
    cutting_speed = models.FloatField()     # [mm/min]
    surface_roughness = models.FloatField() # [μm]
    cost_per_meter = models.FloatField()    # [Kč/m]

    created_at = models.DateTimeField(auto_now_add=True)
```

#### Frontend JavaScript

**Umístění:** `static/js/modules/calculator/calculations.js`

Obsahuje identické výpočty jako backend pro offline funkcionalitu.

```javascript
class AWJCalculations {
    static calculateWaterFlow(nozzleDiameter, pressure) {
        // Implementace stejná jako Python verze
    }

    static calculateCuttingSpeed(...params) {
        // Implementace stejná jako Python verze
    }
}
```

#### API Endpoints

- `POST /api/calculations/quick_calculate/` - Rychlý výpočet
- `POST /api/calculations/` - Výpočet s uložením
- `GET /api/calculations/history/` - Historie
- `POST /api/calculations/optimize/` - Optimalizace

#### Testování

**Unit testy:**
```python
def test_water_flow_calculation():
    flow = AWJCalculationService.calculate_water_flow(0.33, 380)
    assert flow > 0
    assert flow < 10

def test_cutting_speed_steel():
    speed = AWJCalculationService.calculate_cutting_speed(
        'steel', 10, 380, 8, 0.33, 1.0
    )
    assert 100 < speed < 200
```

#### Příklady použití

**Python:**
```python
from backend.apps.calculations.services import AWJCalculationService

results = AWJCalculationService.perform_full_calculation({
    'material_type': 'steel',
    'thickness': 10.0,
    'pressure': 380.0,
    # ...
})

print(f"Řezná rychlost: {results['cutting_speed']} mm/min")
```

**JavaScript:**
```javascript
const results = AWJCalculations.performFullCalculation({
    materialType: 'steel',
    thickness: 10.0,
    pressure: 380.0,
    // ...
});

console.log(`Řezná rychlost: ${results.cuttingSpeed} mm/min`);
```

#### Reference

**Fyzikální vzorce:**
- Bernoulliho rovnice pro proudění tekutin
- Empirické modely AWJ řezání (Hashish, 1989)

**Literatura:**
- Hashish, M. (1989). "Pressure effects in abrasive-waterjet machining"
- Momber, A. W., & Kovacevic, R. (1998). "Principles of Abrasive Water Jet Machining"

---

## 💡 Doporučení pro budoucí dokumentaci:

### Pro každý modul vytvořte:
1. **Přehled** - Účel a funkcionalita
2. **Architektura** - Struktura souborů a tříd
3. **API Reference** - Dokumentace všech tříd a metod
4. **Datové modely** - Popis databázových modelů
5. **Příklady použití** - Konkrétní use cases
6. **Testování** - Jak testovat modul
7. **Reference** - Odkazy na literaturu a zdroje

### Doporučené nástroje:
- **Sphinx** - Pro Python dokumentaci
- **JSDoc** - Pro JavaScript dokumentaci
- **MkDocs** - Pro Markdown dokumentaci
- **Swagger/OpenAPI** - Pro API dokumentaci

## ⚠️ Status: 🚧 PŘIPRAVENO - Čeká na formální dokumentaci
Backend moduly jsou plně funkční ✅
