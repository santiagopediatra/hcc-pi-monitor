# HCC-PI Monitor

Sistema demostrativo para monitorizar adherencia institucional documentada a cinco prácticas de parto humanizado. No mide directamente la experiencia materna, la dignidad, la satisfacción ni el consentimiento real.

**DEMO ACADÉMICA — Datos demostrativos.** Esta propuesta no pertenece oficialmente a ninguna institución. Hospital A, Hospital B y Hospital C son nombres genéricos y sus datos son simulados para la presentación.

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Abra `http://localhost:8501`.

## Despliegue en Streamlit Community Cloud

1. Publique el contenido de esta carpeta en un repositorio de GitHub. `app.py` debe permanecer en la raíz.
2. Ingrese a [Streamlit Community Cloud](https://share.streamlit.io/) y conecte su cuenta de GitHub.
3. Seleccione el repositorio y la rama que desea desplegar.
4. Indique `app.py` como archivo principal y pulse **Deploy**.

La plataforma instalará automáticamente las dependencias declaradas en `requirements.txt`. Esta aplicación no utiliza secretos, servicios externos ni una base de datos.

## Uso responsable

Esta aplicación es un prototipo de investigación y no está validada para uso clínico.
Los datos de Hospital A, Hospital B y Hospital C son demostrativos y no representan instituciones reales. **No utilizar para decisiones clínicas.**
