#this python file is just me experimenting with basic code to refamiliarise myself with python"
from ast import Break
from subprocess import list2cmdline


print("Hello World")
if 0 > 2:
    print("mamma mia")
else:
    print("You Fucked Up")
X = 5
print(X) #remember variables are case sensitive
print(33 == 22) # booleans print true or false

listsSuck = ["apple", "banana", "murder", 2] #just kidding lists are fine but dont get cocky
#lists are ordered and changeable   
print(listsSuck)
listsSuck.append("BEANS")
print(listsSuck)
listsSuck.insert(1,"cyanide") #remember that position 1 is actually second in the list
print(listsSuck)
listsSuck.pop(2)
print(listsSuck)
for x in listsSuck:
    print(x)
    if x == "murder":
        break #this simply stops the loop when it finds murder

def functionTest(): #if there are going to be args passed into the function trype them in the brackets, use *arg if its an unknown amount
    print("the test function works")

functionTest()

class stayClassy:
    def __init__(self, name, age): #this does not need to be named self but it does need to be the first item in a clas
        self.name = name
        self.age = age  
    
    def endboard(self):
        print("gamermode"+ self.name)
    
    def __str__(self):
        return f"{self.name}({self.age})" #this combines the set into a string.

    def classism(self):
        print("damn " + self.name)

p1 = stayClassy("megadeth 2000", 34)

print(p1.name)
print(p1.age)
print(p1)
p1.classism()
p1.endboard()

class inheritor(stayClassy): #this means inheritor takes on the properties of "stayclassy" allowing its properties to be reused or added to
    pass
inher = inheritor("John",11)
inher.classism()

username = input("Enter your username:") # the input function pauses operation for the user to perform inputs
print("Username is " + username)
