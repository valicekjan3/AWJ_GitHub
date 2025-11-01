# AI Module - JavaScript

## 📋 Účel
JavaScript logika pro AI optimalizaci AWJ parametrů

## ⚠️ AKTUÁLNÍ STAV
Složka je PRÁZDNÁ - AI optimalizace zatím běží pouze na backendu ✅

## 🎯 Budoucí implementace

### Plánované soubory:
```
ai/
├── optimization.js        # Optimalizační algoritmy
├── predictions.js         # Predikce výsledků
├── recommendations.js     # Doporučení parametrů
└── aiHelpers.js          # Pomocné funkce
```

## 📝 Příklad optimization.js:
```javascript
// optimization.js
export class AIOptimization {
  /**
   * Optimalizace parametrů pro maximální rychlost
   */
  static async optimizeForSpeed(baseParams) {
    const response = await fetch('/api/calculations/optimize/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...baseParams,
        target: 'max_speed'
      })
    });

    return await response.json();
  }

  /**
   * Optimalizace parametrů pro minimální náklady
   */
  static async optimizeForCost(baseParams) {
    const response = await fetch('/api/calculations/optimize/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ...baseParams,
        target: 'min_cost'
      })
    });

    return await response.json();
  }

  /**
   * Predikce výsledků pro různé parametry
   */
  static predictResults(materialType, thickness, paramVariations) {
    // Grid search napříč parametry
    const predictions = [];

    for (const params of paramVariations) {
      const result = AWJCalculations.performFullCalculation({
        materialType,
        thickness,
        ...params
      });
      predictions.push({ params, result });
    }

    return predictions;
  }
}
```

## 🔗 Backend API:
- ✅ `POST /api/calculations/optimize/` - Již funguje!
- Backend má `AWJOptimizationService` s funkcemi:
  - `optimize_for_speed()`
  - `optimize_for_cost()`

## 💡 Implementace:
Frontend může volat backend API nebo implementovat vlastní optimalizační algoritmy v JavaScriptu
