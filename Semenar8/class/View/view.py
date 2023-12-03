from typing import List
from Controller.Interfaces.i_get_controller import iGetController
from Controller.Interfaces.i_get_view import iGetView
from Model.Domain.student import Student


class View(iGetView):
    def __init__(self):
     self.control = None


    def setController(self, control: iGetController):
        self.control = control

    def callModel(self):
        self.control.update()

    def printAllStudent(self, students: List[Student]):
        print("----------- Список студентов ----------")
        for s in students:
            print(s)