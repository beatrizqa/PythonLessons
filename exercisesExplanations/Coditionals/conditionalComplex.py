temperature = int(input("How hot is your memory card? "))

if temperature < 20 or temperature > 70:
    print("Soooooooooooooooooorry, you can't play!")
    
else:
    print("Great, you can continue playing your game")



# if temperature >= 20 and temperature <= 70:
#     print("Great, you can continue playing your game")
# else:
#     print("Soooooooooooooooooorry, you can't play!")


# Program that takes input from a user playing a game on a pc.
#     1. User has to guess the temperature of the memory card
#         1. if it is between 20 and 70, it works ok
#         2. outside that range, the memory card does not work properly
#     2. if the temperature is more than or equal to 20 AND it is less than or equal to 70 it means that both conditions are true 
#         and the whole statement is true so we print continue playing
#     3. if one of them is false, it means we cannot continue playing 

'''
'AND' TRUTH TABLE
        true        false
true    TRUE        FALSE
false   FALSE       FALSE
'''
'''
'OR' TRUTH TABLE
        true        false
true    TRUE        TRUE
false   TRUE       FALSE
'''

