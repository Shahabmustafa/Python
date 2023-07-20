# while loop

num1 = int(input("Enter your Table : "))
result = 1
while result <= 10:
    print(num1,"x",result,"=",result*num1)
    result = result + 1

list = [1,2,3,4,5]

i = 0

while i < len(list):
    list[i] = list[i] + 100
    i = i+1
    print(list)


# for loop

l1 = ['Shahab','Kashif','Sheraz','Aftab','Bilal']
l2 = ['Mustafa']

for i in l1:
    for b in l2:
        print(i,b)