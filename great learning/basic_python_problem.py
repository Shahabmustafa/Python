num = int(input("Enter Your Number : "))

if(num % 2) == 0:
    print("Even Number",num)
else:
    print("ODD Number",num)


num1 = float(input("Enter your Number : "))

if num1 > 0:
    print('Your Number is Positive')
elif num1 == 0:
    print('Your Number is Zero')
else:
    print("your Number is Negitive")


fac = int(input("Enter your Number : "))

factorial = 1

if(fac < 0):
    print("Sorry,Factorial does not exist for negitive number")
elif(fac == 0):
    print("0 Factorial is 1")
else:
    for i in range(1,fac+1):
        factorial = factorial * i
        print(factorial)

n = int(input("Enter your Number : "))
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
    print("Reverse of the Number",rev)


an = int(input("Enter Your Number : "))

b = 1

print(an + b)