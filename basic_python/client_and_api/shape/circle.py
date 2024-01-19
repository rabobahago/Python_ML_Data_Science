from math import pi


class Cicle:
    def __init__(self, radius) -> None:
        self.radius = radius

    def __str__(self) -> str:
        return f'Area of Circle with radius of {self.radius} is: {pi * self.radius * self.radius}'
