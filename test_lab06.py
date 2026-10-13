import pytest

from triangle import classify_triangle
from insurance import calculate_discount


@pytest.mark.parametrize("a,b,c,expected", [
    (5, 5, 5, "Equilateral"),
    (5, 5, 8, "Isosceles"),
    (4, 5, 6, "Scalene"),
    (2, 3, 5, "Invalid"),
])
def test_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected


@pytest.mark.parametrize("age,claims,policy,expected", [
    ("Under 25", "None", "Standard", 10),
    ("25-65", "None", "Premium", 20),
    ("25-65", "One", "Standard", 5),
    ("Over 65", "2+", "Premium", 0),
])
def test_insurance(age, claims, policy, expected):
    assert calculate_discount(age, claims, policy) == expected