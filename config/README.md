# Configuration Files

## 📁 Účel
Konfigurační soubory pro různá prostředí

## 📋 Doporučené soubory:
- `development.json` - Nastavení pro vývoj
- `production.json` - Nastavení pro produkci
- `testing.json` - Nastavení pro testy
- `constants.json` - Konstanty aplikace

## 📝 Příklad development.json:
```json
{
  "debug": true,
  "api_url": "http://localhost:8000/api",
  "enable_logging": true,
  "cache_timeout": 0
}
```

## 📝 Příklad constants.json:
```json
{
  "MAX_PRESSURE": 600,
  "MIN_PRESSURE": 100,
  "DEFAULT_MESH_SIZE": 80,
  "WATER_DENSITY": 1000
}
```

## 💡 Použití:
Tyto soubory jsou **volitelné** - zatím se používá `.env` soubor pro konfiguraci.
