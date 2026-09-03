"""Lógica de dominio del índice HCC-PI."""
from collections.abc import Mapping, Sequence
from typing import Any

CODIGOS = ("LAB_COMP", "POS_PARTO", "EPIS_SEL", "CLAMP_DIF", "SKIN_SKIN")

def calcular_hccpi(practicas: Mapping[str, bool | int]) -> tuple[float, int]:
    """Retorna el índice individual y el número de prácticas cumplidas."""
    validar_registro(practicas)
    score = sum(bool(practicas[codigo]) for codigo in CODIGOS)
    return score / len(CODIGOS), score

def clasificar_hccpi(indice: float) -> str:
    """Clasifica un índice válido como ALTA, MEDIA o BAJA."""
    if not 0 <= indice <= 1:
        raise ValueError("El HCC-PI debe estar entre 0 y 1.")
    return "ALTA" if indice >= .80 else "MEDIA" if indice >= .60 else "BAJA"

def calcular_adherencia_institucional(indices: Sequence[float]) -> float:
    """Calcula el porcentaje de partos elegibles con HCC-PI >= 0.80."""
    if not indices:
        return 0.0
    if any(not 0 <= valor <= 1 for valor in indices):
        raise ValueError("Todos los índices deben estar entre 0 y 1.")
    return 100 * sum(valor >= .80 for valor in indices) / len(indices)

def evaluar_alertas(adherencia_actual: float, adherencia_anterior: float | None = None,
                    acompanamiento: float | None = None) -> list[str]:
    """Evalúa reglas demostrativas de alerta expresadas en porcentajes."""
    alertas: list[str] = []
    if adherencia_actual < 85:
        alertas.append("Adherencia actual inferior a 85%.")
    if adherencia_anterior is not None and adherencia_anterior - adherencia_actual > 10:
        alertas.append("Descenso superior a 10 puntos porcentuales respecto al periodo anterior.")
    if acompanamiento is not None and acompanamiento < 70:
        alertas.append("Alerta prioritaria: acompañamiento inferior a 70%.")
    return alertas

def validar_registro(registro: Mapping[str, Any]) -> None:
    """Verifica presencia y naturaleza binaria de los cinco componentes."""
    faltantes = [codigo for codigo in CODIGOS if codigo not in registro]
    if faltantes:
        raise ValueError(f"Faltan prácticas: {', '.join(faltantes)}")
    invalidos = [c for c in CODIGOS if registro[c] not in (True, False, 0, 1)]
    if invalidos:
        raise ValueError(f"Valores no binarios: {', '.join(invalidos)}")

