# Metodología HCC-PI

Este documento describe exclusivamente la lógica implementada actualmente. No constituye una guía clínica ni una validación científica.

## Índice individual

Cada registro contiene cinco componentes binarios. Un valor `1` representa cumplimiento documentado y `0`, no cumplimiento documentado.

| Código | Práctica | Definición implementada |
|---|---|---|
| `LAB_COMP` | Acompañamiento en labor | Presencia documentada de acompañante durante la labor. |
| `POS_PARTO` | Posición de parto elegida/no supina | Posición elegida o no supina documentada. |
| `EPIS_SEL` | Episiotomía selectiva | Cumplimiento cuando no se realizó episiotomía rutinaria. |
| `CLAMP_DIF` | Clampaje diferido del cordón | 60 segundos o más, o hasta el cese de pulsación; definición demostrativa. |
| `SKIN_SKIN` | Contacto piel-piel inmediato | Recién nacido sobre la madre dentro de los primeros cinco minutos; definición demostrativa. |

`HCC-PI = suma de prácticas cumplidas / 5`

La aplicación muestra también el recuento de prácticas cumplidas.

## Clasificación

- ALTA: HCC-PI ≥ 0.80.
- MEDIA: HCC-PI ≥ 0.60 y < 0.80.
- BAJA: HCC-PI < 0.60.

## Adherencia institucional

`Adherencia institucional = partos con HCC-PI ≥ 0.80 / total de partos elegibles × 100`

Es una métrica agregada distinta del índice individual.

## Alertas demostrativas

La lógica genera alertas cuando la adherencia actual es inferior a 85%, cuando desciende más de 10 puntos porcentuales respecto al periodo anterior o cuando el acompañamiento es inferior a 70%. Recomienda revisión por el equipo institucional de Calidad; no genera recomendaciones clínicas.

## Naturaleza de la información

- **Datos demostrativos:** histórico, baseline, comparaciones hospitalarias y calidad de datos.
- **Valores de referencia:** factores asociados incluidos para demostración, pendientes de verificación contra la publicación científica.
- **Resultados de investigación:** el proyecto no declara resultados propios ni validación clínica.
- **Hipótesis y funcionalidades futuras:** no están implementadas ni deben inferirse de los paneles.

