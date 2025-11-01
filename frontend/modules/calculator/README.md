# Calculator Module

## 📋 Účel
Modul pro výpočty AWJ parametrů (reaktivní React/Vue.js komponenty)

## ⚠️ AKTUÁLNÍ STAV
**Výpočty JIŽ FUNGUJÍ!** V `static/js/modules/calculator/calculations.js` (300 řádků)

## 🎯 Budoucí React struktura:
```
calculator/
├── CalculatorModule.jsx           # Hlavní komponenta
├── components/
│   ├── MaterialSelector.jsx      # Výběr materiálu
│   ├── ParameterInputs.jsx        # Vstupní parametry
│   ├── ResultsDisplay.jsx         # Zobrazení výsledků
│   └── OptimizationPanel.jsx     # AI optimalizace
├── hooks/
│   ├── useCalculation.js          # Custom hook pro výpočty
│   └── useOptimization.js         # Hook pro optimalizaci
├── calculationLogic.js            # Výpočetní logika
└── calculatorAPI.js               # API komunikace s backendem
```

## 📝 Příklad React komponenty:
```jsx
// CalculatorModule.jsx
import React, { useState } from 'react';
import { useCalculation } from './hooks/useCalculation';
import MaterialSelector from './components/MaterialSelector';
import ParameterInputs from './components/ParameterInputs';
import ResultsDisplay from './components/ResultsDisplay';

export const CalculatorModule = () => {
  const [params, setParams] = useState({
    materialType: 'steel',
    thickness: 10,
    pressure: 380,
    abrasiveFlow: 8
  });

  const { results, calculate, loading } = useCalculation();

  return (
    <div className="calculator-module">
      <MaterialSelector
        value={params.materialType}
        onChange={(val) => setParams({...params, materialType: val})}
      />
      <ParameterInputs
        params={params}
        onChange={setParams}
      />
      <button onClick={() => calculate(params)}>Vypočítat</button>
      <ResultsDisplay results={results} loading={loading} />
    </div>
  );
};
```

## 💡 Migrace ze static/:
1. Zkopírujte `calculations.js` logiku
2. Vytvořte React komponenty
3. Použijte useState/useReducer pro state
4. Připojte na backend API
