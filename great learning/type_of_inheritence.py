# Type of Inheritence

# Single Inheritence
# Multiple Inheritence
# Multi-Level Inheritence
# hybrid Inheritence


class parent1:
    def assign_str1(self,str1):
        self.str1 = str1
    
    def show_str1(self):
        print(self.str1)


class parent2:
    def assign_str2(self,str2):
        self.str2 = str2

    def show_str2(self):
        print(self.str2)

class child(parent1,parent2):
    def assign_str3(self,str3):
        self.str3 = str3

    def show_str3(self):
        print(self.str3)

a1 = child()

a1.assign_str1("Hello world")
a1.assign_str2("Hi How are you")
a1.assign_str3("Hi Guys")

a = a1.show_str1()
b = a1.show_str2()
c = a1.show_str3()

print(a)
print(b)
print(a1.show_str3())
# print(a1.show_str2())
# print(a1.show_str3())


c = "shahab"

print(len(c))