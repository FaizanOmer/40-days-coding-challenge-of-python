# Lets dive into comparision of operaters
# comparison operators
print(10>3)
print(20<5)
print(10>=5)

# in the below chunk of code we compare the two integers.
print(10==10)

# lets try another one why it is false let me know
# because they both are store in different memory location on the system because of different data types.
print(10=="10")
# lets try this one.
print(10!="10")

# can we compare the strings with each other.
print("bag">"BAG")
# this is actually works on the numbers assiging to them in the memory which canbe accessed by ord funcion.
print(ord("B"))

# Lets dig div into the conditional statements.
# conditonals statements are weather you will do this work or not if this condtion happens so the conditional statement 
# is depend on condition on somehow.

# if the temperature is greater than 30 so its warmth drink cold water and enjoy.
temperature = 10
if temperature > 30:
    print("its warmth")
    print("drink cold water and enjoy")
elif temperature > 10:
    print("its nice and amazing weather")   
else:
    print("its cold")
print("i am done hurrah!")

# ternary operaters.
# lets we design a program for a university wether the student is eligible or not for university.
age = 22
if age > 18:
    print("eligible")
else:
    print("in_eligible")
print("hope you a good day")

# lets try another approach for this.
age = 25
if age> 20:
    message = "eligible"
else:
    message = "in_eligible"

print(message)
print("have a nice day")

# lets dive into the logical operators 
# let we build an apllication for the loan giving now we have to decide that who is eligible for loan.
# we will learn how to use And Or and Not operaters.
high_income = True
good_credit = False
Student = True

if high_income and good_credit:
    print("eligible")
else:
    print("Not eligible")
# lets seehow or operater works.
if high_income or good_credit:
    print("eligible")
else:
    print("Not eligible")
# lets try out the not operater.
if not Student:
    print("eligible")
else:
    print("Not eligible")

# lets dig dive into the short circuit evaluation.
if high_income or good_credit or not Student:
    print("eligible")
else:
    print("Not eligible")
# 
if high_income and good_credit and not Student:
    print("eligible")
else:
    print("Not eligible")
# lets dig into chaining comparison operators.
# lets we asume age should be in between 18 and 65.
age =22
if age >= 18 and age <= 65:
    print(" you are eligible for the loan")

# lets dig dive into the loop and nested loops.
# here the number is integer and which initiates the loop.
for number in range(4):
    print("dont give me excuses that you dont have time", number )
# lets play with for loops and if else.
successful = False
for number in range(5):
    print("hello buddy")
    if successful:
        print("succesful")
    else:
        print("you have to be productive programmer")
# lets understan the logic of nested loops.
# in the below code we are printing the x and y co ordinates.
for x in range(3):
    for y in range(3):
        print(f"({x}, {y})")
# in pyhton we have like primitive type like numbers strings and booleans.
print(type(5))
print(type(range(7)))
# so the range is primitive type.
# so the x will print the character of string in iterative order.
for x in "python":
    print(x)

# later on i will implement the list in detail. 
for y in [1,2,3,4,5,6]:
    print(y)

# let dig into the while loops and know how while loop works.
number =100
while number > 0:
    print(number)
    number = number // 2