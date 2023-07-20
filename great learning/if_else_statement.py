# marks = int(input("Enter Your Grades : "))

# if(marks > 70):
#     print("Get Motocycle")
# else:
#     print("Give Practis Test")

#     a = 10
#     b = 20
#     c = 30

#     if(a>b | a>c):
#         print("a is the greattest")
#     elif(b>a | b>c):
#         print("b is the greattest")
#     else:
#         print("c is the greattest")

# if with list
list = [1,2,3,4,5,6]

if list[5] == 6:
    list[5] = list[5] + 100
    print(list)
else:
    list[5] = list[5] + 500
    print(list)

# if with dictonery

dic = {'a' : 1,'b' : 2,'c' : 3,'d' : 4}

if dic['b'] == 2:
    dic['b'] = dic['b'] + 50
    print(dic)

# if with tuple
addName = str(input("Enter Your Name : "))
tuple = ('Shahab Mustafa','Bilal Mustafa','Sheraz Mustafa','Kashif Mustafa','Aftab Mustafa')

if addName in tuple:
    print(addName,"is Present in Tuple")
else:
    print('Your Name not Register in Tuple')
