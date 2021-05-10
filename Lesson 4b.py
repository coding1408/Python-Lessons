#functions
def greetUser ():
    print ("hello")

def greetUser2( name):
    print ("hello "+ str(name))

def getFormatedName(firstName, LastName):
    fullName = firstName + " " + LastName
    return fullName.title()

def jamesBond( firstName, lastName):
    bond = lastName + ", " + firstName + " " + lastName
    return bond.title()

def addition(a, b):
    c = a + b
    return c

def subtration(a, b):
    c = a - b
    return c

def multiplication (a, b):
    c = a * b
    return c

def division (a, b):
    c = a / b
    return c


greetUser()
greetUser2("Aiden")


name = getFormatedName('bam' , 'dam')
print(name)

name2 = jamesBond('Pop', 'Mac')
print(name2)

print(addition(3, 5))
print(subtration(3, 5))
print(multiplication(3, 5))
print(division(3, 5))

