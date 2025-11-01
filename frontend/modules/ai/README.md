# AI Module - AI Optimalizace

## 📋 Účel
Frontend komponenty pro AI optimalizaci AWJ parametrů

## 🎯 Funkcionalita
- Optimalizace pro maximální rychlost řezání
- Optimalizace pro minimální náklady
- Predikce opotřebení nástrojů
- Doporučení parametrů

## 📁 Budoucí struktura:
```
ai/
├── AIModule.jsx                    # Hlavní komponenta
├── components/
│   ├── OptimizationPanel.jsx      # Panel pro výběr cíle optimalizace
│   ├── ParameterRecommendations.jsx
│   └── OptimizationResults.jsx
├── hooks/
│   └── useOptimization.js
└── aiAPI.js                        # API pro backend AI
```

## 📝 Příklad použití:
```jsx
import { useOptimization } from './hooks/useOptimization';

const AIModule = () => {
  const { optimize, results } = useOptimization();

  const handleOptimize = () => {
    optimize({
      materialType: 'steel',
      thickness: 10,
      target: 'max_speed'  // nebo 'min_cost'
    });
  };

  return (
    <div>
      <button onClick={handleOptimize}>Optimalizovat</button>
      <OptimizationResults data={results} />
    </div>
  );
};
```

## 🔗 Backend API:
- `POST /api/calculations/optimize/` - Již funguje! ✅

## ⚠️ AKTUÁLNĚ
Základní optimalizace funguje v backendu:
- ✅ `AWJOptimizationService.optimize_for_speed()`
- ✅ `AWJOptimizationService.optimize_for_cost()`
