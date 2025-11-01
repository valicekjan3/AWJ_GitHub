# Utils - Pomocné funkce

## 📋 Účel
Znovupoužitelné utility funkce pro celou aplikaci

## 📁 Struktura:
```
utils/
├── validators.js        # Validace vstupů
├── formatters.js        # Formátování čísel, dat
├── constants.js         # Konstanty aplikace
├── calculations.js      # Pomocné matematické funkce
└── storage.js           # LocalStorage helpers
```

## 📝 Příklad validators.js:
```javascript
// validators.js
export const validatePressure = (pressure) => {
  if (pressure < 100 || pressure > 600) {
    return { valid: false, error: 'Tlak musí být mezi 100-600 MPa' };
  }
  return { valid: true };
};

export const validateThickness = (thickness) => {
  if (thickness < 0.1 || thickness > 500) {
    return { valid: false, error: 'Tloušťka musí být mezi 0.1-500 mm' };
  }
  return { valid: true };
};

export const validateAllParameters = (params) => {
  const errors = {};

  const pressureCheck = validatePressure(params.pressure);
  if (!pressureCheck.valid) errors.pressure = pressureCheck.error;

  const thicknessCheck = validateThickness(params.thickness);
  if (!thicknessCheck.valid) errors.thickness = thicknessCheck.error;

  return {
    valid: Object.keys(errors).length === 0,
    errors
  };
};
```

## 📝 Příklad formatters.js:
```javascript
// formatters.js
export const formatNumber = (num, decimals = 2) => {
  return parseFloat(num).toFixed(decimals);
};

export const formatCurrency = (amount) => {
  return new Intl.NumberFormat('cs-CZ', {
    style: 'currency',
    currency: 'CZK'
  }).format(amount);
};

export const formatSpeed = (speed) => {
  return `${formatNumber(speed, 1)} mm/min`;
};

export const formatPressure = (pressure) => {
  return `${formatNumber(pressure, 0)} MPa`;
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

export const PRESSURE_LIMITS = {
  MIN: 100,  // MPa
  MAX: 600   // MPa
};

export const THICKNESS_LIMITS = {
  MIN: 0.1,  // mm
  MAX: 500   // mm
};

export const DEFAULT_PARAMETERS = {
  pressure: 380,
  nozzleDiameter: 0.33,
  focusDiameter: 1.0,
  abrasiveFlow: 8,
  meshSize: 80
};
```

## 📝 Příklad calculations.js:
```javascript
// calculations.js
export const clamp = (value, min, max) => {
  return Math.min(Math.max(value, min), max);
};

export const interpolate = (value, min, max, targetMin, targetMax) => {
  const normalized = (value - min) / (max - min);
  return targetMin + normalized * (targetMax - targetMin);
};

export const roundToStep = (value, step) => {
  return Math.round(value / step) * step;
};
```

## 💡 Použití v komponentách:
```jsx
import { validateAllParameters } from '../utils/validators';
import { formatSpeed, formatCurrency } from '../utils/formatters';
import { DEFAULT_PARAMETERS } from '../utils/constants';

const MyComponent = () => {
  const [params, setParams] = useState(DEFAULT_PARAMETERS);

  const handleSubmit = () => {
    const validation = validateAllParameters(params);
    if (!validation.valid) {
      console.error(validation.errors);
      return;
    }
    // Pokračovat s výpočtem...
  };

  return (
    <div>
      <p>Rychlost: {formatSpeed(150)}</p>
      <p>Náklady: {formatCurrency(250)}</p>
    </div>
  );
};
```
