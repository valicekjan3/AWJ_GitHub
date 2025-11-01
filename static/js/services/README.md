# JavaScript Services - API komunikace

## 📋 Účel
Centralizovaná správa API volání z frontendu na backend

## 📁 Budoucí struktura:
```
services/
├── apiClient.js              # Základní fetch wrapper
├── calculationService.js     # API pro výpočty
├── materialService.js        # API pro materiály
├── optimizationService.js    # API pro optimalizaci
└── storageService.js         # LocalStorage management
```

## 📝 Příklad apiClient.js:
```javascript
// apiClient.js
class APIClient {
  constructor(baseURL = '/api') {
    this.baseURL = baseURL;
  }

  async get(endpoint) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return await response.json();
    } catch (error) {
      console.error('API GET Error:', error);
      throw error;
    }
  }

  async post(endpoint, data) {
    try {
      const response = await fetch(`${this.baseURL}${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': this.getCSRFToken()
        },
        body: JSON.stringify(data)
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return await response.json();
    } catch (error) {
      console.error('API POST Error:', error);
      throw error;
    }
  }

  getCSRFToken() {
    const name = 'csrftoken';
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) return value;
    }
    return '';
  }
}

export const apiClient = new APIClient();
```

## 📝 Příklad calculationService.js:
```javascript
// calculationService.js
import { apiClient } from './apiClient.js';

export class CalculationService {
  /**
   * Rychlý výpočet bez ukládání do databáze
   */
  static async quickCalculate(params) {
    return await apiClient.post('/calculations/quick_calculate/', params);
  }

  /**
   * Výpočet s uložením do databáze
   */
  static async saveCalculation(params) {
    return await apiClient.post('/calculations/', params);
  }

  /**
   * Získání historie výpočtů
   */
  static async getHistory(limit = 10) {
    return await apiClient.get(`/calculations/history/?limit=${limit}`);
  }

  /**
   * Porovnání více variant
   */
  static async batchCalculate(paramsList) {
    return await apiClient.post('/calculations/batch_calculate/', {
      calculations: paramsList
    });
  }

  /**
   * Optimalizace parametrů
   */
  static async optimize(params, target) {
    return await apiClient.post('/calculations/optimize/', {
      ...params,
      target  // 'max_speed' nebo 'min_cost'
    });
  }
}
```

## 📝 Příklad materialService.js:
```javascript
// materialService.js
import { apiClient } from './apiClient.js';

export class MaterialService {
  /**
   * Získání seznamu materiálů
   */
  static async getMaterials() {
    return await apiClient.get('/materials/');
  }

  /**
   * Detail materiálu
   */
  static async getMaterial(id) {
    return await apiClient.get(`/materials/${id}/`);
  }

  /**
   * Získání seznamu abraziv
   */
  static async getAbrasives() {
    return await apiClient.get('/abrasives/');
  }
}
```

## 📝 Příklad storageService.js:
```javascript
// storageService.js
export class StorageService {
  /**
   * Uložení výpočtu do Local Storage
   */
  static saveCalculation(calculation) {
    const saved = this.getSavedCalculations();
    saved.push({
      ...calculation,
      timestamp: new Date().toISOString()
    });

    // Limit na 50 uložených výpočtů
    if (saved.length > 50) {
      saved.shift();
    }

    localStorage.setItem('awj_calculations', JSON.stringify(saved));
  }

  /**
   * Získání uložených výpočtů
   */
  static getSavedCalculations() {
    const data = localStorage.getItem('awj_calculations');
    return data ? JSON.parse(data) : [];
  }

  /**
   * Smazání historie
   */
  static clearHistory() {
    localStorage.removeItem('awj_calculations');
  }

  /**
   * Uložení preferencí uživatele
   */
  static savePreferences(prefs) {
    localStorage.setItem('awj_preferences', JSON.stringify(prefs));
  }

  /**
   * Získání preferencí
   */
  static getPreferences() {
    const data = localStorage.getItem('awj_preferences');
    return data ? JSON.parse(data) : {
      defaultMaterial: 'steel',
      defaultPressure: 380,
      saveHistory: true
    };
  }
}
```

## 📝 Příklad použití:
```javascript
// V main.js
import { CalculationService } from './services/calculationService.js';
import { StorageService } from './services/storageService.js';

async function calculateAWJ() {
  const params = {
    materialType: document.getElementById('materialType').value,
    thickness: parseFloat(document.getElementById('thickness').value),
    pressure: parseFloat(document.getElementById('pressure').value),
    // ... další parametry
  };

  try {
    // Zavolat backend API
    const results = await CalculationService.quickCalculate(params);

    // Zobrazit výsledky
    displayResults(results);

    // Uložit do local storage
    StorageService.saveCalculation({ params, results });

  } catch (error) {
    showError('Chyba při výpočtu: ' + error.message);
  }
}
```

## 🔗 Backend API Endpoints:
✅ Všechny tyto endpointy JIŽ FUNGUJÍ na backendu!

- `POST /api/calculations/quick_calculate/`
- `POST /api/calculations/`
- `GET /api/calculations/history/`
- `POST /api/calculations/batch_calculate/`
- `POST /api/calculations/optimize/`
- `GET /api/materials/`
- `GET /api/abrasives/`

## ⚠️ Status: 🚧 Backend funguje ✅ | Frontend service layer NENÍ implementován 🚧
