# Diccionario de datos

Este diccionario refleja el formulario demostrativo y la lógica actual. No define una base clínica validada.

## Componentes HCC-PI

| Variable | Tipo | Valores | Descripción |
|---|---|---|---|
| `LAB_COMP` | Binaria | 0/1 | Acompañamiento en labor documentado. |
| `POS_PARTO` | Binaria | 0/1 | Posición elegida/no supina documentada. |
| `EPIS_SEL` | Binaria | 0/1 | Ausencia de episiotomía rutinaria documentada. |
| `CLAMP_DIF` | Binaria | 0/1 | Clampaje diferido según definición demostrativa. |
| `SKIN_SKIN` | Binaria | 0/1 | Contacto piel-piel según definición demostrativa. |
| `indice` | Numérica | 0.00–1.00 | Suma de componentes dividida para cinco. |
| `score` | Entera | 0–5 | Número de prácticas cumplidas. |

## Variables categóricas del formulario

| Campo interno | Categorías disponibles |
|---|---|
| `edad_materna` | `<20`, `20–34`, `>=35` |
| `educacion` | `Primaria o menos`, `Secundaria o superior` |
| `prenatales` | `0`, `1–4`, `>=5` |
| `gestacional` | `<37`, `37–41`, `>=42` |
| `peso` | `<2500 g`, `2500–3999 g`, `>=4000 g` |
| `apgar` | `<7`, `>=7` |
| `hpp` (hemorragia posparto) | `No`, `Sí` |

## Identificador demostrativo

`id` adopta el formato local `DEMO-00001`. Es generado automáticamente, no corresponde a una historia clínica y se conserva solo durante la sesión.

## Privacidad y datos agregados

El formulario no contempla identificadores personales. Los históricos, hospitales A/B/C, indicadores de calidad, razones de ausencia de acompañante y factores asociados son demostrativos o de referencia. No representan una validación clínica ni resultados atribuibles a instituciones reales.
