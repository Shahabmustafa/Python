
class Name:
    def shahab(self):
        print("My Name Is Shahab Mustafa")

    def bilal(self):
        print("My Name is Bilal Mustafa")
        
print(Name().bilal())
print(Name().shahab())


# pass parameter in class

class Phone:
    def set_color(set,color):
        set.color = color
    
    def set_size(set,size):
        set.size = size
    
    def show_color(set):
        return set.color
    def show_size(set):
        return set.size
    
p2 = Phone()
p2.set_color('Blue')
p2.set_size(20)

print(p2.show_color())
print(p2.show_size())


# Build Constructor in Class

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_detail(self):
        print("Enter Your Name : ",self.name)
        print("Enter Your age : ",self.age)
        print("Enter Your Salary : ",self.salary)
        print("Enter Your Gender : ",self.gender)

e1 = Employee("Shahab",19,25000,"Male")
print(e1.employee_detail())


# inhertiance class

class Vehicle:
    def __init__(self,color,size):
        self.color = color
        self.size = size

    def vehicle_detail(self):
        print('Your Color is',self.color)
        print('Your Car Size is',self.size)
    
e2 = Vehicle("blue",15)
print(e2.vehicle_detail())


class Car(Vehicle):
    def show_car(self):
        print('My car Name is Toyota')

c1 = Car('Red',20)

print(c1.show_car())


# overriding init method

class Fruit:
    def __init__ (self,name,price):
        self.name = name
        self.price = price
    def show_detail(self):
        print("Fruit Name",self.name)
        print("Fruit Price",self.price)

class Vegitable(Fruit):
    def __init__(self,name,price,vName,vPrice):
        super().__init__(name,price)
        self.vName = vName
        self.vPrice = vPrice

    def show_vegetable_detail(self):
        print("Vegetable Name",self.vName)
        print("Vegetable Price",self.vPrice)

f1 = Vegitable("Mango",150,"Potato",100)

print(f1.show_detail())
print(f1.show_vegetable_detail())