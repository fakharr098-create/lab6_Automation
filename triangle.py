def classify_triangle(a, b, c):
    sides = (a, b, c)

    if any(type(side) is not int or not 1 <= side <= 200 for side in sides):
        return "Invalid"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid"

    if a == b == c:
        return "Equilateral"

    if a == b or b == c or a == c:
        return "Isosceles"

    return "Scalene"