magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"Hello, {magician.title()}. I love python programming")
print('end')

#range
for num in range(1, 9):
    print(num)

num_list = list(range(2, 8))
print(num_list)


final_list = []
square_list = list(range(2, 8))
for num in square_list:
    square = num ** 2
    final_list.append(square)
print(final_list)

list_num = [3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(max(list_num))
print(min(list_num))
print(sum(list_num))

square_num = [value ** 2 for value in list_num]
print(square_num)

#slice
slice_num = list_num[:3]
print(slice_num)
print(list_num[1:4])
print(list_num[:-1])
print(list_num[:])
for num in list_num[1:4]:
    print(num)
