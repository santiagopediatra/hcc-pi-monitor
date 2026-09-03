# HCC-PI Monitor

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22285503.svg)](https://doi.org/10.5281/zenodo.22285503)

HCC-PI Monitor es un proyecto académico open source orientado al monitoreo de adherencia institucional documentada a prácticas de parto humanizado. El código se publica para permitir su uso, estudio, modificación y colaboración en investigación bajo la licencia Apache 2.0.

> **Prototipo académico — Datos demostrativos. Actualmente no está destinado a la toma de decisiones clínicas individuales.**

## Objetivo

Convertir cinco procesos documentados en una señal institucional sencilla para vigilancia, comparación temporal e identificación de brechas de implementación. El proyecto busca facilitar la colaboración y futuras investigaciones multicéntricas; no realiza diagnósticos ni recomienda tratamientos.

## Estado actual del proyecto

Esta versión es una demostración académica para congreso. Los valores históricos, comparaciones entre Hospital A, Hospital B y Hospital C, indicadores de calidad y asociaciones mostrados son datos demostrativos o valores de referencia pendientes de verificación contra su fuente científica definitiva. No constituyen resultados de una validación clínica ni evidencia atribuible a instituciones reales.

## Metodología HCC-PI

El índice individual utiliza cinco componentes binarios: acompañamiento en labor (`LAB_COMP`), posición de parto elegida/no supina (`POS_PARTO`), episiotomía selectiva (`EPIS_SEL`), clampaje diferido del cordón (`CLAMP_DIF`) y contacto piel-piel inmediato (`SKIN_SKIN`).

`HCC-PI = número de prácticas cumplidas / 5`

- ALTA: 0.80–1.00.
- MEDIA: 0.60–0.79.
- BAJA: 0.00–0.59.

La adherencia institucional es el porcentaje de partos elegibles con HCC-PI ≥ 0.80 y no debe confundirse con el índice individual. Consulte [la metodología](docs/METODOLOGIA.md) y [el diccionario de datos](docs/DICCIONARIO_DATOS.md).

## Uso de la aplicación

La navegación incluye resumen ejecutivo, tendencias, registro de un parto demostrativo, factores asociados, comparación hospitalaria, calidad de datos y metodología. Los registros se guardan únicamente en `st.session_state` y se eliminan al cerrar la sesión.

## Instalación local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m streamlit run app.py
```

Abra `http://localhost:8501`.

## Aplicación web

La demostración pública está disponible en [hcc-pi-monitor.streamlit.app](https://hcc-pi-monitor.streamlit.app/). Para Streamlit Community Cloud, conecte un fork y seleccione `app.py` como archivo principal.

## Investigación

El repositorio está abierto a propuestas de análisis, validaciones externas y futuros protocolos multicéntricos. Cada estudio debe definir su protocolo, gobernanza, aprobación ética, fuente de datos y plan estadístico. Las funcionalidades futuras y las hipótesis no deben presentarse como resultados obtenidos.

## Scope and data availability

HCC-PI Monitor is open-source academic research software for institutional monitoring and visualization of documented adherence to selected humanized childbirth care practices.

No individual-level clinical research dataset is included or distributed with this repository.

The research supporting development and evaluation of HCC-PI received prior approval from the Comité de Ética para la Investigación en Seres Humanos del Hospital General Docente de Calderón (CEISH-HGDC-2024-007; August 18, 2024).

This software is not intended for individual clinical decision-making. Further external and prospective validation is required.

See [`docs/ETHICS.md`](docs/ETHICS.md) for the scope of this statement.

## Limitaciones

HCC-PI Monitor mide adherencia documentada a procesos. No mide consentimiento informado real, dignidad o privacidad percibidas, comunicación clínica, satisfacción materna ni calidad vivida de la atención. No sustituye evaluación clínica, auditoría ni encuesta postparto. Consulte [las limitaciones completas](docs/LIMITACIONES.md).

## Seguridad y privacidad

La demostración no solicita nombre, cédula, teléfono, correo electrónico, dirección ni número de historia clínica. **No introducir información identificable de pacientes en la demostración pública.** El proyecto no usa base de datos externa ni secretos para su funcionamiento actual.

## Citation

If you use HCC-PI Monitor in research, please cite:

Vasco-Morales, Santiago, & Toapanta-Pinta, Paola. (2026).  
*HCC-PI Monitor (v1.0.0)* [Computer software].  
Zenodo.  
[https://doi.org/10.5281/zenodo.22285504](https://doi.org/10.5281/zenodo.22285504)

Concept DOI for all versions:  
[https://doi.org/10.5281/zenodo.22285503](https://doi.org/10.5281/zenodo.22285503)

Machine-readable citation metadata are available in [`CITATION.cff`](CITATION.cff).

## Cómo contribuir

Consulte [`CONTRIBUTING.md`](CONTRIBUTING.md). Los cambios metodológicos deben justificarse científicamente y quedar documentados.

## Licencia

El software se distribuye bajo la [Apache License 2.0](LICENSE). El aviso de autoría está en [`NOTICE`](NOTICE). La licencia permite usar, estudiar, modificar y redistribuir el código bajo sus condiciones.

## Autores

- Santiago Vasco-Morales
- Paola Toapanta-Pinta

Copyright 2026.
