# 📤 GITHUB UPLOAD - Tato složka

## 🎯 Účel
Tato složka obsahuje **VŠECHNY SOUBORY** pro nahrání na GitHub.

## ✅ CO JE V TÉTO SLOŽCE

```
github-upload/
├── backend/                    # Django backend
├── static/                     # Frontend (CSS, JS)
├── templates/                  # HTML šablony
├── docs/                       # Dokumentace
├── frontend/                   # Připravené složky (s README)
├── config/                     # Konfigurace
├── tests/                      # Testy
├── manage.py                   # Django spouštěč
├── requirements.txt            # Python závislosti
├── .gitignore                  # Git konfigurace
├── .env.example                # Vzor .env souboru
└── *.md                        # Veškerá dokumentace
```

## 🚀 JAK NAHRÁT NA GITHUB

### Krok 1: Vytvořte repozitář na GitHub
1. Jděte na: https://github.com
2. Klikněte **+ → New repository**
3. Název: `awj-calculator-pro`
4. Klikněte **Create repository**
5. Zkopírujte URL (např. `https://github.com/vase-jmeno/awj-calculator-pro.git`)

### Krok 2: Otevřete Command Prompt zde
1. Otevřete tuto složku v Průzkumníku: `C:\Users\KEAI\awj-calculator-pro\github-upload`
2. Do adresního řádku napište `cmd` a stiskněte Enter

### Krok 3: Nahrajte
```bash
# Inicializujte Git
git init

# Přidejte všechny soubory
git add .

# Vytvořte commit
git commit -m "AWJ Calculator Pro - Initial commit"

# Propojte s GitHub (ZMĚŇTE URL na vaši!)
git remote add origin https://github.com/VASE-JMENO/awj-calculator-pro.git

# Nahrajte
git branch -M main
git push -u origin main
```

### Krok 4: Ověření
Jděte na `https://github.com/VASE-JMENO/awj-calculator-pro`

✅ Měli byste vidět všechny složky a soubory

## 📊 Co se nahraje
- **~100 souborů**
- **~5 MB**
- **Celý projekt včetně dokumentace**

## ❓ Co NENÍ v této složce
- ❌ `venv/` - příliš velké, každý si vytvoří vlastní
- ❌ `db.sqlite3` - lokální databáze, každý má vlastní
- ❌ `.env` - tajné údaje, každý má vlastní
- ❌ `__pycache__/` - generované soubory

(Tyto jsou automaticky ignorovány díky `.gitignore`)

## 💡 Tip
Tuto složku můžete přímo přejmenovat na `awj-calculator-pro` a nahrát celou na GitHub!

---

**GitHub = Záloha celého projektu** 📦
