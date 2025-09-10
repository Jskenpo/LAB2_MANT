# TextLib — CI Lab (Continuous Integration)

Pequeña librería de **manipulación de texto** (Opción B del laboratorio) con pruebas unitarias y **GitHub Actions** para ejecutar `pytest` en cada Pull Request a `main`.

## Funciones
Implementadas en `textlib/__init__.py`:

- `reverse(s)` — retorna `s` en orden inverso.
- `count_vowels(s)` — cuenta vocales `a,e,i,o,u` (minúsculas/mayúsculas). No cuenta acentos por defecto.
- `is_palindrome(s)` — evalúa si `s` es palíndromo **ignorando mayúsculas, espacios y signos de puntuación simples**.
- `to_upper(s)` — convierte `s` a mayúsculas.
- `concat(a, b)` — concatena `a` y `b`.

**Contratos y manejo de errores:**
- Todas las funciones requieren `str`. Si el argumento no es `str`, lanzan `TypeError` con un mensaje claro.
- `concat(a, b)` valida que **ambos** sean `str`.

## Cómo correr localmente
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Git: flujo mínimo sugerido
```bash
git init
git add .
git commit -m "feat: textlib with tests and CI"
git branch -M main
git remote add origin <TU_REPO_GITHUB_URL>
git push -u origin main
```

### Probar el CI con Pull Requests
1. Crea una rama: `git checkout -b feat/demo`
2. Cambia algo mínimo (p. ej., rompe una prueba: en `textlib/__init__.py` cambia el retorno de `to_upper` a `return s`).
3. `git commit -am "chore: break test on purpose"` y `git push -u origin feat/demo`
4. Abre un Pull Request hacia `main`. GitHub Actions correrá `pytest` y **debería fallar** con ese cambio.
5. Reviértelo y confirma que al corregir el código, las pruebas pasan.

## Protección de rama (opcional pero recomendado)
En GitHub: *Settings → Branches → Branch protection rules* → New rule
- Branch name pattern: `main`
- Habilitar **"Require status checks to pass before merging"** y seleccionar el workflow `ci`.
- Habilitar **"Require a pull request before merging"**.

---
Laboratorio basado en la guía de **Continuous Integration** (UVG). Ver PDF original para requisitos exactos.