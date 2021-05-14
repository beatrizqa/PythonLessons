# LOOPS:
#    1. can execute a block of code a number if times and we can determine the number of times we
#        want to execute that code
#     2. we can give it a certain value that will predetermine the number of times the loop has to run
#     3. Good if you run SAME cosde over and over again, each time with a different value
#     4. SYNTAX
#         for each number of times we want to loop:
#             do some staff
#             code to execute

'''EXERCISE
    1. Create a message "I'm learning Python"
    2. create a loop that will go over each character in the string and print it out
    3. create a variable called 'character' in the loop
    4. we are going to search inside the message
    5. every time we get the character we are going to print it out '''

message = "I'm learning Python"
for character in message:
    print(character)

'''EXERCISE 2
    1. Print all the separators in the string
        1. create an empty string called separators
        2. get the characters in the string to check if they are separators
        3. if the character is not numeric (there is a method called .isnumeric that returns True or False 
            if the character is numeric)
        4. add, using +=, the separators to the 'separators' variable created 
            1. separators += character is the same as separators = separators + character
        5. print out the variable 'separators'
'''
data_coming_in = "6,5216/56746545\\54654.585727pd65585,587453"

separators = ""

for character in data_coming_in:
    if not character.isnumeric():  # we are checking that the character is NOT numeric
        separators += character
print(separators)
