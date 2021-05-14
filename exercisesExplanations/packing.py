def greet_all(*people):  # by adding '*' now the function can take UNLIMITED arguments
    for person in people:
        print("Hello " + person)

# friends = ["Maria", "Pablo", "Antonio"]


# gives an error as function has only 1 parameter
greet_all("Maria", "Pablo", "Antonio")
# (people) and we are trying to pass 3 (Maria...)

# UNPACKING DATA
#   1. How to take a list and convert it in a bunch of different arguments
#   2. We have 3 parameters, name, age, email
#   3. what if we had a list of data instead


def print_info(name, age, email):
    print(name + "is " + str(age) + ". Reached at " + email)
# print_info("Pablo", 23, "pab@pab.com")


# we create a list
info = ["Pablo", 23, "pab@pab.com"]
# we pass the details in 'info' list as
print(print_info(info[0], info[1], info[2]))
# argumnents for the print_info function.
# You have to pass each element you want to
# print
