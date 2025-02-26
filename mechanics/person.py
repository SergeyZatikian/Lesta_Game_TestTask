class Person:
    
    """Класс Person
    
    В нем описываеться основынем методы класса Person. Можно задать вес, имя и возраст гребцу.
    
    Так же существуют разные типы гребцов, у которых своя эфективность от новичка до профессионала
    """
    
    def __init__(self, name = "NONAME", age = 25, weight = 80):
        self.name = name
        self.age = age
        self.weight = weight
        
        
    def __str__(self):
        return f"{self.name}, {self.age} лет, вес: {self.weight} кг"
    
    
class RowerBeginner(Person):
    def __init__(self, name="NONAME", age=25, weight=80):
        super().__init__(name, age, weight)
        self.rower_efficiency = 1              # Эфективность гребца
        
    def __str__(self):
        return f"Гребец-новичок: {(super().__str__())}"
    
class RowerExperienced(Person):
        def __init__(self, name="NONAME", age=25, weight=80):
            super().__init__(name, age, weight)
            self.rower_efficiency = 2
            
        def __str__(self):
            return f"Гребец-опытный: {(super().__str__())}"
    
class RowerPro(Person):
        def __init__(self, name="NONAME", age=25, weight=80):
            super().__init__(name, age, weight)
            self.rower_efficiency = 3
            
        def __str__(self):
            return f"Гребец-Профессионал: {(super().__str__())}"