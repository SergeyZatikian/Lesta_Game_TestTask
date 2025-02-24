from boat import *
from person import *

# Создаем объекты всех классов
boat = Boat()
motor_boat = Motor_Boat(motor_power=150)
big_boat = Big_Boat()
cargo_boat = Cargo_Boat()

# Создаем гребцов
rower1 = RowerBeginner("Иван", 25, 70)
rower2 = RowerExperienced("Петр", 30, 80)
rower3 = RowerPro("Алексей", 35, 90)

# Проверка базового класса Boat
print("=== Тестирование базового класса Boat ===")
try:
    boat.add_rower(rower1)
    boat.add_rower(rower2)
    boat.add_rower(rower3)
    boat.add_weight(500)
    boat.row_forward()
    boat.turn_left()
    boat.drop_anchor()
    print("Статус лодки:", boat.get_all())
    boat.raise_anchor()
    boat.turn_right()
    boat.turn_around()
    boat.delete_weight(200)
    boat.delete_rower(rower3)
    print("Статус лодки после изменений:", boat.get_all())
except ValueError as e:
    print("Ошибка:", e)
print()

# Проверка класса Motor_Boat
print("=== Тестирование класса Motor_Boat ===")
try:
    motor_boat.row_forward()
    motor_boat.turn_left()
    motor_boat.add_weight(300)
    print("Статус лодки с мотором:", motor_boat.get_all())
    motor_boat.stop_motor()
    motor_boat.drop_anchor()
    print("Статус лодки с мотором после остановки:", motor_boat.get_all())
except ValueError as e:
    print("Ошибка:", e)
print()

# Проверка класса Big_Boat
print("=== Тестирование класса Big_Boat ===")
try:
    for _ in range(5):
        big_boat.add_rower(RowerBeginner())
    big_boat.add_weight(800)
    big_boat.row_forward()
    big_boat.turn_right()
    print("Статус большой лодки:", big_boat.get_all())
    big_boat.delete_rower(big_boat.rowers[0])
    big_boat.delete_weight(400)
    print("Статус большой лодки после изменений:", big_boat.get_all())
except ValueError as e:
    print("Ошибка:", e)
print()

# Проверка класса Cargo_Boat
print("=== Тестирование класса Cargo_Boat ===")
try:
    cargo_boat.add_weight(1500)
    cargo_boat.row_forward()
    cargo_boat.turn_left()
    print("Статус грузовой лодки:", cargo_boat.get_all())
    cargo_boat.delete_weight(500)
    cargo_boat.drop_anchor()
    print("Статус грузовой лодки после изменений:", cargo_boat.get_all())
except ValueError as e:
    print("Ошибка:", e)
print()

# Проверка обработки ошибок
print("=== Тестирование обработки ошибок ===")
try:
    boat.add_weight(-100)  # Отрицательный вес
except ValueError as e:
    print("Ошибка:", e)

try:
    boat.delete_weight(1000)  # Удаление большего веса, чем есть
except ValueError as e:
    print("Ошибка:", e)

try:
    for _ in range(5):
        boat.add_rower(RowerBeginner())  # Превышение максимального количества гребцов
except ValueError as e:
    print("Ошибка:", e)

try:
    big_boat.add_weight(3000)  # Превышение максимального веса
except ValueError as e:
    print("Ошибка:", e)
    
    

# Создаем объект лодки
boat = Boat()

# Сценарий 1: Скорость с одним гребцом-новичком
print("=== Сценарий 1: Скорость с одним гребцом-новичком ===")
rower_novice = RowerBeginner("Иван", 25, 70)
boat.add_rower(rower_novice)
boat.row_forward()
print("Скорость лодки:", boat.get_all()["speed"])
print()

# Сценарий 2: Скорость с одним гребцом-профессионалом
print("=== Сценарий 2: Скорость с одним гребцом-профессионалом ===")
boat = Boat()  # Создаем новую лодку
rower_pro = RowerPro("Алексей", 35, 90)
boat.add_rower(rower_pro)
boat.row_forward()
print("Скорость лодки:", boat.get_all()["speed"])
print()

# Сценарий 3: Скорость с несколькими гребцами разного уровня
print("=== Сценарий 3: Скорость с несколькими гребцами разного уровня ===")
boat = Boat()  # Создаем новую лодку
rower_novice = RowerBeginner("Иван", 25, 70)
rower_experienced = RowerExperienced("Петр", 30, 80)
rower_pro = RowerPro("Алексей", 35, 90)
boat.add_rower(rower_novice)
boat.add_rower(rower_experienced)
boat.add_rower(rower_pro)
boat.row_forward()
print("Скорость лодки:", boat.get_all()["speed"])
print()

# Сценарий 4: Скорость с максимальным количеством гребцов
print("=== Сценарий 4: Скорость с максимальным количеством гребцов ===")
boat = Big_Boat()  # Создаем новую лодку
for i in range(8):  # 4 для базовой лодки, 8 для большой лодки
    rower = RowerBeginner(f"Гребец {i}", 25, 70)
    boat.add_rower(rower)
boat.row_forward()
print("Скорость лодки:", boat.get_all()["speed"])
print()


# Сценарий 5: Скорость моторной лодкиы
print("=== Сценарий 4: Скорость с максимальным количеством гребцов ===")
boat = Motor_Boat()  # Создаем новую лодку
for i in range(4):  # 4 для базовой лодки, 8 для большой лодки
    rower = RowerBeginner(f"Гребец {i}", 25, 70)
    boat.add_rower(rower)
boat.row_forward()
print("Скорость лодки:", boat.get_all()["speed"])
print()