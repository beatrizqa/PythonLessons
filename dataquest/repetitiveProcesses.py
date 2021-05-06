row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

'''
we have a list [3, 5, 1, 2] assigned to a variable ratings, and we want to repeat the following process:
==>>    for each element in ratings, print that element:
'''
ratings = [3, 5, 1, 2]
for element in ratings: # for each element in ratings, print that element
    print(element)

# extract the last element for each list in app_data_set
app_data_set = [row_1, row_2, row_3, row_4, row_5]

for each_list in app_data_set:
    rating = each_list[-1]
    print(rating)

'''
For Loops
    1.  for .... in ..... ==>> for some_variable in some_list:
'''
a_list = [1, 3, 5]

for value in a_list:
    print(value)

# Outside the loop body can interact with the code inside the loop body

a_sum = 0
for value in a_list:
    a_sum = a_sum + value
    print(a_sum)

'''
Compute the average app rating for the apps stored in the app_data_set variable.
    1. Initialize a variable named rating_sum with a value of zero outside the loop body.
    2. Loop (iterate) over the app_data_set list of lists. For each of the five iterations of the loop (for each row in app_data_set):
        1. Extract the rating of the app and store it to a variable named rating. The rating is the last element of each row.
        2. Add the value stored in rating to the current value of the rating_sum.
    3. Outside the loop body, divide the rating sum (stored in rating_sum) by the number of ratings to get an average value.
    4. Store the result in a variable named avg_rating
'''
rating_sum = 0
for row in app_data_set:
    rating = row[-1]
    rating_sum = rating_sum + rating
    print(rating_sum)
    
avg_rating = rating_sum / len(app_data_set) # also avg_rating = rating_sum / 5