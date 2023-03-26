from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

#Counter
letters = 'aaaabbbbcccc'
my_dict_letter = Counter(letters)
print(my_dict_letter)
print(my_dict_letter.keys())
print(my_dict_letter.values())
print(my_dict_letter.items())
print(my_dict_letter.most_common(1))
#most common
print(my_dict_letter.most_common(2)[0][0])
#element as a list
print(list(my_dict_letter.elements()))
#namedtuple
Point = namedtuple("Point", 'x, y')
point = Point(1, 4)
print(point)
print(point.x, point.y)

#OrderedDict: this allow us to remember the order
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)

#default dict
d = defaultdict(int)
d['a'] = 1
d['b'] = 3
d['c'] = 4
d['d']
print(d['d'])

#deque
d = deque()
d.append(2)
d.append(4)
print(d)
d.appendleft(500)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
#extends deque with multiple
d.extend(['a', 'b', 'c', 'd'])
print(d)