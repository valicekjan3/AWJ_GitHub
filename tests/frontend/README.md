# Frontend Tests

## 📋 Účel
Testy pro JavaScript/TypeScript frontend kód

## 🧪 Struktura testů:
```
frontend/
├── calculator.test.js        # Testy výpočtů
├── validation.test.js        # Testy validace
├── formatting.test.js        # Testy formátování
├── api.test.js               # Testy API komunikace
└── components.test.js        # Testy UI komponent (budoucí React)
```

## 📝 Příklad: calculator.test.js

```javascript
// calculator.test.js
import { AWJCalculations } from '../static/js/modules/calculator/calculations.js';

describe('AWJCalculations', () => {
  describe('calculateWaterFlow', () => {
    test('should calculate water flow correctly', () => {
      const flow = AWJCalculations.calculateWaterFlow(0.33, 380);

      expect(flow).toBeGreaterThan(0);
      expect(flow).toBeLessThan(10);
    });

    test('should return higher flow with higher pressure', () => {
      const flowLow = AWJCalculations.calculateWaterFlow(0.33, 200);
      const flowHigh = AWJCalculations.calculateWaterFlow(0.33, 400);

      expect(flowHigh).toBeGreaterThan(flowLow);
    });

    test('should return higher flow with larger nozzle', () => {
      const flowSmall = AWJCalculations.calculateWaterFlow(0.25, 380);
      const flowLarge = AWJCalculations.calculateWaterFlow(0.40, 380);

      expect(flowLarge).toBeGreaterThan(flowSmall);
    });

    test('should handle edge cases', () => {
      // Minimální hodnoty
      const flowMin = AWJCalculations.calculateWaterFlow(0.2, 100);
      expect(flowMin).toBeGreaterThan(0);

      // Maximální hodnoty
      const flowMax = AWJCalculations.calculateWaterFlow(0.5, 600);
      expect(flowMax).toBeGreaterThan(0);
    });
  });

  describe('calculateCuttingSpeed', () => {
    const baseParams = {
      thickness: 10,
      pressure: 380,
      abrasiveFlow: 8,
      nozzleDiameter: 0.33,
      focusDiameter: 1.0
    };

    test('should calculate cutting speed for steel', () => {
      const speed = AWJCalculations.calculateCuttingSpeed(
        'steel',
        ...Object.values(baseParams)
      );

      expect(speed).toBeGreaterThan(100);
      expect(speed).toBeLessThan(200);
    });

    test('aluminum should cut faster than steel', () => {
      const speedSteel = AWJCalculations.calculateCuttingSpeed(
        'steel',
        ...Object.values(baseParams)
      );
      const speedAluminum = AWJCalculations.calculateCuttingSpeed(
        'aluminum',
        ...Object.values(baseParams)
      );

      expect(speedAluminum).toBeGreaterThan(speedSteel);
    });

    test('thicker material should cut slower', () => {
      const speedThin = AWJCalculations.calculateCuttingSpeed(
        'steel',
        5,
        baseParams.pressure,
        baseParams.abrasiveFlow,
        baseParams.nozzleDiameter,
        baseParams.focusDiameter
      );
      const speedThick = AWJCalculations.calculateCuttingSpeed(
        'steel',
        20,
        baseParams.pressure,
        baseParams.abrasiveFlow,
        baseParams.nozzleDiameter,
        baseParams.focusDiameter
      );

      expect(speedThin).toBeGreaterThan(speedThick);
    });

    test('higher pressure should increase cutting speed', () => {
      const speedLow = AWJCalculations.calculateCuttingSpeed(
        'steel',
        baseParams.thickness,
        200,
        baseParams.abrasiveFlow,
        baseParams.nozzleDiameter,
        baseParams.focusDiameter
      );
      const speedHigh = AWJCalculations.calculateCuttingSpeed(
        'steel',
        baseParams.thickness,
        400,
        baseParams.abrasiveFlow,
        baseParams.nozzleDiameter,
        baseParams.focusDiameter
      );

      expect(speedHigh).toBeGreaterThan(speedLow);
    });
  });

  describe('performFullCalculation', () => {
    test('should return all required results', () => {
      const results = AWJCalculations.performFullCalculation({
        materialType: 'steel',
        thickness: 10.0,
        pressure: 380.0,
        nozzleDiameter: 0.33,
        focusDiameter: 1.0,
        abrasiveFlow: 8.0,
        meshSize: 80,
        standoffDistance: 3.0
      });

      // Zkontrolovat všechny klíče
      expect(results).toHaveProperty('waterFlow');
      expect(results).toHaveProperty('hydraulicPower');
      expect(results).toHaveProperty('cuttingSpeed');
      expect(results).toHaveProperty('cutDepth');
      expect(results).toHaveProperty('surfaceRoughness');
      expect(results).toHaveProperty('costPerMeter');

      // Všechny hodnoty by měly být kladné
      Object.values(results).forEach(value => {
        expect(value).toBeGreaterThan(0);
      });
    });
  });
});
```

## 📝 Příklad: validation.test.js

```javascript
// validation.test.js
import { Validators } from '../static/js/utils/validators.js';

describe('Validators', () => {
  describe('validatePressure', () => {
    test('should accept valid pressure', () => {
      const result = Validators.validatePressure(380);
      expect(result.valid).toBe(true);
    });

    test('should reject pressure below minimum', () => {
      const result = Validators.validatePressure(50);
      expect(result.valid).toBe(false);
      expect(result.error).toBeDefined();
    });

    test('should reject pressure above maximum', () => {
      const result = Validators.validatePressure(700);
      expect(result.valid).toBe(false);
      expect(result.error).toBeDefined();
    });

    test('should handle edge cases', () => {
      expect(Validators.validatePressure(100).valid).toBe(true);  // Min
      expect(Validators.validatePressure(600).valid).toBe(true);  // Max
      expect(Validators.validatePressure(99.9).valid).toBe(false);
      expect(Validators.validatePressure(600.1).valid).toBe(false);
    });
  });

  describe('validateThickness', () => {
    test('should accept valid thickness', () => {
      expect(Validators.validateThickness(10).valid).toBe(true);
    });

    test('should reject negative thickness', () => {
      expect(Validators.validateThickness(-5).valid).toBe(false);
    });

    test('should reject thickness above maximum', () => {
      expect(Validators.validateThickness(600).valid).toBe(false);
    });
  });

  describe('validateAllParameters', () => {
    test('should validate all parameters correctly', () => {
      const params = {
        pressure: 380,
        thickness: 10,
        abrasiveFlow: 8
      };

      const result = Validators.validateAllParameters(params);
      expect(result.valid).toBe(true);
      expect(Object.keys(result.errors).length).toBe(0);
    });

    test('should return errors for invalid parameters', () => {
      const params = {
        pressure: 700,    // Invalid
        thickness: -5,    // Invalid
        abrasiveFlow: 25  // Invalid
      };

      const result = Validators.validateAllParameters(params);
      expect(result.valid).toBe(false);
      expect(Object.keys(result.errors).length).toBe(3);
    });
  });
});
```

## 📝 Příklad: formatting.test.js

```javascript
// formatting.test.js
import { Formatters } from '../static/js/utils/formatters.js';

describe('Formatters', () => {
  describe('formatNumber', () => {
    test('should format number with default decimals', () => {
      expect(Formatters.formatNumber(123.456)).toBe('123.46');
    });

    test('should format number with custom decimals', () => {
      expect(Formatters.formatNumber(123.456, 1)).toBe('123.5');
      expect(Formatters.formatNumber(123.456, 3)).toBe('123.456');
    });

    test('should handle invalid input', () => {
      expect(Formatters.formatNumber(NaN)).toBe('-');
    });
  });

  describe('formatSpeed', () => {
    test('should format speed with unit', () => {
      expect(Formatters.formatSpeed(150.234)).toBe('150.2 mm/min');
    });
  });

  describe('formatCurrency', () => {
    test('should format currency in CZK', () => {
      const result = Formatters.formatCurrency(1234.56);
      expect(result).toContain('1');
      expect(result).toContain('234');
      expect(result).toContain('56');
    });
  });

  describe('formatTime', () => {
    test('should format seconds', () => {
      expect(Formatters.formatTime(45)).toBe('45s');
    });

    test('should format minutes and seconds', () => {
      expect(Formatters.formatTime(125)).toBe('2m 5s');
    });

    test('should format hours and minutes', () => {
      expect(Formatters.formatTime(3665)).toBe('1h 1m');
    });
  });
});
```

## 🚀 Spuštění testů:

### Setup (npm/yarn):
```bash
npm install --save-dev jest @testing-library/jest-dom
```

### package.json:
```json
{
  "scripts": {
    "test": "jest",
    "test:watch": "jest --watch",
    "test:coverage": "jest --coverage"
  },
  "jest": {
    "testEnvironment": "jsdom",
    "coverageDirectory": "coverage",
    "collectCoverageFrom": [
      "static/js/**/*.js",
      "!static/js/**/*.test.js"
    ]
  }
}
```

### Spuštění:
```bash
# Všechny testy
npm test

# Watch mode (běží při změnách)
npm run test:watch

# S coverage reportem
npm run test:coverage
```

## 📊 Coverage Report:
Po spuštění s coverage otevřete `coverage/lcov-report/index.html`

## 💡 Doporučení pro testování UI (React):
```javascript
// components.test.js (budoucí React komponenty)
import { render, screen, fireEvent } from '@testing-library/react';
import { CalculatorModule } from '../frontend/modules/calculator/CalculatorModule';

describe('CalculatorModule', () => {
  test('should render calculator form', () => {
    render(<CalculatorModule />);

    expect(screen.getByLabelText(/materiál/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/tloušťka/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/tlak/i)).toBeInTheDocument();
  });

  test('should calculate on button click', async () => {
    render(<CalculatorModule />);

    // Vyplnit formulář
    fireEvent.change(screen.getByLabelText(/tlak/i), {
      target: { value: '380' }
    });

    // Kliknout na tlačítko
    fireEvent.click(screen.getByText(/vypočítat/i));

    // Počkat na výsledky
    const result = await screen.findByText(/řezná rychlost/i);
    expect(result).toBeInTheDocument();
  });
});
```

## ⚠️ Status: 🚧 PŘIPRAVENO - Testy čekají na implementaci
JavaScript kód je funkční ✅, testy připraveny k psaní 🚧
