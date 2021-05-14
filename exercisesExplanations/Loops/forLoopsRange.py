''' EXERCISE
    1. create a for loop over a certain range
    2. print each one of the values in a separate line
    3. include 'i' in a range. The RANGE is set in ((1, 30) it's up to but not included)
    4. print i in the following format ==>> 'i : 1' '''

for i in range(1, 30):
    print("i : {}".format(i))

# With RANGES
#   1. you do not have to sopecify a starting point if you want to start at 0
#   2. you can add 'steps' (0, 30 2) ==>> from 0 to 29 every 2 numbers (0, 2, 4, ...)
#   3. you can also go backwards (30, 0 -2)

''' EXERCISE 2 
    1. use 'range' to evaluate the condition on the temperature of your memory card'''

temperature = int(input("How hot is your memory card?: "))
if temperature in range(20, 71):
    print("Cool, you can keep playing")
else:
    print("Sorry, can't do")
