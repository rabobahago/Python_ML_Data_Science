class Square:
    def __init__(self, side) -> None:
        self.side = side

    def __str__(self) -> str:
        return f'Area of square with side: {self.side} is: {self.side * self.side}'
