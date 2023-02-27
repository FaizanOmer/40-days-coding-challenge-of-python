# variables in python
course_name = "pYTHon programming"
print(course_name)

# string length builtint function
print(len(course_name))
# how to find the specific character in string
print(course_name[0])

# how to find the last character of string
print(course_name[-1])

# print the specific string from the written string.
# make sure that the last index is not included.
print(course_name[0:6])

# if we dont give the starting index then the compiler will consider it as initial one.
print(course_name[:3])

# if we dont assign both the values then it will return the copy of the origninal one.
print(course_name[:])

# lets dive into the concatination 
first_name = "Muhammad Faizan"
second_name = "Omer"
my_full_name = first_name + " " + second_name
print(my_full_name)

# lets have another approach 
full = f"{first_name} {second_name}"
print(full)

# lets learn some built-in functions.
print(course_name.upper())
print(course_name.lower())
print(course_name.title())

# lets use strip for the removing free space at beginning and ending.
course_title = "      hello i am mern stack developer  "
print(course_title)
print(course_title.strip())

# we use rstrip for the right and lstrip for the left side.
print(course_title.rstrip())
print(course_title.lstrip())

# lets find the specific string index number.
print(course_title.find("mern"))

# lets replace the values.
print(course_title.replace("r","a"))

# lets play with the boolean values.
print("mern" in course_title)
print("mean" in course_title)
print("mean" not in course_title)

# number types in numbers.
# absolute as abs.
print(abs(-3.66))
# round numbers.
print(round(4.99))
import math as mt

print(mt.ceil(3.33))

# type conversions in python
x = 1
print(type(x))
y = 1.222
print(type(y))
z = "i am full stack developer"
print(type(z))
