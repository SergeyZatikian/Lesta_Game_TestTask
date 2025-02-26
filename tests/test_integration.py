import pytest
from mechanics.person import RowerBeginner, RowerPro
from mechanics.boat import Boat, Big_Boat, Motor_Boat, Cargo_Boat

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
    boat = Boat()
    for _ in range(boat.max_rowers):
        boat.add_rower(RowerPro())
    boat.row_forward()
    speed_normal_boat = boat.speed

    motor_boat = Motor_Boat()
    for _ in range(motor_boat.max_rowers):
        motor_boat.add_rower(RowerPro())
    motor_boat.row_forward()
    speed_motor_boat = motor_boat.speed

    big_boat = Big_Boat()
    for _ in range(big_boat.max_rowers):
        big_boat.add_rower(RowerPro())
    big_boat.row_forward()
    speed_big_boat = big_boat.speed

    cargo_boat = Cargo_Boat()
    for _ in range(cargo_boat.max_rowers):
        cargo_boat.add_rower(RowerPro())
    cargo_boat.row_forward()
    speed_cargo_boat = cargo_boat.speed

    assert speed_normal_boat > 0
    assert speed_motor_boat > speed_normal_boat
    assert speed_big_boat > speed_normal_boat
    assert speed_cargo_boat > 0