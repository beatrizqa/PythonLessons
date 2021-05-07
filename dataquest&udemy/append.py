# APPEND COMMAND
# LIST 1
a_list = [1, 2]
a_list.append(3)
print(a_list)

# LIST 2
empty_list = []
empty_list.append(12)
print(empty_list)

# APPEND LIST 1 & 2
list_1 = []
list_2 = [5, 's', 1]

list_1.append('data')
list_2.append(1.6)

print(list_1)
print(list_2)

#EXAMPLE 1
''' 
1. We initialize an empty list.
2. We start looping over our data set and extract the ratings.
3. We append the ratings to the empty list we created at step one.
4. Once we have all the ratings, we:
    1. use the sum() command to sum up all the ratings (to be able to use sum(), we'll need to store the ratings as floats or integers); and then
    2. we divide the sum by the number of ratings (which we can get using the len() command).
'''
row_1 = ['Facebook', 0.0, 'USD', 25458445, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

app_data_set = [row_1, row_2, row_3, row_4, row_5]

ratings = [] # Initialize an empty list.
for row in app_data_set:
    rating = row[-1]  # start looping over our data set and extract the ratings.
    ratings.append(rating)  #We append the ratings to the empty list we created at step one.
print(ratings)

avg_rating = sum(ratings) / len(ratings) # use the sum() command to sum up all the ratings;
                                         # we divide the sum by the number of ratings

print(avg_rating)

# EXAMPLE 2
'''
compute the average app rating for all of the 7,197 apps stored in our data set.
    1. Initialize an empty list named all_ratings.
    2. Loop through the apps_data[1:] list of lists (make sure you don't include the header row). 
       For each of the 7,197 iterations of the loop:
            1. Extract the rating of the app and store it to a variable named rating (the rating has the index 
               number 7). Make sure you convert the rating value from a string to a float.
            2. Append the value stored in rating to the list all_ratings.
    3. Compute the sum of all ratings using the sum() command.
    4. Divide the sum of all ratings by the number of ratings, and assign the result to a variable named avg_rating
'''
all_ratings = []

for row in app_data_set[1:]:
    rating = float(row[7])
    all_ratings.append(rating)

avg_rating = sum(all_ratings) / len(all_ratings) # it won't work in here because 'Applestore.csv' file doesn't exist



