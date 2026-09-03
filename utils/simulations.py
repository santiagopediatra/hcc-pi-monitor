"""Ayudantes reproducibles para registros ficticios."""
from typing import Any

def siguiente_id(registros: list[dict[str, Any]]) -> str:
    """Genera un identificador local consecutivo sin datos personales."""
    return f"DEMO-{len(registros) + 1:05d}"

