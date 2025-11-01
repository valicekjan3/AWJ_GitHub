# JavaScript Utils - Pomocné funkce

## 📋 Účel
Znovupoužitelné utility funkce pro celou aplikaci

## 📁 Budoucí struktura:
```
utils/
├── validators.js         # Validace vstupů
├── formatters.js        # Formátování hodnot
├── constants.js         # Konstanty
├── mathHelpers.js       # Matematické funkce
└── domHelpers.js        # DOM manipulace
```

## 📝 Příklad validators.js:
```javascript
// validators.js
export const Validators = {
  /**
   * Validace tlaku
   */
  validatePressure(pressure) {
    if (isNaN(pressure) || pressure < 100 || pressure > 600) {
      return {
        valid: false,
        error: 'Tlak musí být mezi 100-600 MPa'
      };
    }
    return { valid: true };
  },

  /**
   * Validace tloušťky
   */
  validateThickness(thickness) {
    if (isNaN(thickness) || thickness < 0.1 || thickness > 500) {
      return {
        valid: false,
        error: 'Tloušťka musí být mezi 0.1-500 mm'
      };
    }
    return { valid: true };
  },

  /**
   * Validace průtoku abraziva
   */
  validateAbrasiveFlow(flow) {
    if (isNaN(flow) || flow < 0 || flow > 20) {
      return {
        valid: false,
        error: 'Průtok abraziva musí být mezi 0-20 kg/h'
      };
    }
    return { valid: true };
  },

  /**
   * Validace všech parametrů
   */
  validateAllParameters(params) {
    const errors = {};

    const checks = [
      { field: 'pressure', validator: this.validatePressure },
      { field: 'thickness', validator: this.validateThickness },
      { field: 'abrasiveFlow', validator: this.validateAbrasiveFlow }
    ];

    for (const check of checks) {
      const result = check.validator(params[check.field]);
      if (!result.valid) {
        errors[check.field] = result.error;
      }
    }

    return {
      valid: Object.keys(errors).length === 0,
      errors
    };
  }
};
```

## 📝 Příklad formatters.js:
```javascript
// formatters.js
export const Formatters = {
  /**
   * Formátování čísla
   */
  formatNumber(num, decimals = 2) {
    if (isNaN(num)) return '-';
    return parseFloat(num).toFixed(decimals);
  },

  /**
   * Formátování měny
   */
  formatCurrency(amount, currency = 'CZK') {
    if (isNaN(amount)) return '-';
    return new Intl.NumberFormat('cs-CZ', {
      style: 'currency',
      currency: currency
    }).format(amount);
  },

  /**
   * Formátování rychlosti
   */
  formatSpeed(speed) {
    return `${this.formatNumber(speed, 1)} mm/min`;
  },

  /**
   * Formátování tlaku
   */
  formatPressure(pressure) {
    return `${this.formatNumber(pressure, 0)} MPa`;
  },

  /**
   * Formátování průtoku
   */
  formatFlow(flow) {
    return `${this.formatNumber(flow, 2)} l/min`;
  },

  /**
   * Formátování procent
   */
  formatPercent(value) {
    return `${this.formatNumber(value, 1)}%`;
  },

  /**
   * Formátování času
   */
  formatTime(seconds) {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    const s = Math.floor(seconds % 60);

    if (h > 0) return `${h}h ${m}m`;
    if (m > 0) return `${m}m ${s}s`;
    return `${s}s`;
  }
};
```

## 📝 Příklad constants.js:
```javascript
// constants.js
export const MATERIAL_TYPES = {
  STEEL: 'steel',
  ALUMINUM: 'aluminum',
  TITANIUM: 'titanium',
  COPPER: 'copper',
  GLASS: 'glass',
  CERAMIC: 'ceramic',
  COMPOSITE: 'composite'
};

export const MATERIAL_NAMES = {
  steel: 'Ocel',
  aluminum: 'Hliník',
  titanium: 'Titan',
  copper: 'Měď',
  glass: 'Sklo',
  ceramic: 'Keramika',
  composite: 'Kompozit'
};

export const LIMITS = {
  PRESSURE: { min: 100, max: 600, default: 380 },
  THICKNESS: { min: 0.1, max: 500, default: 10 },
  NOZZLE_DIAMETER: { min: 0.2, max: 0.5, default: 0.33 },
  FOCUS_DIAMETER: { min: 0.5, max: 2.0, default: 1.0 },
  ABRASIVE_FLOW: { min: 0, max: 20, default: 8 },
  MESH_SIZE: { min: 50, max: 120, default: 80 }
};

export const OPTIMIZATION_TARGETS = {
  MAX_SPEED: 'max_speed',
  MIN_COST: 'min_cost'
};

export const API_ENDPOINTS = {
  QUICK_CALCULATE: '/api/calculations/quick_calculate/',
  SAVE_CALCULATION: '/api/calculations/',
  OPTIMIZE: '/api/calculations/optimize/',
  HISTORY: '/api/calculations/history/',
  MATERIALS: '/api/materials/',
  ABRASIVES: '/api/abrasives/'
};
```

## 📝 Příklad mathHelpers.js:
```javascript
// mathHelpers.js
export const MathHelpers = {
  /**
   * Omezení hodnoty do rozsahu
   */
  clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  },

  /**
   * Lineární interpolace
   */
  lerp(start, end, t) {
    return start + (end - start) * t;
  },

  /**
   * Zaokrouhlení na krok
   */
  roundToStep(value, step) {
    return Math.round(value / step) * step;
  },

  /**
   * Normalizace hodnoty do rozsahu 0-1
   */
  normalize(value, min, max) {
    return (value - min) / (max - min);
  },

  /**
   * Převod mezi rozsahy
   */
  map(value, inMin, inMax, outMin, outMax) {
    const normalized = this.normalize(value, inMin, inMax);
    return this.lerp(outMin, outMax, normalized);
  },

  /**
   * Průměr pole čísel
   */
  average(numbers) {
    return numbers.reduce((a, b) => a + b, 0) / numbers.length;
  },

  /**
   * Výpočet procent
   */
  percentage(value, total) {
    return (value / total) * 100;
  }
};
```

## 📝 Příklad domHelpers.js:
```javascript
// domHelpers.js
export const DOMHelpers = {
  /**
   * Vytvoření HTML elementu
   */
  createElement(tag, className, textContent) {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (textContent) el.textContent = textContent;
    return el;
  },

  /**
   * Zobrazení/skrytí elementu
   */
  toggleElement(selector, show) {
    const el = document.querySelector(selector);
    if (el) {
      el.style.display = show ? 'block' : 'none';
    }
  },

  /**
   * Zobrazení loading stavu
   */
  showLoading(selector) {
    const el = document.querySelector(selector);
    if (el) {
      el.classList.add('loading');
      el.disabled = true;
    }
  },

  /**
   * Skrytí loading stavu
   */
  hideLoading(selector) {
    const el = document.querySelector(selector);
    if (el) {
      el.classList.remove('loading');
      el.disabled = false;
    }
  },

  /**
   * Zobrazení chybové zprávy
   */
  showError(message, duration = 5000) {
    const errorDiv = this.createElement('div', 'error-message', message);
    document.body.appendChild(errorDiv);

    setTimeout(() => {
      errorDiv.remove();
    }, duration);
  },

  /**
   * Synchronizace slider s input
   */
  syncSliderInput(sliderId, inputId) {
    const slider = document.getElementById(sliderId);
    const input = document.getElementById(inputId);

    if (!slider || !input) return;

    slider.addEventListener('input', () => {
      input.value = slider.value;
    });

    input.addEventListener('input', () => {
      slider.value = input.value;
    });
  }
};
```

## 📝 Příklad použití:
```javascript
// V main.js
import { Validators, Formatters, LIMITS, MathHelpers } from './utils/index.js';

function validateAndCalculate() {
  const pressure = parseFloat(document.getElementById('pressure').value);
  const thickness = parseFloat(document.getElementById('thickness').value);

  // Validace
  const validation = Validators.validateAllParameters({
    pressure,
    thickness,
    abrasiveFlow: 8
  });

  if (!validation.valid) {
    showErrors(validation.errors);
    return;
  }

  // Clamp hodnot
  const clampedPressure = MathHelpers.clamp(
    pressure,
    LIMITS.PRESSURE.min,
    LIMITS.PRESSURE.max
  );

  // Formátování výstupu
  const formattedSpeed = Formatters.formatSpeed(150);
  const formattedCost = Formatters.formatCurrency(250);

  console.log(`Rychlost: ${formattedSpeed}, Náklady: ${formattedCost}`);
}
```

## ⚠️ Status: 🚧 PŘIPRAVENO - Vyžaduje implementaci
Některé utility funkce jsou již v `static/js/main.js`, ale nejsou organizované do modulů
