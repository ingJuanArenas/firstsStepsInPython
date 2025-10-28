

from dataclasses import dataclass, field


@dataclass
class Person:
    name:str
    idP:int
    age:int
    profession:str

    def __post_init__(self):
        if self.age < 0:
            print("Edad invalida")
        elif self.age>120:
            print("Edad invalida")


@dataclass
class Student(Person):
    def __post_init__(self):
        super().__post_init__()
        if self.age < 18:
            print("Edad invalida para estudiantes")
        elif self.age > 25:
            print("Edad invalida para estudiantes")


@dataclass
class Teacher(Person):
    def __post_init__(self):
        super().__post_init__()
        if self.age < 30:
            print("Edad invalida para profesores")
        elif self.age > 40:
            print("Edad invalida para profesores")


# now, create difrent varibales using all these classes 

# def run():
#     person1 = Person("John Doe", 30, 35, "Software Engineer")
#     student1 = Student("Jane Smith", 18, 19, "Computer Science")
#     teacher1 = Teacher("Mike Johnson", 35, 40, "Mathematics")
#     print(person1.name)
#     print(student1.profession)
#     print(teacher1.idP)




#Now make another difrent classes using the difrent tools that @dataclass offers to us all in one tab not step by step
@dataclass
class Car:
    make:str
    model:str
    year:int
    color:str
    price: int = field(default=3000)

    def __post_init__(self):
        if self.year < 1900:
            print("Año invalido")
        elif self.year > 2023:
            print("Año invalido")



@dataclass(frozen=True)
class Motorbike:
    model:str
    serial:str
    year: int
    max_speed: int = field(default= 180)



## now create cars and print 
def run():
    car1 = Car("Toyota", "Corolla", 2020, "Rojo", 3500)
    car2 = Car("Honda", "Civic", 2019, "Azul", 3200)
    ## create a motorbike instance an try to modify one of its values
    motorbike1 = Motorbike("Yamaha", "YZF-R1", 2021, 220)
    print(str(motorbike1))
    print(car1.make)
    print(car2.model)
    print(car1.year)
    print(car2.color)
    print(car1.price)


    
if __name__ == "__main__":
    run()

