def rsmart_divider(x: int, y: int):
    try:
        num = x / y
        print(num)
    except ZeroDivisionError:
        print("Can't divide by zero, please divide by another number")
    except TypeError:
        print('Both x and y must be of the same type')
    except Exception as e:
        print('Oops, something went wrong,: {e}')


rsmart_divider(2, '2')
