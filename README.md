# 🌊 AWJ Calculator Pro

**Professional Abrasive Water Jet Calculator with AI-Powered Optimization**

[![Django](https://img.shields.io/badge/Django-4.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-Enabled-orange.svg)](https://developers.google.com/web/progressive-web-apps)

## 🎯 O Projektu

AWJ Calculator Pro je **nejpokročilejší webová aplikace** pro výpočty a optimalizaci procesů abrazivního vodního paprsku (Abrasive Water Jet). Kombinuje vědecké výpočty, strojové učení a interaktivní vizualizace pro profesionální inženýry a techniky.

### ✨ Klíčové Vlastnosti

- 🧮 **Přesné Výpočty** - Řezná rychlost, síly, hydraulický výkon, náklady
- 📊 **Analýza Sil** - 2D/3D analýza rozkladu sil při řezání
- 🤖 **AI Optimalizace** - Machine learning pro optimální parametry
- 💬 **AI Chatbot** - Inteligentní asistent pro AWJ technologii
- 🎮 **Gamifikace** - Interaktivní výukové hry a simulace
- 📈 **Grafy** - Interaktivní 2D (Chart.js) a 3D (Three.js) vizualizace
- 📱 **PWA** - Funguje offline jako mobilní aplikace
- 🌍 **Multi-platform** - Web, Desktop, Mobile

## 🚀 Rychlý Start

### Předpoklady

- Python 3.10+
- pip
- virtualenv (doporučeno)
- Git

### Lokální Instalace

```bash
# 1. Klonování repositáře
git clone https://github.com/yourusername/awj-calculator-pro.git
cd awj-calculator-pro

# 2. Vytvoření virtuálního prostředí
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

# 3. Instalace závislostí
pip install -r requirements.txt

# 4. Migrace databáze
python manage.py migrate

# 5. Vytvoření superusera (admin)
python manage.py createsuperuser

# 6. Spuštění serveru
python manage.py runserver

# 7. Otevřete prohlížeč
http://localhost:8000
```

## 📦 Deployment na PythonAnywhere

Podrobný návod najdete v [PYTHONANYWHERE_DEPLOYMENT.md](docs/PYTHONANYWHERE_DEPLOYMENT.md)

**Rychlý přehled:**

1. Vytvořte účet na [PythonAnywhere.com](https://www.pythonanywhere.com)
2. Otevřete Bash console
3. Klonujte projekt: `git clone <your-repo-url>`
4. Vytvořte virtualenv: `mkvirtualenv --python=/usr/bin/python3.10 awj`
5. Instalujte dependencies: `pip install -r requirements.txt`
6. Nastavte Web app v PythonAnywhere dashboard
7. Hotovo!

## 🏗️ Architektura Projektu

```
awj-calculator-pro/
├── backend/              # Django Backend
│   ├── apps/            # Modulární Django aplikace
│   │   ├── calculations/
│   │   ├── analysis/
│   │   ├── ai_optimization/
│   │   └── chatbot/
│   └── core/            # Nastavení projektu
│
├── frontend/            # Frontend komponenty
│   └── modules/         # Modulární JS komponenty
│
├── static/              # Statické soubory
│   ├── css/            # Stylování
│   ├── js/             # JavaScript
│   └── images/         # Obrázky
│
├── templates/           # HTML šablony
└── docs/               # Dokumentace
```

Podrobný popis architektury: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

## 🔧 Moduly

### 1. Calculator Module
Výpočty řezných parametrů:
- Řezná rychlost
- Hydraulický výkon
- Průtok vody
- Spotřeba abraziva
- Drsnost povrchu
- Náklady na řez

### 2. Analysis Module
Analýza sil při řezání:
- Normálová síla (Fn)
- Tečná síla (Ft)
- Axiální síla (Fa)
- Časový průběh sil
- Statistická analýza

### 3. AI Optimization Module
- Optimalizace parametrů pomocí ML
- Predikce výsledků
- Doporučení nastavení
- Učení z historických dat

### 4. Visualization Module
- 3D model AWJ procesu
- Interaktivní animace řezání
- Real-time vizualizace sil
- Částicový systém

### 5. Chatbot Module
- NLP zpracování dotazů
- Kontextová komunikace
- Databáze znalostí o AWJ
- História konverzace

### 6. Games Module
- Interaktivní simulace
- Výukové scénáře
- Leaderboard
- Achievement systém

## 📊 API Endpointy

### Calculations API
```
POST /api/calculations/calculate/
{
  "material": "steel",
  "thickness": 10,
  "pressure": 380,
  "nozzle_diameter": 0.33,
  "abrasive_flow": 8
}
```

### Analysis API
```
POST /api/analysis/forces/
{
  "parameters": { ... },
  "time_range": [0, 10]
}
```

### AI Optimization API
```
POST /api/ai/optimize/
{
  "target": "max_speed",
  "constraints": { ... }
}
```

Kompletní API dokumentace: [docs/api/](docs/api/)

## 🧪 Testování

```bash
# Spuštění všech testů
python manage.py test

# Frontend testy
npm test

# Coverage
pytest --cov=backend
```

## 🌐 Technologie

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - API
- **NumPy/SciPy** - Vědecké výpočty
- **Scikit-learn** - Machine Learning
- **TensorFlow/PyTorch** - Deep Learning

### Frontend
- **HTML5/CSS3** - Moderní design
- **Vanilla JavaScript** - ES6+ moduly
- **Chart.js** - 2D grafy
- **Three.js** - 3D vizualizace
- **Service Worker** - PWA podpora

### Database
- **SQLite** - Development
- **MySQL** - Production (PythonAnywhere)
- **PostgreSQL** - Alternativa

## 📱 PWA Funkce

- ✅ Offline funkčnost
- ✅ Instalace na plochu
- ✅ Push notifikace
- ✅ Background sync
- ✅ Responsivní design

## 🤝 Přispívání

Příspěvky jsou vítány! Postupujte podle těchto kroků:

1. Forkněte projekt
2. Vytvořte feature branch (`git checkout -b feature/AmazingFeature`)
3. Commitněte změny (`git commit -m 'Add AmazingFeature'`)
4. Pushněte do branch (`git push origin feature/AmazingFeature`)
5. Otevřete Pull Request

## 📖 Dokumentace

- [Instalační průvodce](docs/INSTALLATION.md)
- [Deployment na PythonAnywhere](docs/PYTHONANYWHERE_DEPLOYMENT.md)
- [Struktura projektu](PROJECT_STRUCTURE.md)
- [API dokumentace](docs/api/)
- [Moduly dokumentace](docs/modules/)
- [FAQ](docs/FAQ.md)

## 🐛 Hlášení Chyb

Našli jste chybu? [Vytvořte issue](https://github.com/yourusername/awj-calculator-pro/issues)

## 📄 Licence

Tento projekt je licencován pod MIT licencí - viz [LICENSE](LICENSE) pro detaily.

## 👨‍💻 Autoři

- **Váš

 Jméno** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Poděkování

- Inspirováno výzkumem AWJ technologie
- Děkujeme komunitě Django a Python
- Chart.js a Three.js vývojářům

## 📞 Kontakt

- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

## 🔗 Odkazy

- [Live Demo](https://yourusername.pythonanywhere.com)
- [Dokumentace](https://awj-calculator-docs.com)
- [Video Tutorial](https://youtube.com/watch?v=xxx)

---

**Made with ❤️ for AWJ Technology Engineers**

Last Updated: November 2024
Version: 1.0.0
