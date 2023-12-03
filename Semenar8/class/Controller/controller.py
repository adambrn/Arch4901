from typing import List
from Controller.Interfaces.i_get_controller import iGetController
from Controller.Interfaces.i_get_model import iGetModel
from Controller.Interfaces.i_get_view import iGetView
from Model.Domain.student import Student


class Controller(iGetController):
    def __init__(self, model: iGetModel, view: iGetView):
        self.model = model
        self.view = view
        self.students = []


    def test(self, studs: List[Student]) -> bool:
        if len(studs) > 0:
            return True
        else:
            return False

    def update(self):
        #MVP
        self.students = self.model.getAllStudents()

        if self.test(self.students):
            self.view.printAllStudent(self.students)
        else:
            print("Модель не доступна!")

        #MVC
        # Логика контроллера
        # self.view.printAllStudent(self.model.getAllStudents())