# FUNCTIONS & SYNTAX:
#     1. Think of a function as a machine that takes input and produces a result
#     2. some instructions grouped together that perform a certain task
#     1. def == definition ==>>> define the following function
#     2. 'name of the function' ==>> give the function a name you want
#     3. ():  ==>>>>  this is where the parameters will go
#     4. indentention ==> this means the code in the indentation is part of the function.
#     5. call the function ==>> use the function  ==>>> execute the function
#         1. you write the function name followed by ()

# A function can be:
#     1. a collection of code
#         1. You can use a function over and over again
#     2. a mapping
#         1. define a function called function2  which will take an input or an argument
#         2. we are calling the argument 'x'
#         3. in return to whoever calls this function we are returning '2*x'
#         4. we are MAPPING the input x to the output 2*x
#             def function2(x):
#                 return 2*x
#         5. to call this function we use
#             a = function2(3)
#                 1. this will assign '6' to the variable 'a'
#         6. a function can have MULTIPLE ARGUMENTS:
#             def function3(x, y): ==>>>> it takes 2 arguments 'x' and 'y'
#                 return x + y
#         7. to call this function:
#             a = function3(1, 2)

# RETURNING SOMETHING
#     1. the function allows to operate in some data and pass the result to whatever we called
#         our function
#     2. def helloFunc():
#         return "Hello Function."
#             1. This means when we execute our function (helloFunc()) it's going to be equal to
#                 our return value ===>>> "helloFunc" == "Hello Function."
#     3. The function in line 33-34 when executed, returns a string.
#           1. Once this happens, the function can be treated as a String and had methods like a variable
#         so helloFunc().upper() will return "HELLO FUNCTION.""


def absolute_value(num):  # define the following function
    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))  # this will return '4' because is '-4' return '-num'

# BENEFITS OF FUNCTIONS:
#     1. We can save lines of code if function is large
#     2. One source of truth. No repeat of code. We do not need to repeat ourselves ==>> "KEEPING
#        YOUR CODE DRY"
#     3. Need changes? update one spot
#     4. can improve code readability
#     5. allows to put code with a specific purpose into a single location


def greet(name):  # we need to create a variable inside the ()_ in the function == PARAMETER

    print("Hey there")
    # change 'Pablo' to variable 'name' so we can change the names when calling greet()
    print("Welcome " + name)


# We want this function to work with 'anybody' not just 'Pablo'
# 'Antonio' = argument, when you pass data to the function
greet("Antonio")  # invoke a function  in passing a name
greet("Maria")
greet("Xiomara")
