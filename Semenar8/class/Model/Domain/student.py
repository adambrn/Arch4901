
from Model.Domain.person import Person

class Student(Person):
    def __init__(self, name: str, age: int, id: int):
        super().__init__(name, age)
        self.id = id

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def __str__(self) -> str:
        return f"Student [age={super().get_age()}, name={super().get_name()}, id={self.id}]"