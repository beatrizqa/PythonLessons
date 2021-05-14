actualAge = 665

print("What is Flamel's age, Wesley?")
guess = int(input())

    # == to compare if the 2 values are equal (es lo mismo que)
    # != opposite to == (no es lo mismo que)
    # = to assign a value to a variable

# THIS IS WHEN GUESS == AGE
if guess == actualAge: # this means we guessed correctly and so we check if guess is <> the age and print different statements
    print("You guessed correctly, 20 points for Griffindor!!")
    
else: # this means we guessed incorrectly and so we check if guess is <> the age and print different statements
    if guess < actualAge:
        print("Ron, guess higher")
    else:
        print("Please Mr Wesley, guess lower")
    
    guess = int(input())
    if guess == actualAge:
        print("Yeah! You got it right!")
    else:
        print("No, no, no, no!")


# THIS IS WHEN THE GUESS != TO AGE
'''
1. If the guess is NOT EQUAL to the actual age
    1. then we are going to check if the guess is less than the actual actualAge
    2. and print "Ron, guess higher"
2. ELSE if the guess is greater that the actual age 
    1. then we are going to print "Please Mr Wesley, guess lower" '''

if guess != actualAge: # this means we guessed incorrectly and so we check if guess is <> the age and print different statements
    if guess < actualAge:
        print("Ron, guess higher")
    else:
        print("Please Mr Wesley, guess lower")
    
    guess = int(input())
    if guess == actualAge:
        print("Yeah! You got it right!")
    else:
        print("No, no, no, no!")
else:
    print("You guessed correctly, 20 points for Griffindor!!")


# OLD WAY TO DO IT
# print("What is Flamel's age, Wesley?")
# guess = int(input())
# if guess < actualAge:
#     print("Please Ron guess higher")
#     guess = int(input())
#     if guess == actualAge:
#         print("Well done Ron, 10 points for Griffindor")
#     else:
#         print("Ron, you should know better")

# elif guess > actualAge:
#     print("Please Mr Wesley, guess lower")
#     guess = int(input())
#     if guess == actualAge:
#         print("Well done Mr Wesley, 10 points for Griffindor")
#     else:
#         print("Mr Wesley!!!! That is wrong")

# else:
#     print("You guessed correctly, 20 points for Griffindor!!")



