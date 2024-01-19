def g(*words):
    uppercase_word = map(str.upper, words)
    print(*uppercase_word)
g('This', 'is', "My", "Love")
def f(*words):
    uppercase_words = [word.upper() for word in words]
    print(*uppercase_words)
f('This', 'is', 'CS50')

nums = [30, 5, 7, 90, 100, 1000]
larger_num = filter(lambda x: x > 50, nums)
print(list(larger_num))
larger_num = [num + 2 for num in nums if num > 45]
square_num = [num * num for num in nums]
print(larger_num, square_num)
