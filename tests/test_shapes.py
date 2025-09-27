import math
import pytest
from geometry.shapes import Circle, Triangle

def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * 4)

def test_triangle_area():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0)

def test_triangle_right():
    t = Triangle(3, 4, 5)
    assert t.is_right_triangle() is True
    t2 = Triangle(2, 3, 4)
    assert t2.is_right_triangle() is False

def test_polymorphism():
    shapes = [Circle(1), Triangle(3, 4, 5)]
    areas = [s.area() for s in shapes]
    assert math.isclose(areas[0], math.pi)
    assert math.isclose(areas[1], 6.0)

def test_invalid_triangle():
    with pytest.raises(ValueError):
        Triangle(1, 2, 100)
