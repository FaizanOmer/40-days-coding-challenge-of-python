# lets dig dive into the fuctions as we already use builtin functions but now we create oue own custom functions.
def greet():
    print("hi welcome to functions")
    print("welcome on board")
greet()

# lets define parameters in function and then pass arguments to know about function re usability.
def greet(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome on board")

greet("Muhammad", "Faizan Omer")
greet("Muhammad","Furqan Omer")

# so we have two types of functions
# 1 that is to build to perform some specific task. above we have this type function.
# 2 another one is to return some value so we can use that value later on in some other function.

def welcome_greetings(name):
    return f"hi {name}"

message = welcome_greetings("Muhammad")
#later on we will pass message as an argument to any function.
print(message)
# greet is a function retruns none value in python every function returns none value by default.
def greet(name):
    print(f"hi {name}")

print(greet("Faizan"))

# lets dive into the keyword arguments.
# lets incement the number by passing an argument.
def increment(number, by):
    return number + by

print(increment(5,1))

# lets dig dive into the default arguments.
# we will use default as an parameter in the function.
def increment(number, by=1):
    return number + by

print(increment(11))

# lets define a function that takes a variable numbr of arguments.
def multiply(x,y):
    return x*y

print(multiply(2,4)) 

def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total

print(multiply(2,4,5,6))

# lets have some work on dictionaries.
def save_user(**user):
    print(user)

save_user(id="1", name="muhammad", age="23")

# here is hte end of the functions now into next we move towards data structures.