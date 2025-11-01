# 🌐 PYTHONANYWHERE - Co nahrát a jak

## 🎯 Účel PythonAnywhere
PythonAnywhere = **Běžící aplikace online**
- Vaše aplikace dostupná 24/7 na internetu
- URL jako: `vasejmeno.pythonanywhere.com`
- Kdokoliv může používat vaši aplikaci
- ZDARMA pro malé projekty

---

## ✅ CO NAHRÁT NA PYTHONANYWHERE

### **Ne všechno! Jen to, co je potřeba k běhu.**

### 📋 Seznam souborů k nahrání:

#### 1. Backend kód (NUTNÉ) ✅
```
backend/
├── apps/
│   └── calculations/          # Hlavní aplikace
│       ├── models.py
│       ├── services.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       └── admin.py
└── core/
    ├── settings.py            # Konfigurace
    ├── urls.py
    └── wsgi.py                # Pro PythonAnywhere
```

#### 2. Frontend (NUTNÉ) ✅
```
static/
├── css/
│   └── main.css              # Styly
├── js/
│   ├── main.js               # Hlavní JS
│   └── modules/
│       └── calculator/
│           └── calculations.js
├── manifest.json              # PWA
└── sw.js                      # Service Worker

templates/
└── index.html                 # Hlavní HTML
```

#### 3. Konfigurace (NUTNÉ) ✅
```
manage.py                      # Django spouštěč
requirements.txt               # Seznam Python balíčků
```

#### 4. Dokumentace (VOLITELNÉ) 📄
```
README.md                      # Hlavní dokumentace
docs/                          # Další dokumentace
```

### ❌ CO NENAHRÁVAT

```
venv/                          # ❌ Vytvoří se na serveru
__pycache__/                   # ❌ Vytvoří se automaticky
*.pyc                          # ❌ Kompilované soubory
db.sqlite3                     # ❌ Vytvoří se nová databáze
.env                           # ❌ Nastavíte přímo na serveru
.git/                          # ❌ Git složka (velká)

frontend/                      # ❌ Prázdné složky s README
config/                        # ❌ Není potřeba
tests/                         # ❌ Testy neběží na serveru
```

**Proč to nenahrávat?**
- Zabírá místo
- Není potřeba pro běh aplikace
- Některé věci se vytvoří automaticky

---

## 🚀 JAK NAHRÁT (5 kroků)

### Krok 1: Registrace na PythonAnywhere

1. Jděte na: https://www.pythonanywhere.com
2. Klikněte **Pricing & signup**
3. Vyberte **Create a Beginner account** (ZDARMA)
4. Vyplňte:
   - **Username:** např. `vasejmeno` (bude v URL!)
   - **Email:** váš email
   - **Password:** silné heslo
5. Potvrďte email

✅ Váš web bude na: `https://vasejmeno.pythonanywhere.com`

---

### Krok 2: Nahrajte soubory

**Způsob A: Přes Git (DOPORUČENO)**

1. V PythonAnywhere otevřete **Consoles** → **Bash**
2. Zadejte:

```bash
# Klonujte projekt z GitHubu (ZMĚŇTE URL!)
git clone https://github.com/VASE-JMENO/awj-calculator-pro.git

# Přejděte do projektu
cd awj-calculator-pro

# Ověřte soubory
ls
```

✅ Měli byste vidět: `backend/`, `static/`, `templates/`, `manage.py`, atd.

**Způsob B: Ručně přes Files**

1. Klikněte **Files**
2. Nahrajte po jednom:
   - Složku `backend/`
   - Složku `static/`
   - Složku `templates/`
   - Soubor `manage.py`
   - Soubor `requirements.txt`

---

### Krok 3: Nainstalujte závislosti

V Bash console:

```bash
# Vytvořte virtuální prostředí
mkvirtualenv --python=/usr/bin/python3.10 awj-env

# Aktivujte (pokud není aktivní)
workon awj-env

# Nainstalujte balíčky
cd ~/awj-calculator-pro
pip install -r requirements.txt

# Vytvořte databázi
python manage.py migrate

# Vytvořte admin uživatele
python manage.py createsuperuser
# Zadejte username, email, heslo
```

✅ Všechno by mělo projít bez chyb

---

### Krok 4: Nastavte Web App

1. Klikněte **Web** v menu
2. Klikněte **Add a new web app**
3. Klikněte **Next** (doména `vasejmeno.pythonanywhere.com` je OK)
4. Vyberte **Manual configuration**
5. Vyberte **Python 3.10**
6. Klikněte **Next**

**Nastavení:**

#### A) Virtualenv
- **Virtualenv:** `/home/vasejmeno/.virtualenvs/awj-env`

#### B) Source code
- **Source code:** `/home/vasejmeno/awj-calculator-pro`

#### C) WSGI Configuration File
Klikněte na **WSGI configuration file** (odkaz) a NAHRAĎTE CELÝ OBSAH:

```python
import os
import sys

# Cesta k projektu
path = '/home/vasejmeno/awj-calculator-pro'
if path not in sys.path:
    sys.path.append(path)

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.core.settings'

# WSGI aplikace
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

⚠️ **ZMĚŇTE `vasejmeno`** na vaše skutečné username!

**Uložte:** Ctrl+S

#### D) Static Files

V sekci **Static files** přidejte:

| URL          | Directory                                        |
|--------------|--------------------------------------------------|
| `/static/`   | `/home/vasejmeno/awj-calculator-pro/static`      |

⚠️ **ZMĚŇTE `vasejmeno`**!

#### E) Reload

Klikněte zelené tlačítko **Reload vasejmeno.pythonanywhere.com**

---

### Krok 5: Ověření

1. Jděte na: `https://vasejmeno.pythonanywhere.com`

✅ **Měli byste vidět:**
- Formulář kalkulátoru
- Modrou a oranžovou barevnou schému
- Všechno funguje

❌ **Pokud vidíte chybu:**
- Klikněte **Log files** → **Error log**
- Najděte poslední chybu
- Opravte podle návodu níže

---

## 📊 Co běží na PythonAnywhere

### Struktura na serveru:
```
/home/vasejmeno/
├── awj-calculator-pro/        ← Váš projekt
│   ├── backend/
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   └── db.sqlite3             ← Databáze (vytvoří se)
└── .virtualenvs/
    └── awj-env/               ← Python balíčky
```

### Co se používá:
- ✅ `backend/` - Django aplikace
- ✅ `static/` - CSS, JavaScript
- ✅ `templates/` - HTML
- ✅ `db.sqlite3` - SQLite databáze (nová, prázdná)

### Co není potřeba:
- ❌ `frontend/`, `config/`, `tests/` - Dokumentace
- ❌ `.git/` - Git historie
- ❌ `venv/` - Lokální prostředí

---

## ⚙️ Nastavení Django pro PythonAnywhere

V souboru `backend/core/settings.py` změňte:

```python
# Vypněte debug mód
DEBUG = False

# Přidejte vaši doménu
ALLOWED_HOSTS = ['vasejmeno.pythonanywhere.com', 'localhost']

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Pro sběr static souborů
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'static'),
]
```

Pak v Bash console:
```bash
python manage.py collectstatic
```

---

## 🔄 Aktualizace aplikace

Když změníte kód a chcete aktualizovat na PythonAnywhere:

### Způsob A: Přes Git
```bash
# V PythonAnywhere Bash console
cd ~/awj-calculator-pro
git pull origin main
python manage.py migrate       # Pokud jsou změny v DB
python manage.py collectstatic --noinput

# Klikněte Reload v Web záložce
```

### Způsob B: Ručně
1. Nahrajte změněné soubory přes **Files**
2. Klikněte **Reload** v **Web** záložce

---

## 🗄️ Databáze na PythonAnywhere

### Vytvoření admin účtu
```bash
python manage.py createsuperuser
```

### Přístup k admin rozhraní
`https://vasejmeno.pythonanywhere.com/admin`

### Přidání testovacích dat
```bash
python manage.py shell
```
```python
from backend.apps.calculations.models import Material

Material.objects.create(
    name="Ocel",
    material_type="steel",
    tensile_strength=400.0,
    k_factor=1.0,
    density=7850.0
)
```

---

## 💾 Co je v databázi na serveru

**NOVÁ databáze** (prázdná):
- Žádné výpočty
- Žádní uživatelé (musíte vytvořit)
- Žádné materiály (můžete přidat)

**Je odděleně od vaší lokální databáze!**

---

## 📊 Porovnání GitHub vs PythonAnywhere

| Aspekt           | GitHub                     | PythonAnywhere          |
|------------------|----------------------------|-------------------------|
| **Účel**         | Záloha kódu                | Běžící aplikace         |
| **Co nahrát**    | VŠECHNO                    | Jen backend + frontend  |
| **Výsledek**     | Uložený projekt            | Živý web                |
| **URL**          | github.com/user/project    | user.pythonanywhere.com |
| **Databáze**     | ❌ Není                    | ✅ SQLite               |
| **Běží?**        | ❌ Ne (jen kód)            | ✅ Ano (živá aplikace)  |
| **Cena**         | ✅ Zdarma                  | ✅ Zdarma (basic)       |

---

## ✅ Checklist - PythonAnywhere hotovo

- [ ] Registrace na PythonAnywhere
- [ ] Soubory nahrány (přes Git nebo Files)
- [ ] Závislosti nainstalovány (`pip install -r requirements.txt`)
- [ ] Databáze vytvořena (`python manage.py migrate`)
- [ ] Web app nakonfigurována (WSGI, static files)
- [ ] Aplikace běží na `https://vasejmeno.pythonanywhere.com` ✅
- [ ] Admin účet vytvořen
- [ ] Výpočty fungují

---

## ❓ Časté problémy

### ❌ 500 Internal Server Error
Zkontrolujte **Error log**:
1. **Web** → **Log files** → **Error log**
2. Najděte poslední chybu
3. Časté příčiny:
   - Špatná cesta v WSGI (`vasejmeno` není změněno)
   - Chybí balíček (`pip install ...`)
   - Špatné `ALLOWED_HOSTS` v settings.py

### ❌ Static soubory se nenačítají (CSS chybí)
```bash
python manage.py collectstatic
```
A zkontrolujte **Static files** v Web záložce.

### ❌ ImportError: No module named ...
```bash
workon awj-env
pip install -r requirements.txt
```

### ❌ Změny se neprojeví
Klikněte **Reload** v **Web** záložce!

---

## 🎉 Hotovo!

Když vidíte aplikaci na `https://vasejmeno.pythonanywhere.com`:

✅ **Backend funguje** (Django, API)
✅ **Frontend funguje** (HTML, CSS, JS)
✅ **Databáze funguje** (SQLite)
✅ **Aplikace běží 24/7**

---

## 🎯 Souhrn: GitHub vs PythonAnywhere

### 📤 GitHub (záloha kódu)
```
Nahrajete: VŠECHNO
Výsledek: Uložený projekt
URL: github.com/user/awj-calculator-pro
```

### 🌐 PythonAnywhere (živá aplikace)
```
Nahrajete: Backend + Frontend + requirements.txt
Výsledek: Běžící web
URL: vasejmeno.pythonanywhere.com
```

**OBA jsou potřeba!**
- GitHub = bezpečná záloha
- PythonAnywhere = fungující aplikace

---

**Vaše aplikace je nyní ONLINE a kdokoliv ji může používat!** 🎊
