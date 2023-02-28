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
d: