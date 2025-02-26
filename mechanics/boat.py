from mechanics.person import *

class Boat:
    def __init__(self): 
        self.speed = 0              # скорость лодки
        self.direction = 0          # направление ложки
        self.rowers = []            # список гребцов
        self.rowers_weight = 0      # вес всех гребцов
        self.weight = 0             # вес лодки
        self.anchor = False         # якорь опущен или нет
        
        self.max_weight = 1000      # Максимальный вес 
        self.max_rowers = 4         # Максимальное количесвто гребцов
    
    def add_rower(self, rower):
        
        if len(self.rowers) + 1 > self.max_rowers:
            raise ValueError(f"Превышено максимально количесвто гребцов {self.max_rowers}")
        if not isinstance(rower, Person):
            raise ValueError("Гребец должен быть обьектом класса Person")
        if self.weight + rower.weight > self.max_weight:
            raise ValueError("Вес превышает максималный вес лодки")
        self.rowers.append(rower)
        self.rowers_weight += rower.weight
        self.weight += rower.weight
            
    def delete_rower(self, rower):
        if not isinstance(rower, Person):
            raise ValueError("Гребец должен быть обьектом класса Person")
        if rower in self.rowers:
            self.rowers.remove(rower)
            self.weight -= rower.weight
            self.rowers_weight -= rower.weight
        else:
            raise ValueError("Гребец не найден")
        
    def add_weight(self, weight):
        if not isinstance(weight, int):
            raise ValueError("Вес груза должен быть целым числом")
        if weight <= 0:
            raise ValueError("Вес груза должен быть положительнеым")
        if self.weight + weight > self.max_weight:
            raise ValueError("Превышен максимальный вес")
        self.weight += weight

    def delete_weight(self, weight):
        if not isinstance(weight, int):
            raise ValueError("Вес груза должен быть целым числом")
        if weight <= 0:
            raise ValueError("Вес груза должен быть положительнеым")
        if  weight > self.weight - self.rowers_weight:
            raise ValueError("Недостаточно груза на лодке")
        self.weight -= weight
        
    def drop_anchor(self):
        self.anchor = True
        self.speed = 0
        
    def raise_anchor(self):
        self.anchor = False
    
    def row_forward(self):
        if self.anchor: self.speed = 0
        else:
            base_speed = 10
            speed_reduction = self.weight/100
            total_efficiency = sum(rower.rower_efficiency for rower in self.rowers)
            self.speed = max(base_speed*total_efficiency - speed_reduction, 0)
    
    def turn_left(self):
        if not self.anchor: 
            self.direction -= 90
            self._normalize_direction()
    
    def turn_right(self):
        if not self.anchor: 
            self.direction += 90
            self._normalize_direction()
   
    def turn_around(self):
        if not self.anchor: 
            self.direction += 180
            self._normalize_direction()
            
    def _normalize_direction(self):
        self.direction = self.direction % 360
        if self.direction > 180: self.direction -= 360        


    def get_all(self):
        return {
            "speed": self.speed,
            "direction": self.direction,
            "rowers": [str(rower) for rower in self.rowers],
            "weight": self.weight,
            "rowers_weight": self.rowers_weight,
            "anchor": self.anchor
        }
        
        
        
class Motor_Boat(Boat):
    def __init__(self, motor_power = 100):
        super().__init__()
        self.motor_power = motor_power
    
    def row_forward(self):
        if self.anchor: self.speed = 0
        else:
            base_speed = 10
            speed_reduction = self.weight/100
            total_efficiency = sum(rower.rower_efficiency for rower in self.rowers)
            self.speed = max((base_speed*total_efficiency - speed_reduction) + self.motor_power, 0)
    
            
    def stop_motor(self):
        self.speed = 0
        
    def get_all(self):
        status = super().get_all()
        status["motor_power"] = self.motor_power
        return(status)
    
class Big_Boat(Boat):
    def __init__(self):
        super().__init__()
        self.max_rowers = 8
        self.max_weight = 2000
            
    def get_all(self):
        status = super().get_all()
        status["max_rowers"] = self.max_rowers
        return(status)
    
class Cargo_Boat(Boat):
    def __init__(self):
        super().__init__()
        self.max_weight = 2000
            
            
    
