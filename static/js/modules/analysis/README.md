# Analysis Module - JavaScript

## 📋 Účel
JavaScript logika pro analýzu sil a procesů AWJ

## 🎯 Plánovaná funkcionalita
- Výpočet sil (Fn, Ft, Fa)
- Časový průběh sil
- Analýza vlivu parametrů
- Příprava dat pro grafy

## 📁 Budoucí struktura:
```
analysis/
├── forceCalculations.js   # Výpočty sil
├── timeSeriesAnalysis.js  # Časový průběh
├── parameterAnalysis.js   # Analýza vlivu parametrů
└── analysisHelpers.js     # Pomocné funkce
```

## 📝 Příklad forceCalculations.js:
```javascript
// forceCalculations.js
export class ForceAnalysis {
  /**
   * Výpočet normálové síly (Fn)
   * @param {number} pressure - Tlak [MPa]
   * @param {number} focusDiameter - Průměr fokusační trysky [mm]
   * @returns {number} Normálová síla [N]
   */
  static calculateNormalForce(pressure, focusDiameter) {
    const p_pa = pressure * 1e6; // MPa -> Pa
    const d_m = focusDiameter / 1000; // mm -> m
    const area = Math.PI * Math.pow(d_m / 2, 2);
    const force = p_pa * area;
    return parseFloat((force).toFixed(2));
  }

  /**
   * Výpočet tečné síly (Ft)
   * Empirický vztah založený na řezné rychlosti
   */
  static calculateTangentialForce(materialType, thickness, cuttingSpeed) {
    const materialFactors = {
      steel: 1.0,
      aluminum: 0.6,
      titanium: 1.4,
      copper: 0.7,
      glass: 0.4,
      ceramic: 0.8,
      composite: 0.9
    };

    const k = materialFactors[materialType] || 1.0;
    const ft = k * thickness * (1000 / cuttingSpeed);
    return parseFloat(ft.toFixed(2));
  }

  /**
   * Výpočet axiální síly (Fa)
   */
  static calculateAxialForce(normalForce, tangentialForce) {
    // Fa je typicky 10-20% Fn
    const fa = normalForce * 0.15;
    return parseFloat(fa.toFixed(2));
  }

  /**
   * Kompletní analýza sil
   */
  static performForceAnalysis(params) {
    const fn = this.calculateNormalForce(params.pressure, params.focusDiameter);
    const ft = this.calculateTangentialForce(
      params.materialType,
      params.thickness,
      params.cuttingSpeed
    );
    const fa = this.calculateAxialForce(fn, ft);

    return {
      normalForce: fn,
      tangentialForce: ft,
      axialForce: fa,
      resultantForce: Math.sqrt(fn**2 + ft**2 + fa**2)
    };
  }
}
```

## 📝 Příklad použití s Chart.js:
```javascript
// Příklad vytvoření grafu časového průběhu sil
import { ForceAnalysis } from './forceCalculations.js';

function createForceTimeSeriesChart(params, duration = 10) {
  const timePoints = [];
  const fnData = [];
  const ftData = [];

  for (let t = 0; t <= duration; t += 0.1) {
    timePoints.push(t);

    // Simulace časového průběhu (zjednodušeno)
    const forces = ForceAnalysis.performForceAnalysis(params);
    fnData.push(forces.normalForce);
    ftData.push(forces.tangentialForce);
  }

  return {
    labels: timePoints,
    datasets: [
      {
        label: 'Normálová síla (Fn)',
        data: fnData,
        borderColor: 'rgb(0, 102, 255)',
      },
      {
        label: 'Tečná síla (Ft)',
        data: ftData,
        borderColor: 'rgb(255, 107, 53)',
      }
    ]
  };
}
```

## 🔗 Backend:
Backend v `backend/apps/analysis/` je připravený, ale vyžaduje implementaci

## ⚠️ Status: 🚧 PŘIPRAVENO - Vyžaduje implementaci
