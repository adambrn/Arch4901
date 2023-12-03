from typing import List
from Controller.Interfaces.i_get_controller import iGetController
from Controller.Interfaces.i_get_model import iGetModel
from Controller.Interfaces.i_get_view import iGetView
from Controller.controller import Controller
from Model.Domain.student import Student
from Model.model import Model
from View.view import View


def main():
    students: List[Student] = []
    s1 = Student("Сергей", 21, 101)
    s2 = Student("Андрей", 22, 111)
    s3 = Student("Иван", 22, 121)
    s4 = Student("Игорь", 23, 301)
    s5 = Student("Даша", 25, 171)
    s6 = Student("Лена", 23, 104)
    students.append(s1)
    students.append(s2)
    students.append(s3)
    students.append(s4)
    students.append(s5)
    students.append(s6)


    mod: iGetModel = Model(students)
    view: iGetView = View()

    control: iGetController = Controller(mod, view)

    view.setController(control)

    view.callModel()

   # control.update()
    
if __name__ == '__main__':
    main()

