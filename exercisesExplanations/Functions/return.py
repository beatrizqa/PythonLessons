def greet(name): 
    if name("Claire"):
        print("You smell like pickles")
        return # prevents line 5 & 6 from ex3ecuting when we use 'Claire'
    print("Welcome " + name) 

greet("Antonio") 
greet("Maria")
greet("Xiomara")
greet("Claire)")

# RETURN
#     1. Can be use to exit a function early
#     2. return is for function
#     3. 'continuous break' is for loops

# CALLER = When you call or invoke a function
#     1. We want to give the dat back to the caller to decide what to do with it
#         1. perhaps give it to another function or assign it to a variable

#Instead of printing data to tthe consaole, now this function returns data 
def greet(name): 
    if name == "Claire":
        return "Who do you think you are"
    return "Hey there. Welcome " + name

# with RETURN ==>> we give it an input, processes some data and then it gives us an output

print(greet("Claire")) 
