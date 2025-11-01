# 📤 Návod: Jak nahrát projekt na GitHub

## Krok 1️⃣: Příprava (jen poprvé)

### A) Nainstalujte Git (pokud ještě nemáte)
1. Stáhněte Git: https://git-scm.com/download/win
2. Spusťte instalátor
3. Klikejte "Next" (výchozí nastavení je OK)

### B) Ověřte instalaci
Otevřete Command Prompt (cmd) a zadejte:
```bash
git --version
```
Mělo by vypsat verzi (např. `git version 2.42.0`)

### C) Nastavte své jméno a email (jen JEDNOU)
```bash
git config --global user.name "Vaše Jméno"
git config --global user.email "vas.email@example.com"
```

## Krok 2️⃣: Vytvořte repozitář na GitHub

### A) Přihlaste se na GitHub
1. Jděte na: https://github.com
2. Přihlaste se (nebo vytvořte účet)

### B) Vytvořte nový repozitář
1. Klikněte na **+** (vpravo nahoře) → **New repository**
2. Vyplňte:
   - **Repository name:** `awj-calculator-pro`
   - **Description:** `Advanced AWJ Calculator with AI optimization`
   - **Visibility:** Public nebo Private (jak chcete)
   - ❌ **NEZAŠKRTÁVEJTE:** "Add a README file" (už ho máte!)
   - ❌ **NEZAŠKRTÁVEJTE:** "Add .gitignore" (už ho máte!)
3. Klikněte **Create repository**

### C) Zkopírujte URL repozitáře
GitHub vám ukáže URL, vypadá nějak takto:
```
https://github.com/VASE-JMENO/awj-calculator-pro.git
```
**Poznamenejte si tuto URL!**

## Krok 3️⃣: Nahrajte projekt na GitHub

### A) Otevřete Command Prompt v projektu
1. Otevřete Průzkumník Windows
2. Přejděte do: `C:\Users\KEAI\awj-calculator-pro`
3. Do adresního řádku napište `cmd` a stiskněte Enter

### B) Inicializujte Git repozitář
```bash
git init
```
✅ Mělo by vypsat: `Initialized empty Git repository...`

### C) Přidejte všechny soubory
```bash
git add .
```
*(Tečka na konci je důležitá!)*

### D) Vytvořte první commit
```bash
git commit -m "Initial commit: AWJ Calculator Pro v1.0 - Production ready"
```
✅ Mělo by vypsat statistiky (např. `30 files changed, 5000+ insertions`)

### E) Propojte s GitHub repozitářem
```bash
git remote add origin https://github.com/VASE-JMENO/awj-calculator-pro.git
```
⚠️ **DŮLEŽITÉ:** Nahraďte `VASE-JMENO` vaším skutečným GitHub username!

### F) Ověřte propojení
```bash
git remote -v
```
✅ Mělo by vypsat dvakrát vaši URL (fetch a push)

### G) Nahrajte na GitHub
```bash
git branch -M main
git push -u origin main
```

⚠️ **První nahrání:** GitHub vás může požádat o přihlášení:
- **Username:** Vaše GitHub username
- **Password:** ❌ NEPOUŽÍVEJTE heslo! Použijte **Personal Access Token**

### H) Jak vytvořit Personal Access Token (pokud ho potřebujete)
1. Jděte na GitHub → **Settings** (vpravo nahoře, ikona profilu)
2. **Developer settings** (vlevo dole)
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token** → **Generate new token (classic)**
5. **Note:** `AWJ Calculator Upload`
6. **Expiration:** 90 days (nebo jak chcete)
7. **Select scopes:** ✅ Zaškrtněte **repo** (celý)
8. **Generate token**
9. **ZKOPÍRUJTE TOKEN!** (ukáže se jen jednou)
10. Použijte ho jako heslo při `git push`

## Krok 4️⃣: Ověření

### A) Zkontrolujte na GitHubu
1. Jděte na: `https://github.com/VASE-JMENO/awj-calculator-pro`
2. Měli byste vidět všechny soubory ✅
3. README.md by se měl zobrazit na hlavní stránce ✅

### B) Ověřte soubory
Zkontrolujte, že jsou tam tyto klíčové soubory:
- ✅ README.md
- ✅ requirements.txt
- ✅ manage.py
- ✅ backend/
- ✅ static/
- ✅ templates/

## 🎉 Hotovo! Projekt je na GitHubu!

---

## 📝 Budoucí aktualizace projektu

Když něco změníte v projektu a chcete nahrát změny:

```bash
# 1. Přidejte změněné soubory
git add .

# 2. Vytvořte commit s popisem změn
git commit -m "Popis toho, co jste změnili"

# 3. Nahrajte na GitHub
git push
```

### Příklad:
```bash
git add .
git commit -m "Added new material: Copper"
git push
```

---

## ❓ Časté problémy a řešení

### ❌ Problem: `git: command not found`
**Řešení:** Git není nainstalovaný nebo není v PATH
- Nainstalujte Git z https://git-scm.com
- Restartujte Command Prompt

### ❌ Problem: `fatal: remote origin already exists`
**Řešení:** Remote už existuje
```bash
git remote remove origin
git remote add origin https://github.com/VASE-JMENO/awj-calculator-pro.git
```

### ❌ Problem: `Updates were rejected because the remote contains work...`
**Řešení:** Na GitHubu je něco, co nemáte lokálně
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### ❌ Problem: `Authentication failed`
**Řešení:** Použijte Personal Access Token místo hesla
- Vytvořte token podle Kroku 3H výše
- Použijte token jako heslo

---

## 💡 Tipy

### 1. Kontrola stavu před commitováním
```bash
git status
```
Ukáže, které soubory budou commitovány

### 2. Zobrazení historie commitů
```bash
git log --oneline
```

### 3. Zobrazení změn před commitováním
```bash
git diff
```

### 4. Ignorování souborů
Soubor `.gitignore` už je vytvořený a ignoruje:
- `__pycache__/`
- `*.pyc`
- `db.sqlite3`
- `.env`
- `venv/`

---

## 🔗 Užitečné odkazy

- **GitHub dokumentace:** https://docs.github.com
- **Git cheat sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **Git tutorial:** https://www.youtube.com/results?search_query=git+github+tutorial+czech

---

**Váš projekt je nyní bezpečně zálohovaný na GitHubu!** 🎊
