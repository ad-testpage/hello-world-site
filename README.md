# Hello World Website

Preprosta HTML stran z DevOps CI/CD procesom.

## Tehnologije
- HTML
- CSS
- GitHub Pages
- GitHub Actions

## Struktura repozitorija

- `index.html` – glavna HTML stran - struktura strani
- `style.css` - izgled atrani (barve, pisave, razmiki, poravnave)
- `images` - datoteka s slikami  
- `smoke-check.py` – preprosti python smoke test za preverjanje strani
- `.github/workflows/smoke-test.yml` – workflow, ki naredi smoke test

## Deployment
Push na `master` branch → avtomatska objava
