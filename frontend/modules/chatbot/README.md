# Chatbot Module

## 📋 Účel
AI asistent pro dotazy o AWJ technologii

## 🎯 Funkcionalita
- Odpovědi na otázky o AWJ
- Doporučení parametrů
- Řešení problémů
- Kontextová konverzace

## 📁 Budoucí struktura:
```
chatbot/
├── ChatbotModule.jsx
├── components/
│   ├── ChatWindow.jsx             # Hlavní chat okno
│   ├── MessageList.jsx            # Seznam zpráv
│   ├── MessageInput.jsx           # Vstup zprávy
│   ├── QuickActions.jsx           # Rychlé akce
│   └── SuggestedQuestions.jsx     # Navrhované otázky
├── hooks/
│   └── useChatbot.js
└── chatbotAPI.js                  # WebSocket API
```

## 📝 Příklad React komponenty:
```jsx
import React, { useState } from 'react';
import { useChatbot } from './hooks/useChatbot';

const ChatbotModule = () => {
  const { messages, sendMessage, loading } = useChatbot();
  const [input, setInput] = useState('');

  const handleSend = () => {
    sendMessage(input);
    setInput('');
  };

  return (
    <div className="chatbot">
      <MessageList messages={messages} />
      <MessageInput
        value={input}
        onChange={setInput}
        onSend={handleSend}
        disabled={loading}
      />
      <SuggestedQuestions
        questions={[
          'Jaké parametry zvolit pro ocel 10mm?',
          'Jak optimalizovat náklady?',
          'Co ovlivňuje drsnost povrchu?'
        ]}
        onSelect={sendMessage}
      />
    </div>
  );
};
```

## 🔗 Backend:
- WebSocket nebo REST API pro chat
- OpenAI GPT API doporučeno
- Backend v `backend/apps/chatbot/` - vyžaduje implementaci

## ⚠️ AKTUÁLNĚ
UI chatbota je připraveno v `templates/index.html` ✅
Backend vyžaduje implementaci 🚧
