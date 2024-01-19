#errors & Exceptions
# x = 9
# if x > 150:
#     raise Exception('Invalid number, x must greater than 150')
# y = 100
# assert(y >= 106),'x is less than 101'



# try:
#     a = 400 / 0
#     print(a)
# except Exception as e:
#     print(e)

try:
    a = 7 / 0
    b = 90 + ""
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up')