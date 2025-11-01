# Chatbot Module - PŘIPRAVENO K IMPLEMENTACI

## 📋 Účel
AI asistent pro AWJ technologii

## 🎯 Plánovaná funkcionalita
- Natural Language Processing (NLP)
- Odpovědi na otázky o AWJ
- Doporučení parametrů
- Kontextová konverzace
- Historie chatu

## 🔧 Technologie
- OpenAI GPT API (doporučeno)
- Nebo vlastní model (BERT, GPT-2)
- Django channels pro WebSocket

## 📝 Implementace
1. Vytvořit `models.py` - ChatMessage, Conversation
2. Vytvořit `ai_engine.py` - NLP zpracování
3. Vytvořit WebSocket consumer
4. Frontend integrace

## 💡 Rychlý start
Pro prototyp použijte OpenAI API s předpřipravenými prompty o AWJ technologii.
