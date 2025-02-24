import pytest
from person import *
from boat import *

# Функциональные тесты

def test_add_beginner_rower():
    boat = Boat()
    rower = RowerBeginner()
    boat.add_rower(rower)
    assert len(boat.rowers) == 1
    assert boat.weight == rower.weight

def test_add_pro_rower():
    boat = Boat()
    rower = RowerPro()
    boat.add_rower(rower)
    assert len(boat.rowers) == 1
    assert boat.weight == rower.weight

def test_delete_rower():
    boat = Boat()
    rower = RowerBeginner()
    boat.add_rower(rower)
    boat.delete_rower(rower)
    assert len(boat.rowers) == 0
    assert boat.weight == 0

def test_add_weight():
    boat = Boat()
    boat.add_weight(100)
    assert boat.weight == 100

def test_delete_weight():
    boat = Boat()
    boat.add_weight(100)
    boat.delete_weight(100)
    assert boat.weight == 0

def test_row_forward():
    boat = Boat()
    rower = RowerBeginner()
    boat.add_rower(rower)
    boat.row_forward()
    assert boat.speed > 0

def test_turn_left():
    boat = Boat()
    boat.turn_left()
    assert boat.direction == -90

def test_turn_right():
    boat = Boat()
    boat.turn_right()
    assert boat.direction == 90

def test_turn_around():
    boat = Boat()
    boat.turn_around()
    assert boat.direction == 180

def test_drop_anchor():
    boat = Boat()
    boat.row_forward()
    boat.drop_anchor()
    assert boat.speed == 0
    assert boat.anchor == True

def test_raise_anchor():
    boat = Boat()
    boat.drop_anchor()
    boat.raise_anchor()
    assert boat.anchor == False

def test_max_weight_exceeded():
    boat = Boat()
    with pytest.raises(ValueError):
        boat.add_weight(1001)

def test_max_rowers_exceeded():
    boat = Boat()
    for _ in range(4):
        boat.add_rower(RowerBeginner())
    with pytest.raises(ValueError):
        boat.add_rower(RowerBeginner())

def test_delete_nonexistent_rower():
    boat = Boat()
    rower = RowerBeginner()
    with pytest.raises(ValueError):
        boat.delete_rower(rower)

def test_delete_nonexistent_weight():
    boat = Boat()
    with pytest.raises(ValueError):
        boat.delete_weight(100)

def test_initial_state():
    boat = Boat()
    assert boat.speed == 0
    assert boat.direction == 0
    assert len(boat.rowers) == 0
    assert boat.weight == 0
    assert boat.anchor == False

def test_get_status():
    boat = Boat()
    rower = RowerBeginner()
    boat.add_rower(rower)
    status = boat.get_all()
    assert status["speed"] == 0
    assert status["direction"] == 0
    assert len(status["rowers"]) == 1
    assert status["weight"] == rower.weight
    assert status["anchor"] == False

def test_rower_efficiency():
    boat = Boat()
    rower1 = RowerBeginner()
    rower2 = RowerPro()
    boat.add_rower(rower1)
    boat.add_rower(rower2)
    boat.row_forward()
    assert boat.speed > 0

# Интеграционные тесты

def test_rowers_influence_on_speed():
    boat = Boat()
    rower1 = RowerBeginner()
    rower2 = RowerPro()
    boat.add_rower(rower1)
    boat.add_rower(rower2)
    boat.row_forward()
    assert boat.speed > 0

def test_weight_influence_on_speed():
    boat = Boat()
    rower = RowerBeginner()
    boat.add_rower(rower)
    boat.add_weight(500)
    boat.row_forward()
    assert boat.speed > 0

def test_anchor_stops_boat():
    boat = Boat()
    rower = RowerBeginner()
    boat.add_rower(rower)
    boat.row_forward()
    boat.drop_anchor()
    assert boat.speed == 0
    
def test_max_speed_different_boats():
    # Обычная лодка
    boat = Boat()
    for _ in range(boat.max_rowers):
        boat.add_rower(RowerPro())
    boat.row_forward()
    speed_normal_boat = boat.speed

    # Моторная лодка
    motor_boat = Motor_Boat()
    for _ in range(motor_boat.max_rowers):
        motor_boat.add_rower(RowerPro())
    motor_boat.row_forward()
    speed_motor_boat = motor_boat.speed

    # Большая лодка
    big_boat = Big_Boat()
    for _ in range(big_boat.max_rowers):
        big_boat.add_rower(RowerPro())
    big_boat.row_forward()
    speed_big_boat = big_boat.speed

    # Грузовая лодка
    cargo_boat = Cargo_Boat()
    for _ in range(cargo_boat.max_rowers):
        cargo_boat.add_rower(RowerPro())
    cargo_boat.row_forward()
    speed_cargo_boat = cargo_boat.speed

    # Проверка, что скорость рассчитана корректно
    assert speed_normal_boat > 0
    assert speed_motor_boat > speed_normal_boat  # Моторная лодка быстрее
    assert speed_big_boat > speed_normal_boat   # Большая лодка быстрее
    assert speed_cargo_boat > 0                 # Грузовая лодка движется