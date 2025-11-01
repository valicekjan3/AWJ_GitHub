# Services - API komunikace

## 📋 Účel
Centralizovaná správa API komunikace s backendem

## 📁 Struktura:
```
services/
├── apiClient.js              # Hlavní axios/fetch wrapper
├── calculationService.js     # API pro výpočty
├── optimizationService.js    # API pro optimalizaci
├── chatbotService.js         # WebSocket pro chatbot
├── authService.js            # Autentizace (budoucí)
└── storageService.js         # Local/Session Storage
```

## 📝 Příklad API Client:
```javascript
// apiClient.js
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

export class APIClient {
  static async get(endpoint) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`);
    if (!response.ok) throw new Error('API Error');
    return response.json();
  }

  static async post(endpoint, data) {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('API Error');
    return response.json();
  }
}
```

## 📝 Příklad Calculation Service:
```javascript
// calculationService.js
import { APIClient } from './apiClient';

export class CalculationService {
  static async quickCalculate(params) {
    return APIClient.post('/calculations/quick_calculate/', params);
  }

  static async saveCalculation(params) {
    return APIClient.post('/calculations/', params);
  }

  static async getHistory() {
    return APIClient.get('/calculations/history/');
  }

  static async optimize(params, target) {
    return APIClient.post('/calculations/optimize/', {
      ...params,
      target  // 'max_speed' nebo 'min_cost'
    });
  }
}
```

## 📝 Použití v React:
```jsx
import { CalculationService } from '../services/calculationService';

const MyComponent = () => {
  const handleCalculate = async () => {
    try {
      const results = await CalculationService.quickCalculate({
        materialType: 'steel',
        thickness: 10,
        pressure: 380
      });
      console.log(results);
    } catch (error) {
      console.error('Chyba při výpočtu:', error);
    }
  };

  return <button onClick={handleCalculate}>Vypočítat</button>;
};
```

## 🔗 Backend API endpoints:
- ✅ `POST /api/calculations/quick_calculate/`
- ✅ `POST /api/calculations/`
- ✅ `GET /api/calculations/history/`
- ✅ `POST /api/calculations/optimize/`
- ✅ `GET /api/materials/`
- ✅ `GET /api/abrasives/`

## 💡 Doporučení:
- Použijte axios pro lepší error handling
- Implementujte retry logiku
- Přidejte caching (React Query)
- Error boundary pro API chyby
