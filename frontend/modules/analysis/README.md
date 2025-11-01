# Analysis Module - Analýza sil

## 📋 Účel
Vizualizace a analýza sil při řezání AWJ

## 🎯 Funkcionalita
- Výpočet normálové síly (Fn)
- Výpočet tečné síly (Ft)
- Výpočet axiální síly (Fa)
- Časový průběh sil
- Graf průběhu řezání

## 📁 Budoucí struktura:
```
analysis/
├── AnalysisModule.jsx
├── components/
│   ├── ForceChart.jsx             # Graf sil (Chart.js)
│   ├── TimeSeriesChart.jsx        # Časový průběh
│   ├── ForceVectorDisplay.jsx     # Zobrazení vektorů sil
│   └── ParameterInfluence.jsx     # Vliv parametrů na síly
├── hooks/
│   └── useForceAnalysis.js
└── analysisAPI.js
```

## 📝 Příklad Chart.js grafu:
```jsx
import { Line } from 'react-chartjs-2';

const ForceChart = ({ forceData }) => {
  const data = {
    labels: forceData.time,
    datasets: [
      {
        label: 'Normálová síla (Fn)',
        data: forceData.fn,
        borderColor: 'rgb(0, 102, 255)',
      },
      {
        label: 'Tečná síla (Ft)',
        data: forceData.ft,
        borderColor: 'rgb(255, 107, 53)',
      }
    ]
  };

  return <Line data={data} />;
};
```

## 🔗 Backend:
Backend připraven v `backend/apps/analysis/` - vyžaduje implementaci

## ⚠️ Status: 🚧 PŘIPRAVENO - Vyžaduje implementaci backendu
