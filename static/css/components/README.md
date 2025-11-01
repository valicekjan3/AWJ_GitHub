# CSS Components

## 📋 Účel
Samostatné CSS soubory pro jednotlivé UI komponenty

## ⚠️ AKTUÁLNÍ STAV
Všechny styly jsou momentálně v `static/css/main.css` (700 řádků) ✅
Tato složka je připravena pro budoucí rozdělení stylů

## 📁 Budoucí struktura:
```
components/
├── buttons.css           # Tlačítka
├── inputs.css            # Vstupní pole
├── sliders.css           # Posuvníky
├── cards.css             # Karty
├── tabs.css              # Záložky
├── modals.css            # Modální okna
├── forms.css             # Formuláře
└── loading.css           # Loading stavy
```

## 📝 Příklad buttons.css:
```css
/* buttons.css */
.btn {
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-blue), #0052cc);
  color: white;
  box-shadow: 0 4px 15px rgba(0, 102, 255, 0.3);
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 102, 255, 0.4);
}

.btn-secondary {
  background: white;
  color: var(--primary-blue);
  border: 2px solid var(--primary-blue);
}

.btn-secondary:hover {
  background: var(--primary-blue);
  color: white;
}

.btn-large {
  width: 100%;
  padding: 16px 32px;
  font-size: 18px;
}

.btn.loading {
  opacity: 0.6;
  cursor: not-allowed;
  pointer-events: none;
}
```

## 📝 Příklad inputs.css:
```css
/* inputs.css */
.input-group {
  margin-bottom: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: var(--text-dark);
}

.input-group input[type="number"],
.input-group select {
  width: 100%;
  padding: 12px;
  border: 2px solid #E0F2FE;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.input-group input:focus,
.input-group select:focus {
  outline: none;
  border-color: var(--primary-blue);
  box-shadow: 0 0 0 3px rgba(0, 102, 255, 0.1);
}

.input-group.error input {
  border-color: var(--error-red);
}

.input-error-message {
  color: var(--error-red);
  font-size: 14px;
  margin-top: 4px;
}
```

## 📝 Příklad cards.css:
```css
/* cards.css */
.card {
  background: white;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
}

.card-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 16px;
  border-bottom: 2px solid #F0F9FF;
}

.card-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-dark);
}

.card-icon {
  font-size: 24px;
  margin-right: 12px;
  color: var(--primary-blue);
}

.card-body {
  padding: 16px 0;
}
```

## 💡 Migrace z main.css:
Když budete chtít rozdělit styly:
1. Zkopírujte příslušné sekce z `main.css`
2. Vytvořte samostatné soubory v této složce
3. Importujte v `main.css`:
```css
/* main.css */
@import 'components/buttons.css';
@import 'components/inputs.css';
@import 'components/cards.css';
/* ... */
```

## 🎯 Výhody rozdělení:
- Lepší organizace kódu
- Snadnější maintenance
- Možnost lazy loading
- Znovupoužitelnost komponent

## ⚠️ Status: 🚧 PŘIPRAVENO
Momentálně používejte `static/css/main.css` - plně funkční! ✅
