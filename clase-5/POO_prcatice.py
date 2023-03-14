from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, last_name, dni, email):
        self.name = name
        self.last_name = last_name
        self.dni = dni
        self.email = email
    def __str__(self) -> str:
        return super().__str__()
    @abstractmethod
    def signin(self):
        pass
        
class Student(Person):
    def __init__(self, name, last_name, dni, email, matricula, baja):
        super().__init__(name, last_name, dni, email)
        self.matricula = matricula
        self.baja = baja
        
    def signin(self):
        print("Sign in succesfully")
        
class Professor(Person):
    def __init__(self, name, last_name, dni, email, matricula, baja):
        super().__init__(name, last_name, dni, email)
        self.matricula = matricula
        self.baja = baja
        
    def signin(self):
        print("Sign in professor is succesfully")
        
        
new_student = Student("Lucas", "Rodriguez", 12312313, "lucas@gmail.com", 1234, True )
new_student.signin()

new_pro