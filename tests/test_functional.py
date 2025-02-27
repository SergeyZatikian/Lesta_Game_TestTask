import pytest
from mechanics.person import RowerBeginner, RowerPro
from mechanics.boat import Boat

@pytest.mark.parametrize("rower", [RowerBeginner, RowerPro])
def test_add_rower(rower):
    boat = Boat()
    rower = rower()
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