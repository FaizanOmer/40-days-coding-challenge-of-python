# lets begin the journey of data stuctures in python we will see and practice different topics.

# lets know about the lists.
letters = ["f","a","i","z","a","n"]
matrix = [["0","1"], ["2","3"]]
# in the below one line code we make a list of zeros.
zeros = ["0"]* 5
print(zeros) 
# lets combine the above lists together.
combined = letters + matrix + zeros
print(combined)

# lets we make a list of 20 integers then we have builtin functions lets explore.
numbers = list(range(21))
print(numbers)

# lets break the string into the characters.
chars = list("faizan omer")
print(chars)
print(len(chars))

# lets learn about that how to access item from the list.
list1 = ["a","b","c","d"]
print(list1[0])
# if you want to print the first three items from the list then here we go.
print(list1[0:3])
# in the below code we change the character at index 0.
list1[0] = "A"
print(list1)

#lets how to print even and odd numbers of the from the list.
numbers = list(range(21))
print(numbers[::2])
print(numbers[::3])
# lets print the list in the reverse order.
print(numbers[::-1])

# lets learn about how to unpack the lists.

number1 = [0,1,2,3,4,5,6,7,8,9,10]
first,*others, last = number1

print(first,last)
print(others)

# lets dig into the looping over lists.
letters = ["a","b","c"]
for letter in enumerate(letters):
    print(letter)

# Adding or removing items from the lists.
letters2 = ["A","B","C","D"]

# lets add charater in the list
letters2.append("E")

print(letters2)


