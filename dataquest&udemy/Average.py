# to open the file AppleStore.csv and transform it into a list of lists:

'''
opened_file = open('AppleStore.csv') ==>> this opens the file
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file) ==>> converts the file in a list of lists
'''

'''
Compute the average app rating for all the 7,197 apps stored in the data set.
    1. Initialize a variable named rating_sum with a value of zero.
    2. Loop through the apps_data[1:] list of lists (make sure you don't include the header row). For each of the 7,197 iterations of the loop (for each row in apps_data[1:]):
        1. Extract the rating of the app and store it to a variable named rating (the rating has the index number 7). Make sure you convert the rating value from a string to a float using the float() command.
        2. Add the value stored in rating to the current value of the rating_sum.
        3. Divide the rating sum (stored in rating_sum) by the number of ratings to get an average value. Store the result in a variable named avg_rating
'''
rating_sum = 0
for row in apps_data[1:]:
    rating = float(row[7])
    rating_sum = rating_sum + rating
avg_rating = rating_sum / len(apps_data[1:])

print(avg_rating)  # it does not work because it cannot open the 'Applestore.csv' file



