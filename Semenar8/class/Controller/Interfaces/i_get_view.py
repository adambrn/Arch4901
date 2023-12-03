from abc import ABC, abstractmethod
from typing import List
from Controller.Interfaces.i_get_controller import iGetController

from Model.Domain.student import Student

class iGetView(ABC):
    @abstractmethod
    def printAllStudent(self, students: List[Student]):
     pass

    @abstractmethod
    def setController(self, control: iGetController):
        pass