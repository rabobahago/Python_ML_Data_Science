class Rectagle:
    def __init__(self, side_a, side_b) -> None:
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self) -> str:
        return f'Area of rectangle with side a: {self.side_a} and side b: {self.side_b} is: {self.side_a * self.side_b}'
