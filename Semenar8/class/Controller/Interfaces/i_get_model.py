from abc import ABC, abstractmethod

class iGetModel(ABC):
    @abstractmethod
    def getAllStudents(self):
      pass