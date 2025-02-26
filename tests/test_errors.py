import pytest
from mechanics.person import RowerBeginner
from mechanics.boat import Boat

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