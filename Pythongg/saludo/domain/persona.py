from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str

    def saludo(self) -> str:
        return f"Hola {self.nombre}"