# Chatbot Module - JavaScript

## 📋 Účel
JavaScript logika pro AI chatbot asistenta

## ⚠️ AKTUÁLNÍ STAV
UI chatbota je připraveno v `templates/index.html` ✅
JavaScript logika vyžaduje implementaci 🚧

## 📁 Budoucí struktura:
```
chatbot/
├── chatbot.js             # Hlavní chatbot logika
├── messageHandler.js      # Zpracování zpráv
├── nlp.js                 # Natural Language Processing
├── responses.js           # Předpřipravené odpovědi
└── websocket.js           # WebSocket komunikace
```

## 📝 Příklad chatbot.js:
```javascript
// chatbot.js
export class AWJChatbot {
  constructor() {
    this.messages = [];
    this.context = {};
  }

  /**
   * Odeslání zprávy
   */
  async sendMessage(userMessage) {
    this.messages.push({
      role: 'user',
      content: userMessage,
      timestamp: new Date()
    });

    // Detekce typu dotazu
    const intent = this.detectIntent(userMessage);
    const response = await this.generateResponse(intent, userMessage);

    this.messages.push({
      role: 'assistant',
      content: response,
      timestamp: new Date()
    });

    return response;
  }

  /**
   * Detekce záměru uživatele
   */
  detectIntent(message) {
    const lowerMsg = message.toLowerCase();

    if (lowerMsg.includes('parametr') || lowerMsg.includes('nastavení')) {
      return 'parameter_recommendation';
    }
    if (lowerMsg.includes('optimalizace') || lowerMsg.includes('optimální')) {
      return 'optimization';
    }
    if (lowerMsg.includes('náklady') || lowerMsg.includes('cena')) {
      return 'cost_inquiry';
    }
    if (lowerMsg.includes('rychlost') || lowerMsg.includes('rychle')) {
      return 'speed_inquiry';
    }
    if (lowerMsg.includes('materiál')) {
      return 'material_inquiry';
    }

    return 'general';
  }

  /**
   * Generování odpovědi
   */
  async generateResponse(intent, message) {
    switch (intent) {
      case 'parameter_recommendation':
        return await this.recommendParameters(message);

      case 'optimization':
        return 'Pro optimalizaci použijte AI Optimalizaci v hlavním menu. ' +
               'Můžete optimalizovat pro maximální rychlost nebo minimální náklady.';

      case 'cost_inquiry':
        return 'Náklady na řezání závisí na:\n' +
               '• Průtoku abraziva (cena abraziva)\n' +
               '• Rychlosti řezání (čas)\n' +
               '• Spotřebě energie\n' +
               'Použijte kalkulátor pro přesný výpočet.';

      case 'speed_inquiry':
        return 'Řezná rychlost závisí na:\n' +
               '• Typu materiálu\n' +
               '• Tloušťce materiálu\n' +
               '• Tlaku vody\n' +
               '• Průtoku abraziva\n' +
               'Zadejte parametry do kalkulátoru.';

      case 'material_inquiry':
        return 'Podporované materiály:\n' +
               '• Ocel (steel) - k=1.0\n' +
               '• Hliník (aluminum) - k=1.3\n' +
               '• Titan (titanium) - k=0.7\n' +
               '• Měď (copper) - k=1.1\n' +
               '• Sklo (glass) - k=0.9\n' +
               '• Keramika (ceramic) - k=0.6\n' +
               '• Kompozit (composite) - k=0.8';

      default:
        return 'Jak vám mohu pomoci s AWJ technologií? ' +
               'Ptejte se na parametry, materiály, optimalizaci nebo náklady.';
    }
  }

  /**
   * Doporučení parametrů
   */
  async recommendParameters(message) {
    // Extrakce materiálu a tloušťky ze zprávy
    const materialMatch = message.match(/ocel|hliník|titan|měď/i);
    const thicknessMatch = message.match(/(\d+)\s*mm/);

    if (!materialMatch || !thicknessMatch) {
      return 'Pro doporučení parametrů mi řekněte materiál a tloušťku. ' +
             'Například: "Jaké parametry pro ocel 10mm?"';
    }

    const material = this.normalizeMaterial(materialMatch[0]);
    const thickness = parseInt(thicknessMatch[1]);

    return `Doporučené parametry pro ${material} ${thickness}mm:\n` +
           `• Tlak: 380 MPa\n` +
           `• Průtok abraziva: ${thickness < 20 ? '8' : '12'} kg/h\n` +
           `• Průměr fokusační trysky: 1.0 mm\n` +
           `• Mesh abraziva: 80\n\n` +
           `Zadejte tyto hodnoty do kalkulátoru pro přesný výpočet.`;
  }

  /**
   * Normalizace názvu materiálu
   */
  normalizeMaterial(material) {
    const mapping = {
      'ocel': 'ocel',
      'hliník': 'hliník',
      'titan': 'titan',
      'měď': 'měď'
    };
    return mapping[material.toLowerCase()] || material;
  }
}
```

## 📝 Příklad použití:
```javascript
// V main.js
import { AWJChatbot } from './modules/chatbot/chatbot.js';

const chatbot = new AWJChatbot();

document.getElementById('sendChatBtn').addEventListener('click', async () => {
  const input = document.getElementById('chatInput');
  const message = input.value;

  if (!message.trim()) return;

  // Zobrazit zprávu uživatele
  displayMessage('user', message);

  // Získat odpověď
  const response = await chatbot.sendMessage(message);

  // Zobrazit odpověď bota
  displayMessage('assistant', response);

  input.value = '';
});
```

## 🚀 Pokročilá implementace:
Pro produkční použití implementujte:
1. **WebSocket** pro real-time komunikaci
2. **OpenAI API** pro inteligentní odpovědi
3. **Context management** pro udržení konverzace
4. **Intent classification** pomocí ML modelu

## 🔗 Backend:
Backend v `backend/apps/chatbot/` vyžaduje implementaci Django Channels + OpenAI API

## ⚠️ Status: 🚧 UI hotovo ✅ | Backend a JS logika 🚧
