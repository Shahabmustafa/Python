# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.


salary = int(input('Enter Salary : '))

service = int(input('Enter your Service : '))
if(service > 5):
    print('You are salary is',salary*5)
else:
    print('You are not eliable 5 Parsent bonus'),


# Take two int values from user and print greatest among them.

first = int(input("Enter your first number : ")),
second = int(input("Enter your second number : ")),

if(first > second):
    print('first is Grether than Number',first)
elif(first < second):
    print('second is Grether than Number',second )
elif(first == second):
    print("first and second are Equal")
else:
    print('error')


# A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantitySuppose, one unit will cost 100.Judge and print total cost for user.

item = int(input("Item Price : "))

if(item > 1000):
    print('You are Decount is',item / 10)
else:
    print('your are not eligible this discount')




# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.

totalNumber = 1100

Name = input('Enter your Name : ')
obtainMark = int(input('Enter your obtain Marks : '))

percentage = obtainMark * 100 / 1100

if(percentage >= 90):
    print(' A Excelent Percentage',percentage)
elif(percentage >= 80):
    print(' B Very Good Percentage',percentage)
elif(percentage >= 70):
    print(' C Good Percentage',percentage)
elif(percentage >= 60):
    print(' D Better Percentage',percentage)
elif(percentage >= 50):
    print(' E Better Percentage',percentage)
elif(percentage >= 40):
    print(' F Better Percentage',percentage)
elif(percentage >= 30):
    print(' G Better Percentage',percentage)
