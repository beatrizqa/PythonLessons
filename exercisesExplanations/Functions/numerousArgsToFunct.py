def greet(name="User", be_nice=True):  # 'be_nice' is going to default to TRUE
    if not be_nice:
        return "Who do you think you are"
    return "Hey there. Welcome " + name


# now we have the option in here of passing 'FALSE'
print(greet("Pablo", False))

# KEYWORD
#     1. we are putting the parameter name (be_nice) in the argument 'print(greet(be_nice=FALSE))'
#     2. POSITIONAL arguments must come first and then the NAMED arguments
#     3. POSITIONAL arguments ==>> 'be_nice = False'
#     4. NAMED arguments ==>> "Pablo"
# Example ==>>  print(greet(be_nice=False, name = "Pablo")) ==>> Parameters by name

POSITIONAL ONLY PARAMETERS
1. You cannot swap the positions of the parameters in the function:
    2. def greet(name="User", be_nice=True):
        1. name = User == ==>> > parameter 1
        2. be_nice = True == == = >> parameter 2


# with the '/' you cannot swap the positions in the arguments when calling the function
def greet(name="User", be_nice, /):
    if not be_nice:
        return "Who do you think you are"
    return "Hey there. Welcome " + name


# this will give an error because we are using a NAMED argument(be_nice)
print(greet("Pablo", be_nice=True))

# Can make SOME OF THE parameters POSITIONAL only:
#     1. to make 'name' positional only you put ', /' after name
#         1. def greet(name, /, be_nice):
#     2. Anything before the '/' is positioned only and everything after the '/' is by name only

Whether you pass data by POSITION, KEYWORD or BOTH
1. Anything on the left of the '/' is by POSITION only
2. Anything after the '/' is either
3. Anything after the '*' is keyword only


def do_nothing(pos1, pos2, pos3, /, either1, either2, *, keyword1, keyword2, keyword3):
