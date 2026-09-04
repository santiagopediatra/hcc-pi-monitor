"""Única fuente de datos de la aplicación demostrativa."""

BASELINE_INSTITUCIONAL = 92.6
ETIQUETA_DATOS_DEMO = "Datos demostrativos para presentación académica"
NOTA_BASELINE = (
    "Baseline de referencia utilizado en esta DEMO. Debe validarse contra la "
    "fuente científica definitiva antes de publicación."
)

PRACTICAS = {
    "LAB_COMP": {"nombre": "Acompañamiento en labor", "corto": "Acompañamiento", "valor": 76.1,
                 "definicion": "Presencia documentada de acompañante durante la labor."},
    "POS_PARTO": {"nombre": "Posición de parto elegida/no supina", "corto": "Posición", "valor": 96.6,
                  "definicion": "Posición elegida o no supina documentada."},
    "EPIS_SEL": {"nombre": "Episiotomía selectiva", "corto": "Episiotomía selectiva", "valor": 89.6,
                 "definicion": "Cumplimiento cuando no se realizó episiotomía rutinaria."},
    "CLAMP_DIF": {"nombre": "Clampaje diferido del cordón", "corto": "Clampaje", "valor": 98.1,
                  "definicion": "≥60 segundos o hasta el cese de pulsación (definición demostrativa)."},
    "SKIN_SKIN": {"nombre": "Contacto piel-piel inmediato", "corto": "Contacto piel-piel", "valor": 92.5,
                  "definicion": "RN sobre la madre dentro de los primeros 5 minutos (definición demostrativa)."},
}

HISTORICO = {
    "Año": [2018, 2019, 2020, 2021, 2022, 2023],
    "Adherencia institucional": [95.0, 96.4, 80.9, 82.3, 96.1, 96.8],
    "Acompañamiento": [74.2, 75.8, 40.5, 42.1, 75.2, 76.1],
    "Posición": [95.1, 96.2, 91.2, 92.5, 96.4, 96.6],
    "Episiotomía selectiva": [89.5, 89.8, 89.1, 89.4, 89.7, 89.6],
    "Clampaje": [97.8, 98.2, 95.2, 96.1, 98.0, 98.1],
    "Contacto piel-piel": [91.2, 92.1, 82.3, 84.2, 92.3, 92.5],
}

FACTORES_ASOCIADOS = {
    "Acompañante": [
        ("Edad <20 años", 5.18, 2.41, 11.10, "<0.001"), ("Edad ≥35", 3.44, 2.11, 5.58, "<0.001"),
        ("Pareja estable", .86, .80, .94, "<0.001"), ("Educación baja", .87, .81, .94, "<0.001"),
        ("Prenatal <4 visitas", .87, .80, .96, "0.004"), ("Hemorragia posparto (HPP)", .82, .74, .91, "<0.001")],
    "Posición": [("Minoría étnica", 2.71, 1.53, 4.83, "<0.001"),
                 ("Psicoprofilaxis", 1.43, 1.15, 1.78, "0.001"), ("Educación baja", .82, .69, .97, "0.025")],
    "Clampaje": [("Educación baja", .74, .59, .93, "0.010"), ("Peso <2500 g", .55, .39, .78, "<0.001"),
                 ("Apgar <7", .10, .07, .14, "<0.001")],
    "Contacto piel-piel": [("Prematurez", .43, .32, .57, "<0.001"), ("Peso bajo", .74, .56, .98, "0.034"),
                           ("Apgar <7", .11, .08, .16, "<0.001"), ("Hemorragia posparto (HPP)", .48, .39, .58, "<0.001")],
}

HOSPITALES_SIMULADOS = {
    "Hospital A": {"Adherencia institucional": 92.6, "Acompañamiento": 76.1, "Posición de parto": 96.6, "Episiotomía selectiva": 89.6, "Clampaje diferido": 98.1, "Contacto piel-piel": 92.5},
    "Hospital B": {"Adherencia institucional": 87.4, "Acompañamiento": 71.2, "Posición de parto": 91.0, "Episiotomía selectiva": 86.8, "Clampaje diferido": 94.6, "Contacto piel-piel": 89.3},
    "Hospital C": {"Adherencia institucional": 81.9, "Acompañamiento": 64.8, "Posición de parto": 87.3, "Episiotomía selectiva": 82.1, "Clampaje diferido": 91.5, "Contacto piel-piel": 84.7},
}

CALIDAD_DATOS = {"Completitud registros": 97.8, "Campos faltantes": 2.2, "Registros auditados": 5.0, "Inconsistencias": 1.4}
RAZONES_SIN_ACOMPANANTE = {"Restricción institucional": 28, "No disponible": 22, "Paciente no lo solicitó": 16,
                           "Paciente lo rechazó": 8, "Motivo clínico": 10, "No documentado": 12, "Otro": 4}
