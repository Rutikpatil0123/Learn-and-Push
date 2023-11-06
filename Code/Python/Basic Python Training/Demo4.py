from functools import reduce

#higher Order Functions
def square(x):
    return x*x

def even(x):
    return x % 2 == 0

def subtract(a,b):
    return a - b

def applier(q,x):
    return q(x)

print(applier(square , 5))

double  = lambda x : x * 2
print(applier(square , 7))
print(applier(double, 7))

list1 = [2,4,6,8]
list2 = [11,24,5,23]

# map and filter and redue

print(list(map(double,list2)))
print(list(map(square, list1)))
print(list(map(even, range(10,20))))
print(list(filter(even, range(10,30))))

print(list(zip(list1,list2)))

print(reduce(lambda x,y : x+y, list1))

# list comprehensions
print([i * 2 for i in list1])

list3 = [i * 2 for i in list1]
print(list3)

li = [('a',1), ('b', 2), ('c', 3)]

print([n * 3 for(x,n) in li])

oplist = [(6,3),(1,7),(5,5)]

print([subtract(y,x) for (x,y) in oplist])

print([i * 2 for i in list1 if i > 4])

