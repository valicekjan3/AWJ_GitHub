# 🚀 AWJ Calculator Pro - Deployment na PythonAnywhere

Kompletní návod pro nasazení AWJ Calculator Pro na PythonAnywhere

---

## 📋 Předpoklady

- GitHub účet (pro git clone)
- PythonAnywhere účet (FREE nebo PAID)
- Projekt nahraný na GitHubu

---

## 🔧 Krok 1: Registrace na PythonAnywhere

1. Jděte na [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Klikněte na **"Pricing & signup"**
3. Vyberte **"Create a Beginner account"** (ZDARMA)
4. Vyplňte registrační formulář
5. Potvrďte email

---

## 💻 Krok 2: Nahrání Projektu

### A) Přes Git (DOPORUČENO)

```bash
# 1. Otevřete PythonAnywhere Dashboard
# 2. Klikněte na "Consoles" → "Bash"

# 3. Klonujte váš repositář
git clone https://github.com/VASE-JMENO/awj-calculator-pro.git

# 4. Přejděte do složky
cd awj-calculator-pro

# 5. Zkontrolujte soubory
ls -la
```

### B) Přes Upload (Alternativa)

1. Vytvořte ZIP archiv projektu
2. V PythonAnywhere → **Files** → **Upload a file**
3. Nahrajte ZIP
4. V Bash console: `unzip awj-calculator-pro.zip`

---

## 🐍 Krok 3: Vytvoření Virtual Environment

```bash
# 1. Vytvořte virtualenv s Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 awj-env

# 2. Aktivujte (automaticky aktivováno při vytvoření)
# Pro manuální aktivaci později:
workon awj-env

# 3. Zkontrolujte Python verzi
python --version
# Mělo by zobrazit: Python 3.10.x
```

---

## 📦 Krok 4: Instalace Závislostí

```bash
# 1. Ujistěte se, že jste v projektu a virtualenv je aktivní
cd ~/awj-calculator-pro
workon awj-env

# 2. Upgrade pip
pip install --upgrade pip

# 3. Instalace dependencies
pip install -r requirements.txt

# Poznámka: Pokud TensorFlow selže (velký balíček):
# pip install --no-cache-dir tensorflow-cpu
```

---

## 🗄️ Krok 5: Databáze Setup

### Pro SQLite (Development/Free account):

```bash
# 1. Spusťte migrace
python manage.py migrate

# 2. Vytvořte superusera
python manage.py createsuperuser
# Username: admin
# Email: your@email.com
# Password: (bezpečné heslo)

# 3. Zkontrolujte databázi
ls -l db.sqlite3
```

### Pro MySQL (Paid account):

```bash
# 1. V PythonAnywhere → Databases → vytv

ořte MySQL databázi

# 2. Upravte backend/core/settings.py:
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vasejmeno$awjcalc',
        'USER': 'vasejmeno',
        'PASSWORD': 'vase-heslo',
        'HOST': 'vasejmeno.mysql.pythonanywhere-services.com',
    }
}
```

```bash
# 3. Nainstalujte MySQL client
pip install mysqlclient

# 4. Migrace
python manage.py migrate
python manage.py createsuperuser
```

---

## 🌐 Krok 6: Konfigurace Web App

### 1. Vytvoření Web App

1. V PythonAnywhere Dashboard → **Web**
2. **Add a new web app**
3. Vyberte doménu: `vasejmeno.pythonanywhere.com`
4. Framework: **Manual configuration**
5. Python version: **Python 3.10**

### 2. Konfigurace WSGI

1. V Web tab klikněte na **WSGI configuration file**
2. **SMAZAT celý obsah** a nahradit tímto:

```python
import os
import sys

# Cesta k projektu
path = '/home/VASEJMENO/awj-calculator-pro'
if path not in sys.path:
    sys.path.append(path)

# Virtualenv
virtualenv_path = '/home/VASEJMENO/.virtualenvs/awj-env'
activate_this = f'{virtualenv_path}/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'backend.core.settings'

# Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**DŮLEŽITÉ:** Nahraďte `VASEJMENO` vaším PythonAnywhere username!

### 3. Virtualenv Nastavení

1. V Web tab sekce **Virtualenv**
2. Zadejte cestu: `/home/VASEJMENO/.virtualenvs/awj-env`

### 4. Static Files

1. V Web tab sekce **Static files**
2. Přidejte:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/VASEJMENO/awj-calculator-pro/staticfiles` |
| `/media/` | `/home/VASEJMENO/awj-calculator-pro/media` |

---

## 📁 Krok 7: Collect Static Files

```bash
# 1. V Bash console
cd ~/awj-calculator-pro
workon awj-env

# 2. Collect static files
python manage.py collectstatic --noinput

# 3. Zkontrolujte
ls -l staticfiles/
```

---

## 🔐 Krok 8: Environment Variables

```bash
# 1. Vytvořte .env soubor
cd ~/awj-calculator-pro
nano .env

# 2. Vložte:
```

```env
DEBUG=False
SECRET_KEY=vase-tajny-klic-zde-min-50-znaku-nahodnych
ALLOWED_HOSTS=vasejmeno.pythonanywhere.com
```

```bash
# 3. Uložte: Ctrl+X, Y, Enter
```

---

## ✅ Krok 9: Finální Kroky

### 1. Zkontrolujte Settings

```bash
# Otevřete settings.py
nano backend/core/settings.py

# Zkontrolujte:
# - DEBUG = False (produkce)
# - ALLOWED_HOSTS obsahuje vaši doménu
# - SECRET_KEY je bezpečný
```

### 2. Reload Web App

1. V **Web** tab
2. Klikněte na zelené tlačítko **"Reload vasejmeno.pythonanywhere.com"**
3. Počkejte ~10 sekund

### 3. Testování

Otevřete v prohlížeči:
```
https://vasejmeno.pythonanywhere.com
```

Měla by se zobrazit hlavní stránka AWJ Calculator!

---

## 🐛 Troubleshooting

### Chyba: "ImportError: No module named..."

```bash
workon awj-env
pip install CHYBEJICI_MODUL
# Reload web app
```

### Chyba: "OperationalError: no such table"

```bash
cd ~/awj-calculator-pro
workon awj-env
python manage.py migrate
# Reload web app
```

### Static files se nenačítají

```bash
python manage.py collectstatic --noinput
# Zkontrolujte Static files mapping ve Web tab
# Reload web app
```

### Error 500

```bash
# Zkontrolujte error log ve Web tab
# Sekce "Log files" → error.log
```

---

## 🔄 Aktualizace Projektu

```bash
# 1. Pull changes z Gitu
cd ~/awj-calculator-pro
git pull origin main

# 2. Instalace nových dependencies (pokud jsou)
workon awj-env
pip install -r requirements.txt

# 3. Migrace (pokud jsou nové)
python manage.py migrate

# 4. Collect static
python manage.py collectstatic --noinput

# 5. Reload web app
# Ve Web tab klikněte Reload
```

---

## ⚙️ Pokročilá Konfigurace

### Automatické Reloading (GitHub Webhook)

1. V GitHubu → Settings → Webhooks
2. Add webhook
3. Payload URL: `https://www.pythonanywhere.com/user/VASEJMENO/webhook/`
4. Content type: `application/json`
5. Secret: (vygenerujte ve Web tab)

### Custom Doména

1. Upgrade na Paid account
2. Web tab → Add domain
3. Nastavte DNS záznamy

### HTTPS (automaticky aktivní)

PythonAnywhere poskytuje FREE SSL certifikát!

---

## 📊 Monitoring

### Sledování Logů

```bash
# Error log
tail -f /var/log/VASEJMENO.pythonanywhere.com.error.log

# Access log
tail -f /var/log/VASEJMENO.pythonanywhere.com.access.log

# Django log (pokud je nastavený)
tail -f ~/awj-calculator-pro/logs/django.log
```

### CPU/Memory Usage

- Dashboard → Account → Usage statistics

---

## 💾 Zálohování

```bash
# 1. Backup databáze
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# 2. Stáhnout přes Files tab nebo:
# In local terminal:
scp VASEJMENO@ssh.pythonanywhere.com:~/backup_*.json ./
```

---

## 🎉 Hotovo!

Vaše AWJ Calculator Pro aplikace běží na:
```
https://vasejmeno.pythonanywhere.com
```

### Admin Interface:
```
https://vasejmeno.pythonanywhere.com/admin
```

### API Endpoints:
```
https://vasejmeno.pythonanywhere.com/api/calculations/
https://vasejmeno.pythonanywhere.com/api/materials/
```

---

## 📞 Podpora

- **PythonAnywhere Forums:** [www.pythonanywhere.com/forums](https://www.pythonanywhere.com/forums)
- **Django Documentation:** [docs.djangoproject.com](https://docs.djangoproject.com)
- **Projekt GitHub:** Vytvořte issue

---

**Úspěšný deployment! 🚀**

_Poslední aktualizace: Listopad 2024_
