# API Documentation

## 📋 Účel
Detailní dokumentace REST API endpointů

## ⚠️ AKTUÁLNÍ STAV
API je plně funkční! ✅ Tato složka je připravena pro formální API dokumentaci.

## 🔗 Funkční API Endpoints

### 1. Calculations - Výpočty

#### POST `/api/calculations/quick_calculate/`
**Účel:** Rychlý výpočet bez uložení do databáze

**Request:**
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

**Response:**
```json
{
  "success": true,
  "results": {
    "water_flow": 3.45,
    "hydraulic_power": 21.78,
    "cutting_speed": 150.2,
    "cut_depth": 10.0,
    "surface_roughness": 3.2,
    "cost_per_meter": 245.50,
    "extended_results": {
      "kerf_width": 1.05,
      "jet_velocity": 650.0,
      "reynolds_number": 45000
    }
  }
}
```

#### POST `/api/calculations/`
**Účel:** Výpočet s uložením do databáze

**Request:** Stejný jako quick_calculate

**Response:**
```json
{
  "id": 123,
  "material_type": "steel",
  "thickness": 10.0,
  "cutting_speed": 150.2,
  "created_at": "2024-11-01T12:00:00Z",
  "results": { ... }
}
```

#### GET `/api/calculations/history/`
**Účel:** Historie výpočtů

**Query params:**
- `limit` - Počet výsledků (default: 10)
- `offset` - Offset pro paginaci

**Response:**
```json
{
  "count": 100,
  "next": "/api/calculations/history/?offset=10",
  "previous": null,
  "results": [
    {
      "id": 123,
      "material_type": "steel",
      "thickness": 10.0,
      "cutting_speed": 150.2,
      "created_at": "2024-11-01T12:00:00Z"
    }
  ]
}
```

#### POST `/api/calculations/batch_calculate/`
**Účel:** Porovnání více variant najednou

**Request:**
```json
{
  "calculations": [
    {
      "material_type": "steel",
      "thickness": 10.0,
      "pressure": 380.0,
      ...
    },
    {
      "material_type": "aluminum",
      "thickness": 10.0,
      "pressure": 380.0,
      ...
    }
  ]
}
```

**Response:**
```json
{
  "results": [
    { "cutting_speed": 150.2, "cost_per_meter": 245.50 },
    { "cutting_speed": 195.3, "cost_per_meter": 220.30 }
  ]
}
```

#### POST `/api/calculations/optimize/`
**Účel:** AI optimalizace parametrů

**Request:**
```json
{
  "material_type": "steel",
  "thickness": 10.0,
  "target": "max_speed",  // nebo "min_cost"
  "constraints": {
    "max_pressure": 400.0,
    "max_abrasive_flow": 10.0
  }
}
```

**Response:**
```json
{
  "optimized_params": {
    "pressure": 400.0,
    "abrasive_flow": 10.0,
    "nozzle_diameter": 0.35,
    "focus_diameter": 1.1
  },
  "expected_results": {
    "cutting_speed": 180.5,
    "cost_per_meter": 260.00
  },
  "improvement": {
    "speed_increase": "20%",
    "cost_change": "+6%"
  }
}
```

### 2. Materials - Materiály

#### GET `/api/materials/`
**Účel:** Seznam všech materiálů

**Response:**
```json
[
  {
    "id": 1,
    "name": "Ocel (Steel)",
    "material_type": "steel",
    "tensile_strength": 400.0,
    "k_factor": 1.0,
    "density": 7850.0
  },
  {
    "id": 2,
    "name": "Hliník (Aluminum)",
    "material_type": "aluminum",
    "tensile_strength": 200.0,
    "k_factor": 1.3,
    "density": 2700.0
  }
]
```

#### GET `/api/materials/{id}/`
**Účel:** Detail konkrétního materiálu

### 3. Abrasives - Abraziva

#### GET `/api/abrasives/`
**Účel:** Seznam abraziv

**Response:**
```json
[
  {
    "id": 1,
    "name": "Garnet 80 mesh",
    "mesh_size": 80,
    "cost_per_kg": 15.0,
    "density": 4000.0,
    "hardness": 7.5
  }
]
```

## 📝 Error Handling

### Standard Error Response:
```json
{
  "success": false,
  "error": "Invalid parameter",
  "details": {
    "pressure": ["Tlak musí být mezi 100-600 MPa"],
    "thickness": ["Tloušťka musí být mezi 0.1-500 mm"]
  }
}
```

### HTTP Status Codes:
- `200 OK` - Úspěšný požadavek
- `201 Created` - Vytvořen nový záznam
- `400 Bad Request` - Neplatná data
- `404 Not Found` - Záznam nenalezen
- `500 Internal Server Error` - Chyba serveru

## 🔐 Authentication (Budoucí)
```http
Authorization: Bearer <token>
```

## 📊 Rate Limiting (Budoucí)
- 100 požadavků / minutu pro neautentizované uživatele
- 1000 požadavků / minutu pro autentizované uživatele

## 💡 Příklady použití

### cURL:
```bash
curl -X POST http://localhost:8000/api/calculations/quick_calculate/ \
  -H "Content-Type: application/json" \
  -d '{
    "material_type": "steel",
    "thickness": 10.0,
    "pressure": 380.0,
    "nozzle_diameter": 0.33,
    "focus_diameter": 1.0,
    "abrasive_flow": 8.0,
    "mesh_size": 80,
    "standoff_distance": 3.0
  }'
```

### JavaScript (fetch):
```javascript
const response = await fetch('/api/calculations/quick_calculate/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
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
});

const data = await response.json();
console.log(data.results);
```

### Python (requests):
```python
import requests

response = requests.post(
    'http://localhost:8000/api/calculations/quick_calculate/',
    json={
        'material_type': 'steel',
        'thickness': 10.0,
        'pressure': 380.0,
        'nozzle_diameter': 0.33,
        'focus_diameter': 1.0,
        'abrasive_flow': 8.0,
        'mesh_size': 80,
        'standoff_distance': 3.0
    }
)

results = response.json()['results']
print(f"Řezná rychlost: {results['cutting_speed']} mm/min")
```

## 📖 Budoucí dokumentace:
Pro produkční použití vytvořte:
1. **OpenAPI/Swagger** dokumentaci
2. **Postman Collection**
3. **Interactive API Explorer**

## ⚠️ Status: ✅ API FUNKČNÍ | 🚧 Formální dokumentace připravena
