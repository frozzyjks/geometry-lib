# Geometry Library

Простая библиотека на Python для вычисления площади фигур.

## Поддерживаемые фигуры
Круг (`Circle`)
Треугольник (`Triangle`) с проверкой на прямоугольность

## Пример использования

```python
from geometry.shapes import Circle, Triangle

circle = Circle(3)
print(f"Площадь круга: {circle.area()}")

triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.area()}")
print(f"Прямоугольный ли треугольник? {triangle.is_right_triangle()}")
