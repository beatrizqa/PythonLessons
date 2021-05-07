#car = "bmw m3"

carName = input("What car would you like? ")

# if carName in car:
#     print("{} is in {}".format(carName, car))
# else:
#     print("Sorry we do not have a {}".format(carName))

# IN and NOT IN
#     1. create an input to get a car's name
#     2. create a condition for the 'if statement'
#     3. check if a 'string' ISN@T part of the car name available
#         4. instead of IN use NOT in

# we are going to input a car name and check if the STRING 'bmw' is NOT in the input entered by the user.
#     1. if 'bmw' IS NOT in the car name, then we print 'sorry....'
# To check the strings as caseless (not taking in capital or lower case) ==>>.casefold()

if "bmw" not in carName.casefold():
    print("Sorry we do not have that car")
else:
    print("your {} is ready for you".format(carName))