
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
    def _init(self,name,age,salary,gender):
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
