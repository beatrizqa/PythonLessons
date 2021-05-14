def greet(person, first_time=False):  # it will take a person, in the body we create a
    # custom message for this person. We also add another
    # flag variable 'first_time'  it is the first time in the
    # app and we default that to FALSE
    if first_time:  # Because it is a first time we give them a different message
        return "First time for everythhing. Welcome " + person
    return "Hello, " + person  # in this function we are returning a value


def greet_all(people):  # it takes a list of people, iterates through the list and prints
    # 'hello person' for each one
    for person in people:
       # print("Hello " + person) ===>> we are replacing this 'print' with another 'function call'
        # we need to create this function above 'greet_all' function
        print(greet(person))


friends = ["Maria", "Pablo", "Antonio"]

greet_all(friends)


def greet(person, first_time=False):
    if first_time:
        return "First time for everythhing. Welcome, " + person
    return "Hello, " + person


def greet_all(people):
    for person in people:
        print(greet(person, True))


friends = ["Maria", "Pablo", "Antonio"]

greet_all(friends)
