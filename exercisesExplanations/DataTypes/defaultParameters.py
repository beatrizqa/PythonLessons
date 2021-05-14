def greet(name = "User"): #now if you do not put your name it defaults to 'user'
    if name == "Claire":
        return "Who do you think you are"
    return "Hey there. Welcome " + name

print(greet()) # now we can invoke greet() without name and will print 'Welcome user' as 
                        # it has 'user' as default in the () in the def greet()
                        # We can overwrite greet() and give it a value greet("Pablo") and it will 
                        # use 'Pablo' instead of user 

