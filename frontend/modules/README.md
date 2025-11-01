# Modules - Funkční moduly aplikace

## 📋 Účel
Funkční moduly obsahující business logiku pro různé části aplikace

## 📁 Struktura
```
modules/
├── calculator/      # Výpočty AWJ parametrů
├── analysis/        # Analýza sil a procesů
├── chatbot/         # AI chatbot
├── ai/              # AI optimalizace
├── visualization/   # Grafy a 3D vizualizace
└── games/           # Gamifikace
```

## 🎯 Každý modul obsahuje:
- **Logic** - Business logika (výpočty, API volání)
- **Components** - React/Vue komponenty specifické pro modul
- **State** - Stav modulu (Redux/Vuex)
- **Types** - TypeScript definice

## 📝 Příklad struktury modulu:
```
calculator/
├── CalculatorModule.jsx       # Hlavní komponenta
├── calculatorLogic.js         # Business logika
├── calculatorState.js         # State management
├── calculatorAPI.js           # API komunikace
└── components/
    ├── MaterialSelector.jsx
    ├── ParameterInputs.jsx
    └── ResultsDisplay.jsx
```

## ⚠️ AKTUÁLNĚ
Funkční logika je v:
- ✅ `static/js/modules/calculator/calculations.js` (300 řádků)
- ✅ `static/js/main.js` (400 řádků)

## 💡 Migrace:
Zkopírujte logiku ze `static/js/modules/` a rozdělte do React/Vue komponent
