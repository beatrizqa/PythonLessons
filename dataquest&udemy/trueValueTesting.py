name = input("What is your name? ")

# if name: # this means if there is a name in the input, so we check if the value is there
#     print("Hey there {}". format(name))
# else:
#     print("Who are you?")

# CHECKING FOR AN EMPTY STRING
#     1. change from a simple condition to check if the name variable is EMPTY
#     2. Hint: empty string ""

if name == "":
    print("who are you?")
else:
    print("Hey there {}".format(name))
