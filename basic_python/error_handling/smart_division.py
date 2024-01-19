def smart_division(x: int, y: int):
    try:
        num = x / y
        print(num)
    except ZeroDivisionError:
        print("Can't divide by zero, please use another number as y")


smart_division(30, 0)
