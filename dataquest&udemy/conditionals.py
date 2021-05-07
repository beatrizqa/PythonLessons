age = int(input("Hey Mr Potter, how old are you?"))
print (age)

if age >= 17:
    print("Welcome to the party Harry!")
else:
    print("Sorry Mr Potter but you are not even old enough to do magic outside the school")

'''
IF STATEMENT STRUCTURE
    1. IF
    2. then we check for some condition 'some condition'
        1. if that 'condition' is true, then we will execute a code block inside the STATEMENT
based on the if statement we are going to print something different
    1. if the age is greater than or equal to 17 then we'll print "Welcome to the party Harry"
    2. the condition is TRUE whenever the age is greater than or equal to 17
        1. if the age is less than 17, the condition 'age >=17' is FALSE and it does not run the code in the if statement (print....)
    3. If the age is <= 17 and we want to print a different statement we use else
        1. if the condition is not true we will execute the code inside the ELSE statement'''

# If Statement Structure
#         if some condition
#             if the condition is true
#             code to execute
#         else
#             if condition is not true
#             this code executes 

'''
CHALLENGE
    1. Create an 'if statement that checks if age < 17
    2. print something if the condition is true
    3. create an 'else statement'
    4. print something different in that case
'''
age = int(input("Hello, how old are you?: "))

if age < 17:
    print("Are you thinking of going to University?")
else:
    print("What university did you go to?")


