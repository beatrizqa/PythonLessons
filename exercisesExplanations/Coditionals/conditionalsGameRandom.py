import random
# 'random' is a library
#     1. A library is a collection of codes that have their methods in them that we can use
#     2. No need to 'reinvent' the wheel

actualAge = random.randint(1, 20)  # it returns a random value between a & b
# a random no between 1-20 will be generated using the method 'radint'
print(actualAge)

guess = None

''' ANOTHER WAY TO DO IT to change the highest random number (1,20) (1, 60) (1,35)
    1. declare a variable called 'highestAge' and assign any value
    2. now "actualAge = random.randint(1, 20)" will be == to "actualAge = random.randint(1, highestAge)
    3. the first input (print("What is Flamel's age, Wesley?")) will change to 
        "print("What is Flamel's age, Wesley? (1, {}".format(highestAge))
'''
print("What is Flamel's age, Wesley?")


while guess != actualAge:
    # as long as the GUESS is different to actualAge it will keep asking
    guess = int(input())

    if guess == 0:
        print("Really?? Goodbye :(")
        break

    if guess == actualAge:
        print("You guessed correctly, 20 points for Griffindor!!")

    else:
        if guess < actualAge:
            print("Ron, guess higher")
        else:
            print("Please Mr Wesley, guess lower")

''' We do not need this as this was for the SECOND GUESS, but now we have a loop
        guess = int(input())
        if guess == actualAge:
            print("Yeah! You got it right!")
        else:
            print("No, no, no, no!")
'''
