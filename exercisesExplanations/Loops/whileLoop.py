# WHILE Loops:
#     1. Executes a block of code a number of times
#     2. Instead of determining the number of times before hand
#     3. we get until a certain condition is met
#     4. SYNTAX:
#           create a variable and set it to a certain value (i = 0)
#           while a certain condition is true:
#               do some staff
#               code to execute
#     5. The WHILE loop will keep running until the condition is not true
#     6. Always has something in the body of the WHILE loop that changes the condition or it will run
#           forever
#


for i in range(1, 6):
    print("i = {}".format(i))  # 'i' is equal to a replacement field {}

print("*" * 30)  # to diferentiate between 'for' and 'while' loop

'''EXERCISE:
    1. we create a variable 'i' and set it to 0
    2. then the WHILE loop
        1. while 'i' is less than 9
        2. print 'i' = number
        3. add i == +1 ==>> i += 1 (it takes the value of 'i' and adds 1 to it)'''
i = 0
while i < 9:
    print("i = {}".format(i))  # prints 'i' every time i is less than 9
    i += 1  # this is the same as i = i + 1

''' EXERCISE = PIZZA TOPPINGS
    1. create a while loop that keeps asking for input
    2. input should only stop when the topping chosen is in the available toppings.
        1. unless the topping we want is in the available toppings, it will keep asking to choose a topping
    '''

available_toppings = ["pepperoni", "meat balls", "cheese", "pineapple"]

topping_chosen = ""

while topping_chosen not in available_toppings:
    topping_chosen = input("Choose a topping for your pizza: ")

print("Hope you enjoy {} in your pizza".format(topping_chosen))
