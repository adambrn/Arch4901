from typing import List
from Controller.Interfaces.i_get_model import iGetModel
from Model.Domain.student import Student

class Model(iGetModel):
    def __init__(self, students: List[Student]):
      self.students = students

    def getAllStudents(self) -> List[Student]:
        return self.students