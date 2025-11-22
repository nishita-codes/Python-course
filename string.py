# string ----> text hota hai - senetences , letters , words etc..
# string is immutable --> change nhi ho skta hai

# EXAMPLE
name = "nishita" # double quote
friend = 'aastha' #signle quote
apple = ''' i am eating apple 
and aastha is my C friend
hey i am good 
at programming ''' # triple quote or multiline string

print(apple)

# OPERATIONS ON STRING
# 1 . length of string
name = "Nishita"
print(len(name))

# 2.access indexing
name = "nishita"
print(name[0])
print(name[3])

# string slice
name = "nishita"
print(name[0:5]) # including 0 but not 5
print(name[0:4])
print(name[-4:-2]) # hi

# string concatenation
text = "nishita"
name = "raghav"
print(text + name)

# repetitin
print("hi " * 3)


# FUNCTIONS IN STRING
# 1.upper() , lower() 
name = "Nishita"
print(name.upper())
print(name.lower())


# 2.strip()--->remove spaces
name = "    nishita    "
print(name.strip())

# 3.replace()
name = " i love java "
print(name.replace("java" , "python"))


# 4.split()
data = "apple banana graps mango"
print(data.split(","))

# 5.join()
data = ["a" , "b" ,"c"]
print("-".join(data))

# f-string *********imp
name1= "nishita"
age = 21
print(f"My name is {name1} and i am {age} year old")

#count()
name = "nishita"
print(name.count("i"))

#endswith() -----> checks if the string ends with the given value if yes then return true else return false
str = "Welcome to the Console !!!"
print(str.endswith("!!!"))


#find() ---> searches for the fist occurence of the given value and return the index else return -1
str = "Welcome to the Console !!!"
print(str.find("Console"))

#title() ----> capitalize each letter of the word within the string
str="welcome to the console"
print(str.title())


   





