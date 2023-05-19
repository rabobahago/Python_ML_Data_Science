# Get Around In Python, NumPy, Matplotlib and Pandas.
import numpy
import pandas
myarray = numpy.array([[1,2, 3], [4,5,6]])
rownames = ['a', 'b']
colnames = ['one', 'two', 'three']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

myarray = numpy.array([['JavaScript', 'Python','Java'], ['SQL', 'SQLite', 'PostgreSQL']])
rownames = ['Language', 'Database']
colnames = ['1', '2', '3']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)
