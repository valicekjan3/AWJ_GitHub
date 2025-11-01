# 📁 AWJ Calculator Pro - Modulární Struktura Projektu

## 🎯 Filozofie Architektury

Projekt je navržen jako **modulární, škálovatelný a snadno laditelný** systém s jasným oddělením odpovědností (Separation of Concerns).

## 📂 Struktura Projektu

```
awj-calculator-pro/
│
├── 📁 frontend/                      # Frontend komponenty a moduly
│   ├── 📁 components/               # Znovupoužitelné UI komponenty
│   │   ├── Button.js
│   │   ├── Card.js
│   │   ├── Input.js
│   │   ├── Chart.js
│   │   └── Modal.js
│   │
│   ├── 📁 modules/                  # Hlavní funkční moduly
│   │   ├── 📁 calculator/          # Modul kalkulátoru
│   │   │   ├── CalculatorUI.js
│   │   │   ├── CalculatorLogic.js
│   │   │   └── CalculatorValidation.js
│   │   │
│   │   ├── 📁 analysis/            # Modul analýzy sil
│   │   │   ├── ForceAnalysis.js
│   │   │   ├── ForceVisualization.js
│   │   │   └── ForceCalculations.js
│   │   │
│   │   ├── 📁 visualization/       # 3D vizualizace
│   │   │   ├── ThreeJSScene.js
│   │   │   ├── AWJModel.js
│   │   │   └── Animations.js
│   │   │
│   │   ├── 📁 ai/                  # AI optimalizace
│   │   │   ├── AIOptimizer.js
│   │   │   ├── PredictionEngine.js
│   │   │   └── MLModels.js
│   │   │
│   │   ├── 📁 chatbot/             # AI Chatbot
│   │   │   ├── ChatbotUI.js
│   │   │   ├── ChatbotLogic.js
│   │   │   └── NLPProcessor.js
│   │   │
│   │   └── 📁 games/               # Edukační hry
│   │       ├── AWJGame.js
│   │       ├── GameLogic.js
│   │       └── Leaderboard.js
│   │
│   ├── 📁 services/                 # API komunikace a služby
│   │   ├── APIService.js
│   │   ├── DatabaseService.js
│   │   └── AuthService.js
│   │
│   └── 📁 utils/                    # Pomocné funkce
│       ├── validators.js
│       ├── formatters.js
│       ├── math.js
│       └── logger.js
│
├── 📁 backend/                       # Django Backend
│   ├── 📁 apps/                     # Django aplikace
│   │   ├── 📁 calculations/        # Výpočty AWJ
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── serializers.py
│   │   │   ├── services.py
│   │   │   └── tests.py
│   │   │
│   │   ├── 📁 analysis/            # Analýza sil
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── services.py
│   │   │   └── algorithms.py
│   │   │
│   │   ├── 📁 ai_optimization/     # AI optimalizace
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── ml_engine.py
│   │   │   └── optimizer.py
│   │   │
│   │   └── 📁 chatbot/             # Chatbot backend
│   │       ├── models.py
│   │       ├── views.py
│   │       ├── ai_engine.py
│   │       └── responses.py
│   │
│   ├── 📁 core/                     # Jádro aplikace
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── middleware.py
│   │
│   └── 📁 utils/                    # Backend utility
│       ├── validators.py
│       ├── calculations.py
│       ├── error_handlers.py
│       └── logger.py
│
├── 📁 static/                        # Statické soubory
│   ├── 📁 css/
│   │   ├── main.css                # Základní styly
│   │   ├── 📁 components/          # CSS komponenty
│   │   │   ├── button.css
│   │   │   ├── card.css
│   │   │   ├── input.css
│   │   │   └── navbar.css
│   │   │
│   │   └── 📁 modules/             # CSS modulů
│   │       ├── calculator.css
│   │       ├── analysis.css
│   │       ├── visualization.css
│   │       └── chatbot.css
│   │
│   ├── 📁 js/
│   │   ├── main.js                 # Hlavní entry point
│   │   ├── config.js               # Konfigurace
│   │   │
│   │   ├── 📁 modules/             # JS moduly (zrcadlí frontend/)
│   │   │   ├── 📁 calculator/
│   │   │   │   ├── index.js
│   │   │   │   ├── calculations.js
│   │   │   │   └── validation.js
│   │   │   │
│   │   │   ├── 📁 analysis/
│   │   │   │   ├── index.js
│   │   │   │   ├── force-analysis.js
│   │   │   │   └── charts.js
│   │   │   │
│   │   │   └── ...
│   │   │
│   │   ├── 📁 services/            # API a služby
│   │   │   ├── api.service.js
│   │   │   ├── storage.service.js
│   │   │   └── notification.service.js
│   │   │
│   │   └── 📁 utils/               # Pomocné funkce
│   │       ├── constants.js
│   │       ├── helpers.js
│   │       ├── validators.js
│   │       └── logger.js
│   │
│   └── 📁 images/                   # Obrázky a ikony
│       ├── logo.svg
│       ├── icon-192.png
│       └── icon-512.png
│
├── 📁 templates/                     # HTML šablony
│   ├── base.html                   # Základní šablona
│   ├── index.html                  # Hlavní stránka
│   └── 📁 modules/                 # Modulární šablony
│       ├── calculator.html
│       ├── analysis.html
│       └── chatbot.html
│
├── 📁 config/                        # Konfigurační soubory
│   ├── development.json
│   ├── production.json
│   ├── testing.json
│   └── constants.json
│
├── 📁 tests/                         # Testy
│   ├── 📁 frontend/
│   │   ├── calculator.test.js
│   │   ├── analysis.test.js
│   │   └── utils.test.js
│   │
│   └── 📁 backend/
│       ├── test_calculations.py
│       ├── test_analysis.py
│       └── test_api.py
│
├── 📁 docs/                          # Dokumentace
│   ├── 📁 api/
│   │   ├── calculations.md
│   │   ├── analysis.md
│   │   └── optimization.md
│   │
│   ├── 📁 modules/
│   │   ├── calculator-module.md
│   │   ├── analysis-module.md
│   │   └── ai-module.md
│   │
│   ├── INSTALLATION.md
│   ├── DEVELOPMENT.md
│   └── DEPLOYMENT.md
│
├── requirements.txt                  # Python dependencies
├── package.json                      # Node.js dependencies (volitelné)
├── manage.py                         # Django management
├── README.md                         # Hlavní dokumentace
└── .env.example                      # Environment variables template

```

## 🔧 Moduly a jejich Odpovědnosti

### 1️⃣ **Calculator Module** (`modules/calculator/`)
**Odpovědnost:** Výpočty řezných parametrů AWJ
- Vstupní validace
- Fyzikální výpočty
- Optimalizace parametrů
- Export výsledků

**Soubory:**
- `CalculatorUI.js` - UI komponenta
- `CalculatorLogic.js` - Výpočetní logika
- `CalculatorValidation.js` - Validace vstupů

### 2️⃣ **Analysis Module** (`modules/analysis/`)
**Odpovědnost:** Analýza sil při řezání
- Výpočet složek sil (Fn, Ft, Fa)
- Časový průběh sil
- Statistická analýza
- Grafická vizualizace (2D grafy)

**Soubory:**
- `ForceAnalysis.js` - Hlavní analýza
- `ForceCalculations.js` - Výpočty sil
- `ForceVisualization.js` - Grafy Chart.js

### 3️⃣ **Visualization Module** (`modules/visualization/`)
**Odpovědnost:** 3D vizualizace procesu
- Three.js scéna
- 3D model AWJ
- Animace řezání
- Interaktivní ovládání

**Soubory:**
- `ThreeJSScene.js` - Inicializace scény
- `AWJModel.js` - 3D modely
- `Animations.js` - Animační logika

### 4️⃣ **AI Module** (`modules/ai/`)
**Odpovědnost:** AI optimalizace a predikce
- Optimalizace parametrů
- Predikce výsledků
- Machine Learning modely
- Doporučení

**Soubory:**
- `AIOptimizer.js` - Optimalizační engine
- `PredictionEngine.js` - Predikce
- `MLModels.js` - ML modely

### 5️⃣ **Chatbot Module** (`modules/chatbot/`)
**Odpovědnost:** AI asistent
- Natural Language Processing
- Odpovědi na dotazy
- Kontextová komunikace
- Historie konverzace

**Soubory:**
- `ChatbotUI.js` - UI chatbota
- `ChatbotLogic.js` - Logika konverzace
- `NLPProcessor.js` - Zpracování jazyka

### 6️⃣ **Games Module** (`modules/games/`)
**Odpovědnost:** Edukační hry
- Interaktivní výuka
- Gamifikace
- Leaderboard
- Progress tracking

**Soubory:**
- `AWJGame.js` - Herní engine
- `GameLogic.js` - Herní logika
- `Leaderboard.js` - Žebříček

## 🔗 Komunikace mezi moduly

### Frontend → Backend
```javascript
// Příklad: Calculator volá API
import { APIService } from '@/services/APIService';

const result = await APIService.calculate({
  material: 'steel',
  pressure: 380,
  thickness: 10
});
```

### Modul → Modul
```javascript
// Příklad: Calculator využívá Analysis
import { ForceAnalysis } from '@/modules/analysis/ForceAnalysis';

const forces = ForceAnalysis.calculateForces(parameters);
```

### Backend Django Apps
```python
# Příklad: Calculations využívá Analysis
from apps.analysis.services import ForceAnalysisService

forces = ForceAnalysisService.calculate_forces(params)
```

## 📋 Konvence Pojmenování

### JavaScript
- **Moduly:** PascalCase (`CalculatorLogic.js`)
- **Funkce:** camelCase (`calculateSpeed()`)
- **Konstanty:** UPPER_SNAKE_CASE (`MAX_PRESSURE`)
- **Komponenty:** PascalCase (`Button.js`)

### Python
- **Soubory:** snake_case (`force_analysis.py`)
- **Třídy:** PascalCase (`ForceAnalyzer`)
- **Funkce:** snake_case (`calculate_forces()`)
- **Konstanty:** UPPER_SNAKE_CASE (`MAX_PRESSURE`)

### CSS
- **Soubory:** kebab-case (`calculator-module.css`)
- **Třídy:** BEM (`card__title--primary`)
- **ID:** camelCase (`calculatorForm`)

## 🐛 Ladění a Testování

### 1. Izolované testování modulů
```javascript
// test/frontend/calculator.test.js
import { CalculatorLogic } from '@/modules/calculator/CalculatorLogic';

test('calculates cutting speed correctly', () => {
  const result = CalculatorLogic.calculateSpeed({ /* params */ });
  expect(result).toBe(expected);
});
```

### 2. Logging
```javascript
import { Logger } from '@/utils/logger';

Logger.debug('Calculator', 'Starting calculation', params);
Logger.error('Calculator', 'Invalid input', error);
```

### 3. Error Handling
```javascript
try {
  const result = await CalculatorLogic.calculate(params);
} catch (error) {
  ErrorHandler.handle(error, 'Calculator Module');
}
```

## 🚀 Výhody Modulární Architektury

✅ **Snadné ladění** - Chyby jsou izolovány v konkrétním modulu
✅ **Testovatelnost** - Každý modul lze testovat samostatně
✅ **Znovupoužitelnost** - Moduly lze použít v jiných projektech
✅ **Škálovatelnost** - Snadné přidání nových modulů
✅ **Paralelní vývoj** - Tým může pracovat na různých modulech
✅ **Snadná údržba** - Jasná struktura a odpovědnosti
✅ **Performance** - Lazy loading modulů

## 📦 Import/Export Systém

### ES6 Modules (Frontend)
```javascript
// Export
export class CalculatorLogic { /* ... */ }
export const calculateSpeed = () => { /* ... */ };

// Import
import { CalculatorLogic, calculateSpeed } from './CalculatorLogic';
```

### Django (Backend)
```python
# Export
from .services import CalculationService

# Import
from apps.calculations.services import CalculationService
```

## 🔄 Životní Cyklus Modulu

1. **Inicializace** - Načtení závislostí
2. **Setup** - Nastavení konfigurace
3. **Runtime** - Provádění operací
4. **Cleanup** - Úklid zdrojů
5. **Destroy** - Zrušení modulu

## 📝 Příklad: Vytvoření nového modulu

```javascript
// 1. Vytvořit složku
modules/new-module/

// 2. Vytvořit soubory
NewModule.js         // Hlavní třída
NewModuleUI.js       // UI komponenta
NewModuleLogic.js    // Logika
index.js             // Export point

// 3. Implementovat
export class NewModule {
  constructor(config) {
    this.config = config;
  }

  init() { /* ... */ }
  destroy() { /* ... */ }
}

// 4. Registrovat v main.js
import { NewModule } from '@/modules/new-module';
```

---

**Vytvořeno:** 2024-11-01
**Autor:** AWJ Calculator Pro Team
**Verze:** 1.0.0
