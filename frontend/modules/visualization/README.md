# Visualization Module - Grafy a 3D vizualizace

## 📋 Účel
Interaktivní grafy a 3D vizualizace AWJ procesu

## 🎯 Funkcionalita
- 2D grafy (Chart.js)
- 3D simulace řezání (Three.js)
- Animace řezného procesu
- Interaktivní vizualizace parametrů

## 📁 Budoucí struktura:
```
visualization/
├── VisualizationModule.jsx
├── components/
│   ├── charts/
│   │   ├── CuttingSpeedChart.jsx
│   │   ├── CostAnalysisChart.jsx
│   │   └── ParameterComparisonChart.jsx
│   ├── 3d/
│   │   ├── ThreeJSScene.jsx       # Three.js scéna
│   │   ├── CuttingAnimation.jsx   # Animace řezání
│   │   └── NozzleModel.jsx        # 3D model tryski
│   └── InteractiveGraph.jsx
├── hooks/
│   ├── useChart.js
│   └── useThreeJS.js
└── visualizationHelpers.js
```

## 📝 Příklad Chart.js:
```jsx
import { Bar } from 'react-chartjs-2';

const CuttingSpeedChart = ({ materials, speeds }) => {
  const data = {
    labels: materials,
    datasets: [{
      label: 'Řezná rychlost [mm/min]',
      data: speeds,
      backgroundColor: 'rgba(0, 102, 255, 0.5)',
    }]
  };

  return <Bar data={data} options={{responsive: true}} />;
};
```

## 📝 Příklad Three.js:
```jsx
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';

const CuttingAnimation = () => {
  return (
    <Canvas>
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <mesh>
        <boxGeometry args={[1, 0.1, 1]} />
        <meshStandardMaterial color="silver" />
      </mesh>
      <OrbitControls />
    </Canvas>
  );
};
```

## 📦 Potřebné knihovny:
```bash
npm install chart.js react-chartjs-2
npm install three @react-three/fiber @react-three/drei
```

## ⚠️ AKTUÁLNĚ
- Chart.js a Three.js jsou připraveny v HTML ✅
- JavaScript implementace zatím NENÍ 🚧
