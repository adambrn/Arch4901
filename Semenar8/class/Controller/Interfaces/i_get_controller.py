from abc import ABC, abstractmethod

class iGetController(ABC):
    @abstractmethod
    def update(self):
        pass