# CSS Modules

## 📋 Účel
Styly specifické pro jednotlivé moduly aplikace

## 📁 Budoucí struktura:
```
modules/
├── calculator.css        # Styly pro kalkulátor
├── analysis.css          # Styly pro analýzu
├── chatbot.css           # Styly pro chatbot
├── visualization.css     # Styly pro grafy a 3D
└── games.css            # Styly pro gamifikaci
```

## 📝 Příklad calculator.css:
```css
/* calculator.css */
.calculator-section {
  background: white;
  border-radius: 20px;
  padding: 32px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
}

.calculator-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
  border-bottom: 2px solid #E0F2FE;
}

.calculator-tab {
  padding: 12px 24px;
  background: transparent;
  border: none;
  border-bottom: 3px solid transparent;
  cursor: pointer;
  font-weight: 600;
  color: var(--text-medium);
  transition: all 0.3s ease;
}

.calculator-tab.active {
  color: var(--primary-blue);
  border-bottom-color: var(--primary-blue);
}

.calculator-results {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 24px;
}

.result-card {
  background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
  border-radius: 12px;
  padding: 20px;
  border-left: 4px solid var(--primary-blue);
}

.result-label {
  font-size: 14px;
  color: var(--text-medium);
  margin-bottom: 8px;
}

.result-value {
  font-size: 28px;
  font-weight: 700;
  color: var(--primary-blue);
}

.result-unit {
  font-size: 16px;
  color: var(--text-medium);
  margin-left: 4px;
}
```

## 📝 Příklad chatbot.css:
```css
/* chatbot.css */
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 400px;
  max-width: calc(100vw - 40px);
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  display: flex;
  flex-direction: column;
  max-height: 600px;
  z-index: 1000;
}

.chatbot-header {
  background: linear-gradient(135deg, var(--primary-blue), #0052cc);
  color: white;
  padding: 20px;
  border-radius: 20px 20px 0 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chatbot-messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  background: #F0F9FF;
}

.chat-message {
  margin-bottom: 16px;
  display: flex;
  gap: 12px;
}

.message-user {
  justify-content: flex-end;
}

.message-user .message-bubble {
  background: var(--primary-blue);
  color: white;
}

.message-assistant .message-bubble {
  background: white;
  color: var(--text-dark);
}

.message-bubble {
  padding: 12px 16px;
  border-radius: 16px;
  max-width: 70%;
  word-wrap: break-word;
}

.chatbot-input {
  display: flex;
  padding: 16px;
  border-top: 1px solid #E0F2FE;
  gap: 8px;
}

.chatbot-input input {
  flex: 1;
  padding: 12px;
  border: 2px solid #E0F2FE;
  border-radius: 24px;
  outline: none;
}

.chatbot-input button {
  padding: 12px 24px;
  background: var(--primary-blue);
  color: white;
  border: none;
  border-radius: 24px;
  cursor: pointer;
}
```

## 📝 Příklad visualization.css:
```css
/* visualization.css */
.visualization-section {
  background: white;
  border-radius: 20px;
  padding: 32px;
  margin: 20px 0;
}

.chart-container {
  position: relative;
  height: 400px;
  margin: 20px 0;
}

.chart-controls {
  display: flex;
  gap: 12px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}

.chart-type-selector {
  padding: 8px 16px;
  background: white;
  border: 2px solid var(--primary-blue);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.chart-type-selector.active {
  background: var(--primary-blue);
  color: white;
}

.threejs-container {
  width: 100%;
  height: 500px;
  border-radius: 12px;
  overflow: hidden;
  background: linear-gradient(135deg, #F0F9FF 0%, #E0F2FE 100%);
}

.visualization-controls {
  display: flex;
  gap: 16px;
  margin-top: 20px;
  justify-content: center;
}

.control-button {
  padding: 10px 20px;
  background: white;
  border: 2px solid var(--primary-blue);
  border-radius: 8px;
  color: var(--primary-blue);
  cursor: pointer;
  transition: all 0.3s ease;
}

.control-button:hover {
  background: var(--primary-blue);
  color: white;
}
```

## 💡 Použití:
```html
<!-- V index.html -->
<link rel="stylesheet" href="/static/css/modules/calculator.css">
<link rel="stylesheet" href="/static/css/modules/chatbot.css">
<link rel="stylesheet" href="/static/css/modules/visualization.css">
```

## ⚠️ Status: 🚧 PŘIPRAVENO
Momentálně jsou všechny styly v `main.css` - funkční! ✅
Rozdělení do modulů je volitelné pro lepší organizaci
