# Visualization Module - JavaScript

## 📋 Účel
JavaScript pro 2D grafy (Chart.js) a 3D vizualizace (Three.js)

## 🎯 Funkcionalita
- 2D grafy průběhu parametrů
- Porovnání materiálů
- Analýza nákladů
- 3D simulace řezání
- Animace AWJ procesu

## 📁 Budoucí struktura:
```
visualization/
├── charts/
│   ├── cuttingSpeedChart.js
│   ├── costAnalysisChart.js
│   ├── parameterComparisonChart.js
│   └── chartHelpers.js
├── 3d/
│   ├── threeScene.js
│   ├── cuttingAnimation.js
│   ├── nozzleModel.js
│   └── materialModel.js
└── visualizationManager.js
```

## 📝 Příklad Chart.js - Řezná rychlost:
```javascript
// charts/cuttingSpeedChart.js
export function createCuttingSpeedChart(materials, speeds) {
  const ctx = document.getElementById('cuttingSpeedChart').getContext('2d');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: materials.map(m => m.name),
      datasets: [{
        label: 'Řezná rychlost [mm/min]',
        data: speeds,
        backgroundColor: 'rgba(0, 102, 255, 0.6)',
        borderColor: 'rgba(0, 102, 255, 1)',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Porovnání řezných rychlostí pro různé materiály'
        },
        legend: {
          display: true
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Rychlost [mm/min]'
          }
        }
      }
    }
  });
}
```

## 📝 Příklad Chart.js - Analýza nákladů:
```javascript
// charts/costAnalysisChart.js
export function createCostAnalysisChart(data) {
  const ctx = document.getElementById('costChart').getContext('2d');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.thicknesses,
      datasets: [
        {
          label: 'Náklady na abrazivo',
          data: data.abrasiveCosts,
          borderColor: 'rgb(255, 107, 53)',
          backgroundColor: 'rgba(255, 107, 53, 0.1)',
        },
        {
          label: 'Náklady na energii',
          data: data.energyCosts,
          borderColor: 'rgb(0, 102, 255)',
          backgroundColor: 'rgba(0, 102, 255, 0.1)',
        },
        {
          label: 'Celkové náklady',
          data: data.totalCosts,
          borderColor: 'rgb(0, 208, 132)',
          backgroundColor: 'rgba(0, 208, 132, 0.1)',
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Analýza nákladů v závislosti na tloušťce materiálu'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: {
            display: true,
            text: 'Náklady [Kč/m]'
          }
        },
        x: {
          title: {
            display: true,
            text: 'Tloušťka [mm]'
          }
        }
      }
    }
  });
}
```

## 📝 Příklad Three.js - 3D scéna:
```javascript
// 3d/threeScene.js
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

export class AWJScene {
  constructor(containerId) {
    this.container = document.getElementById(containerId);

    // Scéna, kamera, renderer
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0xf0f9ff);

    this.camera = new THREE.PerspectiveCamera(
      75,
      this.container.clientWidth / this.container.clientHeight,
      0.1,
      1000
    );
    this.camera.position.set(5, 5, 5);

    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
    this.container.appendChild(this.renderer.domElement);

    // Ovládání
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;

    // Osvětlení
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    this.scene.add(ambientLight);

    const directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(10, 10, 10);
    this.scene.add(directionalLight);

    this.animate();
  }

  /**
   * Vytvoření materiálu (desky)
   */
  createMaterial(thickness, materialType) {
    const geometry = new THREE.BoxGeometry(10, thickness / 10, 10);

    const materialColors = {
      steel: 0x708090,
      aluminum: 0xc0c0c0,
      titanium: 0x878787,
      copper: 0xb87333
    };

    const material = new THREE.MeshStandardMaterial({
      color: materialColors[materialType] || 0x808080,
      metalness: 0.8,
      roughness: 0.2
    });

    const mesh = new THREE.Mesh(geometry, material);
    this.scene.add(mesh);
    return mesh;
  }

  /**
   * Vytvoření AWJ trysky
   */
  createNozzle() {
    const geometry = new THREE.CylinderGeometry(0.1, 0.05, 2, 32);
    const material = new THREE.MeshStandardMaterial({
      color: 0x0066ff,
      metalness: 0.9,
      roughness: 0.1
    });

    const nozzle = new THREE.Mesh(geometry, material);
    nozzle.position.set(0, 3, 0);
    this.scene.add(nozzle);
    return nozzle;
  }

  /**
   * Animace vodního paprsku
   */
  createWaterJet() {
    const geometry = new THREE.CylinderGeometry(0.01, 0.02, 3, 32);
    const material = new THREE.MeshBasicMaterial({
      color: 0x00d4ff,
      transparent: true,
      opacity: 0.6
    });

    const jet = new THREE.Mesh(geometry, material);
    jet.position.set(0, 1.5, 0);
    this.scene.add(jet);
    return jet;
  }

  /**
   * Animační smyčka
   */
  animate() {
    requestAnimationFrame(() => this.animate());
    this.controls.update();
    this.renderer.render(this.scene, this.camera);
  }

  /**
   * Resize handler
   */
  onWindowResize() {
    this.camera.aspect = this.container.clientWidth / this.container.clientHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
  }
}
```

## 📝 Příklad použití:
```javascript
// V main.js
import { createCuttingSpeedChart, createCostAnalysisChart } from './modules/visualization/charts/index.js';
import { AWJScene } from './modules/visualization/3d/threeScene.js';

// Vytvoření 2D grafu
const materials = [
  { name: 'Ocel', speed: 150 },
  { name: 'Hliník', speed: 195 },
  { name: 'Titan', speed: 105 }
];
createCuttingSpeedChart(materials, materials.map(m => m.speed));

// Vytvoření 3D scény
const scene = new AWJScene('threejs-container');
scene.createMaterial(10, 'steel');
scene.createNozzle();
scene.createWaterJet();
```

## 📦 Potřebné knihovny:
```html
<!-- Chart.js -->
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<!-- Three.js -->
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/examples/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/"
  }
}
</script>
```

## ⚠️ Status: 🚧 PŘIPRAVENO - Vyžaduje implementaci
Knihovny jsou načteny v HTML ✅, JavaScript implementace NENÍ 🚧
