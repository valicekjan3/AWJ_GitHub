# 📤 GITHUB - Co nahrát a jak

## 🎯 Účel GitHub
GitHub = **Záloha vašeho kódu + portfolio**
- Bezpečně uložený projekt
- Verzování (historie změn)
- Sdílení s ostatními
- Můžete ukázat zaměstnavatelům

---

## ✅ CO NAHRÁT NA GITHUB

### **ODPOVĚĎ: VŠECHNO z projektu!**

Nahrajete celou složku:
```
C:\Users\KEAI\awj-calculator-pro\
```

### 📋 Seznam souborů, které se nahrají:

#### 1. Kód aplikace ✅
```
backend/                    # Django backend
static/                     # CSS, JavaScript, obrázky
templates/                  # HTML šablony
manage.py                   # Django spouštěč
```

#### 2. Konfigurace ✅
```
requirements.txt            # Seznam Python balíčků
.gitignore                  # Co NENAHRÁVAT
.env.example                # Vzor pro tajné údaje
```

#### 3. Dokumentace ✅
```
README.md                   # Hlavní dokumentace
TESTING_GUIDE.md            # Návod k testování
GITHUB_UPLOAD_GUIDE.md      # Návod k nahrání
WHATS_IMPLEMENTED.md        # Co funguje
PROJECT_STRUCTURE.md        # Struktura projektu
FINAL_PROJECT_SUMMARY.md    # Souhrn
docs/                       # Další dokumentace
```

#### 4. Připravené složky ✅
```
frontend/                   # README s návody pro budoucnost
config/                     # README s návody
tests/                      # README s návody
```

### ❌ CO SE NENAHRAJE (automaticky ignorováno)

Tyto soubory/složky jsou v `.gitignore` a **NENAHRAJÍ SE**:
```
venv/                       # Virtuální prostředí (velké!)
__pycache__/                # Python cache
*.pyc                       # Zkompilované soubory
db.sqlite3                  # Databáze (obsahuje data)
.env                        # Tajné údaje (hesla, klíče)
```

**Proč se to nenahrává?**
- `venv/` - každý si vytvoří vlastní
- `db.sqlite3` - každý má vlastní data
- `.env` - obsahuje tajné hesla

---

## 🚀 JAK NAHRÁT (3 kroky)

### Krok 1: Vytvořte repozitář na GitHub

1. Jděte na: https://github.com
2. Přihlaste se
3. Klikněte **+ → New repository**
4. Vyplňte:
   - **Repository name:** `awj-calculator-pro`
   - **Description:** `Advanced AWJ Calculator with AI optimization`
   - **Public** nebo **Private** (jak chcete)
   - ❌ NEZAŠKRTÁVEJTE "Add a README" (už ho máte!)
5. Klikněte **Create repository**
6. **ZKOPÍRUJTE URL** (např. `https://github.com/vase-jmeno/awj-calculator-pro.git`)

---

### Krok 2: Nahrajte projekt

Otevřete **Command Prompt** (Win + R → `cmd`):

```bash
# Přejděte do projektu
cd C:\Users\KEAI\awj-calculator-pro

# Inicializujte Git
git init

# Přidejte VŠECHNY soubory
git add .

# Vytvořte první verzi
git commit -m "AWJ Calculator Pro - První verze"

# Propojte s GitHub (ZMĚŇTE na vaši URL!)
git remote add origin https://github.com/VASE-JMENO/awj-calculator-pro.git

# Nahrajte
git branch -M main
git push -u origin main
```

⚠️ **DŮLEŽITÉ:**
- V příkazu `git remote add origin` změňte `VASE-JMENO` na vaše GitHub username!
- Při prvním `git push` vás GitHub požádá o přihlášení

---

### Krok 3: Ověření

1. Jděte na: `https://github.com/VASE-JMENO/awj-calculator-pro`
2. Měli byste vidět:
   - ✅ Složky: `backend/`, `static/`, `templates/`, `docs/`
   - ✅ Soubory: `README.md`, `requirements.txt`, `manage.py`
   - ✅ README.md se zobrazuje na hlavní stránce

---

## 📊 Co vidí ostatní na vašem GitHubu

Když někdo přejde na váš repozitář, uvidí:

```
awj-calculator-pro/
├── 📄 README.md              ← Hlavní popis (zobrazí se hned)
├── 📁 backend/               ← Django kód
├── 📁 static/                ← Frontend (CSS, JS)
├── 📁 templates/             ← HTML
├── 📁 docs/                  ← Dokumentace
├── 📄 requirements.txt       ← Závislosti
└── 📄 manage.py              ← Django spouštěč
```

**Neuvidí:**
- ❌ Vaši databázi (`db.sqlite3`)
- ❌ Vaše tajné hesla (`.env`)
- ❌ Váš `venv/` (příliš velký)

---

## 🔄 Budoucí aktualizace

Když něco změníte a chcete nahrát změny:

```bash
cd C:\Users\KEAI\awj-calculator-pro

git add .
git commit -m "Popis změny (např. Přidán nový materiál)"
git push
```

---

## 💡 K čemu je to dobré?

### 1. **Záloha**
- Pokud se vám rozbije počítač, projekt je v bezpečí
- Můžete ho stáhnout odkudkoliv

### 2. **Portfolio**
- Zaměstnavatelé si můžou prohlédnout váš kód
- Ukázka vašich schopností

### 3. **Spolupráce**
- Další lidé můžou přispívat (pull requests)
- Issue tracking pro bugy

### 4. **Verzování**
- Historie všech změn
- Můžete se vrátit ke staré verzi

---

## ❓ Časté otázky

**Q: Mohou ostatní vidět můj kód?**
A: Pokud dáte **Public** = ano. Pokud **Private** = jen vy.

**Q: Bude to fungovat stejně jako na mém počítači?**
A: GitHub jen UKLÁDÁ kód. K běhu potřebujete PythonAnywhere (viz druhý návod).

**Q: Co když udělám chybu?**
A: Git pamatuje historii, můžete se vrátit:
```bash
git log              # Zobrazí historii
git checkout XXXXX   # Vrátí se na verzi XXXXX
```

**Q: Kolik to stojí?**
A: GitHub je **ZDARMA** (pro veřejné i soukromé repozitáře).

---

## ✅ Checklist - GitHub hotovo

- [ ] Vytvořen repozitář na github.com
- [ ] Projekt nahrán (`git push`)
- [ ] Na GitHubu vidím všechny soubory
- [ ] README.md se zobrazuje
- [ ] URL funguje: `https://github.com/VASE-JMENO/awj-calculator-pro`

---

## 🎯 Co dál?

Po nahrání na GitHub:
1. ✅ Kód je zálohovaný
2. ✅ Můžete ho sdílet
3. ➡️ **DALŠÍ KROK:** Nasaďte na PythonAnywhere (viz `PYTHONANYWHERE_JEDNODUCHY_NAVOD.md`)

---

**GitHub = Záloha kódu ✅**
**PythonAnywhere = Běžící aplikace 🌐**

Oba jsou potřeba!
