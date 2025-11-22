# if else conditional statement ka use decision lene me hota hai.

# IF STATEMENT :
age = 18
if age>= 18:
    print("you are eligible to vote")

# IF ELSE STATEMENT:
age = 17
if age>= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote") 


    # ELIF STATEMENT:
    num = 65
    if num<0:
        print("num is negative")
    elif (num == 0):
     print("number is zero")
    else:
       print("number is positive")
    
    #NESTED IF
    num = 10 
    if num>=0:
       if num == 0:
          print("number is zero")
       else:
          print("number is positive")
    else:
       print("number is negative")



    #    EXCERCISE:
    # create a python program capable of greeting you with good moring, good afternoon and good evening. your program must use time module to get current hour. here is a sample program and documentation link for you.

    import time
    timestamp = time.strftime("%H:%M:%S")
    print(timestamp)
    timestamp = int(time.strftime("%H"))
    print(timestamp)
    timestamp = int(time.strftime("%M"))
    print(timestamp)
    timestamp = int(time.strftime("%S"))
    print(timestamp)