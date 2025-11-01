# 🧪 Návod: Jak testovat funkčnost Frontend + Backend

## 📋 Přehled testování

Tento návod vás provede **krok za krokem**, jak otestovat, že:
1. ✅ Backend funguje (Django, API, databáze)
2. ✅ Frontend funguje (HTML, CSS, JavaScript)
3. ✅ Frontend komunikuje s backendem
4. ✅ Výpočty jsou správné

---

## Krok 1️⃣: Příprava prostředí

### A) Otevřete Command Prompt
1. Stiskněte **Win + R**
2. Napište `cmd` a stiskněte Enter

### B) Přejděte do projektu
```bash
cd C:\Users\KEAI\awj-calculator-pro
```

### C) Vytvořte virtuální prostředí (pokud ještě nemáte)
```bash
python -m venv venv
```
✅ Mělo by vytvořit složku `venv/`

### D) Aktivujte virtuální prostředí
```bash
venv\Scripts\activate
```
✅ Před příkazovým řádkem by se mělo objevit `(venv)`

### E) Nainstalujte závislosti
```bash
pip install -r requirements.txt
```
✅ Mělo by nainstalovat Django, DRF a další balíčky

---

## Krok 2️⃣: Test Backend - Databáze

### A) Vytvořte databázi
```bash
python manage.py migrate
```
✅ **Co by se mělo stát:**
```
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying calculations.0001_initial... OK
  ...
```

### B) Zkontrolujte, že databáze existuje
```bash
dir db.sqlite3
```
✅ Mělo by vypsat soubor `db.sqlite3`

### C) Vytvořte testovací data (volitelné)
```bash
python manage.py shell
```

V shellu zadejte:
```python
from backend.apps.calculations.models import Material

# Vytvoření materiálu
steel = Material.objects.create(
    name="Ocel Test",
    material_type="steel",
    tensile_strength=400.0,
    k_factor=1.0,
    density=7850.0
)

print(f"Vytvořen materiál: {steel.name}")

# Zobrazení všech materiálů
print(f"Celkem materiálů: {Material.objects.count()}")

# Ukončení
exit()
```

✅ **Mělo by vypsat:** `Vytvořen materiál: Ocel Test`

---

## Krok 3️⃣: Test Backend - Webserver

### A) Spusťte Django server
```bash
python manage.py runserver
```

✅ **Mělo by vypsat:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

⚠️ **NECHTE SERVER BĚŽET!** Otevřete nové okno Command Prompt pro další testy.

### B) Test 1: Hlavní stránka
1. Otevřete prohlížeč (Chrome, Firefox, Edge)
2. Jděte na: **http://localhost:8000**

✅ **CO BYSTE MĚLI VIDĚT:**
- Modrou a oranžovou barevnou schému
- Nadpis "AWJ Calculator Pro"
- Formulář s parametry (Materiál, Tloušťka, Tlak, atd.)
- Tlačítko "Vypočítat"

❌ **Pokud vidíte chybu:**
- Zkontrolujte, že server běží (v cmd)
- Zkontrolujte URL (musí být `localhost:8000`, ne `127.0.0.1:8000`)

### C) Test 2: Admin rozhraní
1. Vytvořte superuživatele (v novém cmd okně):
```bash
cd C:\Users\KEAI\awj-calculator-pro
venv\Scripts\activate
python manage.py createsuperuser
```
Zadejte:
- **Username:** `admin`
- **Email:** můžete nechat prázdný (jen Enter)
- **Password:** např. `admin123` (zadáte dvakrát)

2. Jděte na: **http://localhost:8000/admin**
3. Přihlaste se (username: `admin`, heslo: `admin123`)

✅ **CO BYSTE MĚLI VIDĚT:**
- Django Admin rozhraní
- Sekce "CALCULATIONS" s tabulkami:
  - Abrasive Materials
  - AWJ Calculations
  - Calculation History
  - Materials
  - Optimization Presets

---

## Krok 4️⃣: Test Backend - API Endpoints

### A) Test API pomocí prohlížeče

**Test 1: Seznam materiálů**
- URL: **http://localhost:8000/api/materials/**

✅ **Mělo by vypsat JSON:**
```json
[
  {
    "id": 1,
    "name": "Ocel Test",
    "material_type": "steel",
    "tensile_strength": 400.0,
    ...
  }
]
```

**Test 2: API root**
- URL: **http://localhost:8000/api/**

✅ **Mělo by vypsat dostupné endpointy:**
```json
{
  "calculations": "http://localhost:8000/api/calculations/",
  "materials": "http://localhost:8000/api/materials/",
  "abrasives": "http://localhost:8000/api/abrasives/"
}
```

### B) Test API pomocí Postman (pokročilé)

Pokud máte **Postman** nebo **Insomnia**:

**POST Request: Quick Calculate**
- URL: `http://localhost:8000/api/calculations/quick_calculate/`
- Method: `POST`
- Body (JSON):
```json
{
  "material_type": "steel",
  "thickness": 10.0,
  "pressure": 380.0,
  "nozzle_diameter": 0.33,
  "focus_diameter": 1.0,
  "abrasive_flow": 8.0,
  "mesh_size": 80,
  "standoff_distance": 3.0
}
```

✅ **Response by měla obsahovat:**
```json
{
  "success": true,
  "results": {
    "water_flow": 3.45,
    "hydraulic_power": 21.78,
    "cutting_speed": 150.2,
    "cost_per_meter": 245.50,
    ...
  }
}
```

### C) Test API pomocí Python (v cmd)

```bash
python manage.py shell
```

```python
import requests
import json

# Test quick_calculate endpoint
url = 'http://localhost:8000/api/calculations/quick_calculate/'
data = {
    'material_type': 'steel',
    'thickness': 10.0,
    'pressure': 380.0,
    'nozzle_diameter': 0.33,
    'focus_diameter': 1.0,
    'abrasive_flow': 8.0,
    'mesh_size': 80,
    'standoff_distance': 3.0
}

response = requests.post(url, json=data)
print(f"Status: {response.status_code}")
print(json.dumps(response.json(), indent=2))

exit()
```

✅ **Mělo by vypsat JSON s výsledky**

---

## Krok 5️⃣: Test Frontend - Základní funkce

### A) Test formuláře
1. Jděte na: **http://localhost:8000**
2. V prohlížeči otevřete **Developer Tools** (F12)
3. Přejděte na záložku **Console**

### B) Test 1: Vyplnění formuláře
1. V formuláři vyplňte:
   - **Materiál:** Ocel (Steel)
   - **Tloušťka:** 10 mm
   - **Tlak:** 380 MPa
   - **Průměr trysky:** 0.33 mm
   - **Průměr fokusační trysky:** 1.0 mm
   - **Průtok abraziva:** 8 kg/h
   - **Mesh abraziva:** 80
   - **Vzdálenost trysky:** 3 mm

2. Klikněte **Vypočítat**

✅ **CO BY SE MĚLO STÁT:**
- Pod formulářem by se měly objevit **Result Cards**
- Měly by obsahovat:
  - 💧 Průtok vody: ~3.45 l/min
  - ⚡ Hydraulický výkon: ~21.78 kW
  - 🔪 Řezná rychlost: ~150 mm/min
  - 📏 Hloubka řezu: 10 mm
  - 🎨 Drsnost povrchu: ~3.2 μm
  - 💰 Náklady: ~245 Kč/m

### C) Test 2: Konzole prohlížeče
V **Console** (F12) by NEMĚLY být červené chyby.

✅ **OK:**
```
AWJ Calculator initialized
Calculation completed successfully
```

❌ **CHYBA (pokud vidíte):**
```
Uncaught ReferenceError: calculateAWJ is not defined
```
→ JavaScript se nenačetl správně

### D) Test 3: Network požadavky
1. V Developer Tools (F12) přejděte na záložku **Network**
2. Klikněte **Vypočítat** znovu
3. Měli byste vidět požadavek:
   - **Name:** `quick_calculate/`
   - **Status:** `200` (zelená)
   - **Type:** `xhr` nebo `fetch`

✅ Klikněte na požadavek a zkontrolujte:
- **Headers** → Request Method: `POST`
- **Payload** → Parametry, které jste zadali
- **Response** → JSON s výsledky

---

## Krok 6️⃣: Test Frontend + Backend komunikace

### A) Test offline režimu (PWA)
1. V prohlížeči (F12) → **Network** záložka
2. Nahoře přepněte na **Offline** (místo "No throttling")
3. Klikněte **Vypočítat** znovu

✅ **Mělo by stále fungovat!** (JavaScript počítá lokálně)

### B) Test online režimu
1. Přepněte zpět na **Online**
2. Klikněte **Vypočítat**
3. V Network záložce zkontrolujte, že se volá backend API

✅ **Měli byste vidět:** Request na `quick_calculate/`

### C) Test ukládání do databáze
1. V `static/js/main.js` najděte funkci `calculateAWJ()`
2. Dočasně změňte, aby volala `/api/calculations/` místo `quick_calculate/`

**Nebo** v Console (F12) spusťte:
```javascript
fetch('/api/calculations/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    material_type: 'steel',
    thickness: 10.0,
    pressure: 380.0,
    nozzle_diameter: 0.33,
    focus_diameter: 1.0,
    abrasive_flow: 8.0,
    mesh_size: 80,
    standoff_distance: 3.0
  })
})
.then(r => r.json())
.then(data => console.log(data));
```

3. Jděte na: **http://localhost:8000/admin**
4. Klikněte **AWJ Calculations**

✅ **Měli byste vidět nový záznam** s vašimi parametry

---

## Krok 7️⃣: Test výpočtů - Správnost

### A) Manuální ověření vzorců

**Test průtoku vody:**
- Parametry: tryska 0.33 mm, tlak 380 MPa
- Vzorec: Q = C_d × A × √(2P/ρ)
- Očekávaný výsledek: ~3.4-3.5 l/min

**Python test:**
```python
python manage.py shell
```
```python
from backend.apps.calculations.services import AWJCalculationService

flow = AWJCalculationService.calculate_water_flow(0.33, 380)
print(f"Průtok: {flow} l/min")
# Mělo by být: ~3.45

exit()
```

### B) Porovnání frontend vs backend

**Test v prohlížeči (F12 Console):**
```javascript
// Frontend výpočet
const flow = AWJCalculations.calculateWaterFlow(0.33, 380);
console.log('Frontend průtok:', flow);
```

**Test v Python:**
```python
from backend.apps.calculations.services import AWJCalculationService
flow = AWJCalculationService.calculate_water_flow(0.33, 380)
print(f'Backend průtok: {flow}')
```

✅ **Hodnoty by měly být IDENTICKÉ!**

---

## Krok 8️⃣: Checklist - Co všechno funguje

Zatrhněte, co už jste otestovali:

### Backend:
- [ ] ✅ Databáze se vytvoří (`manage.py migrate`)
- [ ] ✅ Server se spustí (`manage.py runserver`)
- [ ] ✅ Admin rozhraní funguje (`/admin`)
- [ ] ✅ API vrací data (`/api/materials/`)
- [ ] ✅ Quick calculate funguje (`/api/calculations/quick_calculate/`)

### Frontend:
- [ ] ✅ Hlavní stránka se načte (`http://localhost:8000`)
- [ ] ✅ Formulář se zobrazí správně
- [ ] ✅ CSS styly fungují (modrá/oranžová barva)
- [ ] ✅ JavaScript se načte (žádné chyby v Console)

### Frontend + Backend:
- [ ] ✅ Kliknutí na "Vypočítat" zobrazí výsledky
- [ ] ✅ Výsledky jsou realistické (rychlost 100-200 mm/min pro ocel 10mm)
- [ ] ✅ Network request volá backend API
- [ ] ✅ Offline režim funguje (PWA)

### Výpočty:
- [ ] ✅ Průtok vody: ~3.45 l/min (tryska 0.33, tlak 380)
- [ ] ✅ Řezná rychlost: ~150 mm/min (ocel 10mm, 380 MPa)
- [ ] ✅ Frontend a backend dávají stejné výsledky

---

## ❓ Řešení problémů

### ❌ Server nejde spustit
**Chyba:** `Port 8000 is already in use`
```bash
# Najděte proces na portu 8000 a ukončete ho
netstat -ano | findstr :8000
taskkill /PID XXXX /F
```

### ❌ Importy nefungují
**Chyba:** `ModuleNotFoundError: No module named 'rest_framework'`
```bash
# Ujistěte se, že je venv aktivované
venv\Scripts\activate
pip install -r requirements.txt
```

### ❌ Frontend výsledky se nezobrazují
1. Otevřete F12 → Console
2. Zkontrolujte chyby
3. Ověřte, že `main.js` a `calculations.js` se načetly (F12 → Sources)

### ❌ API vrací 404
Zkontrolujte URL:
- ✅ SPRÁVNĚ: `http://localhost:8000/api/materials/`
- ❌ ŠPATNĚ: `http://localhost:8000/materials/`

### ❌ CORS errors
Pokud voláte API z jiné domény:
1. Nainstalujte: `pip install django-cors-headers`
2. Přidejte do `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # Jen pro development!
```

---

## 🎉 Hotovo!

Pokud prošly všechny testy, váš projekt **PLNĚ FUNGUJE!** ✅

### Další kroky:
1. ✅ Nahrajte na GitHub (viz `GITHUB_UPLOAD_GUIDE.md`)
2. ✅ Nasaďte na PythonAnywhere (viz `docs/PYTHONANYWHERE_DEPLOYMENT.md`)
3. ✅ Přidejte pokročilé funkce (Chart.js grafy, 3D vizualizace)

---

**Gratulujeme k funkční aplikaci!** 🎊
