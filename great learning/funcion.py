def hello():
    print('Hello world')

hello()

# Function of Parameter
def abc(x):
    return x + 10
print(abc(10))


b = int(input("Enter your Number : "))
def even_odd(b):
    if(b%2==0):
        print('Positive Number')
    else:
        print('Negative Number')

print(even_odd(b))


# lamda function

g = lambda x: x*x*x
print(g(3))

li = [1,2,3,4,5,6,7,8,9,10]

filter_list = list(filter(lambda x: x%2 != 0,li))
print(filter_list)


map_list = list(map(lambda x: x*2,li))
print(map_list)

from functools import reduce

sum = reduce(lambda x,y:x+y,li)
print(sum)