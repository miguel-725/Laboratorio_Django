from abc import ABC, abstractmethod

class SaludarUseCase(ABC):
    @abstractmethod
    def ejecutar(self, nombre: str) -> str:
        pass