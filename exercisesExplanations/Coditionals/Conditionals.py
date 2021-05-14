devs_money = 100
dev_can_play_smash = False

if devs_money > 10 and dev_can_play_smash: #if devs_money is bigger than 10 and if dev_can_play_smash = True (but because dcps = False it wont print this statement)
    print("Dev enters a smash tornament!")
elif devs_money < 1 and dev_can_play_smash: # elif statement, so that if the previous conditional is False as well as devs_money is less than 1 and dev_can_play_smash
                                            # is True the program will print "Dev is too poor to enter"
    print("Dev is too poor to enter")
else:
    print("Dev just can't play smash") # if all the previous conditionals have been False we execute the else statement.