from functools import reduce
#lambda arguments: expression
add10 = lambda x: x + 10
print(add10(10))

mul = lambda x, y: x * y
print(mul(5, 6))

point = [(99, 2), (9, 4), (53, 23), (8, 24)]
sorted_rule = lambda x: x[1]
sorted_point = sorted(point, key=sorted_rule)
print(point)
print(sorted_point)
#map(func, sequence)
lis = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
square = map(lambda x: x * x, lis)
print(list(square))
r = [x * x for x in lis]
print(list(r))
#filter(func, sequence)
sum_of_list = filter(lambda x: x < 5, lis)
print(list(sum_of_list))
c =  [x for x in lis if x % 2 == 0 ]
print(list(c))
#reduce(func, sequence)
nums = [7, 2, 4, 8, 12]
reduce_nums = reduce(lambda x, y: x + y, nums)
print(reduce_nums)