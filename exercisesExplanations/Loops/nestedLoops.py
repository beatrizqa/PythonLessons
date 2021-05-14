# NESTED LOOPS:
#     1. it is a loop inside another

''' EXERCISE
    1. create a loop for each week in a range of 4 weeks
    2. print out 'week' with the number of the week in each line 
    3. inside this loop, create another loop with 7 days range
    4. print out each day in a new line
    5. After each week print ------- * 15 '''

for week in range(1, 4):  # this will have 3 weeks
    # with each week passing it prints the no of the week
    print("Week : {}".format(week))
    for day in range(1, 8):  # inside each week it'll print 7 days
        print("\tDay : {}".format(day))
    print("*" * 15)

''' EXERCISE 2: MULTIPLICATION TABLE
    1. use nested loops to print out the multiplication table from 1 to 9
'''
print("Multiplication Tables")
for i in range(1, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, i*j))
    print("-" * 30)
