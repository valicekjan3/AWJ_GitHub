# Components - UI Komponenty

## 📋 Účel
Znovupoužitelné UI komponenty pro budoucí React/Vue.js aplikaci

## 🎯 Plánované komponenty

### Základní UI komponenty:
```
components/
├── Button/
│   ├── Button.jsx
│   ├── Button.css
│   └── Button.test.js
├── Input/
│   ├── Input.jsx
│   └── Input.css
├── Slider/
│   └── Slider.jsx
├── Card/
│   └── Card.jsx
├── Modal/
│   └── Modal.jsx
└── Tabs/
    └── Tabs.jsx
```

## 📝 Příklad Button komponenty (React):
```jsx
// Button.jsx
import React from 'react';
import './Button.css';

export const Button = ({ children, variant = 'primary', onClick, disabled }) => {
  return (
    <button
      className={`btn btn-${variant}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children}
    </button>
  );
};
```

## 💡 Jak implementovat:
1. Vytvořte složku pro každou komponentu
2. Oddělte logiku (JSX) od stylů (CSS)
3. Přidejte testy (Jest + React Testing Library)
4. Použijte TypeScript pro type safety

## ⚠️ AKTUÁLNĚ
UI komponenty jsou zatím v `templates/index.html` jako HTML elementy
