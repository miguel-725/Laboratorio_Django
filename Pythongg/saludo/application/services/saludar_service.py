from saludo.application.ports.saludar_use_case import SaludarUseCase
from saludo.domain.persona import Persona

class SaludarService(SaludarUseCase):
    def ejecutar(self, nombre: str) -> str:
        nombre = (nombre or "").strip()
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        persona = Persona(nombre=nombre)
        return persona.saludo()