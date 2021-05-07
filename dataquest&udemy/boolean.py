hair = "Blond"
height = 1.80
evil = True
# these above characteristics we will compare them with the IF STATEMENT. 
# IF STATEMENT will print different outcomes depending on meeting or not all those characteristics

if hair == "Blond" and height > 1.60 or not evil:
    print("You must be Skywalker")
else:
    print("Run!!!!!!!!!!!!!!!!!!! It's Darth Vader")

# It returns ELSE because:
#     1. The hair must be 'Blond' and we have it as 'Black'.
#     2. The height must be over 1.60 which it is true as height = 1.80
#     3. the evil condition must be false (meaning it is not evil)
# Even if we changed 'hair' from 'Black' to 'Blond' 
#   1. it will still run ELSE as the third condition (not evil) is false
# If we change the hair to 'blond' and 'AND not evil' to 'OR not evil' 
#   1. it will take the condition as TRUE because one of the conditions is met 
# AND has a higher precedence over OR (so it reads AND expression first and then the OR expression)