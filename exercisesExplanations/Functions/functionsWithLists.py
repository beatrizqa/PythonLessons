def greet_all(people):  # it is going to greet every person inside of a list
    # inside the () the parameter is 'people'
    for person in people:
        print("Hello " + person)


# Now we create a list outside of the function called 'friends'
friends = ["Maria", "Pablo", "Antonio"]
# now we can invoke this
# we pass in friends in the (). We are calling everyone in the list
greet_all(friends)
# 'friends', we do not have to pass any name, just the name oif the list


# Extract the functionality of the function into a function and invoke the function
# whenever we need it
