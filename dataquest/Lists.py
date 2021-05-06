# we can store data more efficiently using lists.

row_1 = ['Facebook', 0.0, 'USD', 25458445, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

print(row_1)
type(row_1)
print(row_2)
print(row_3)

# To find the length of a list, we can use the len() command
print(len(row_1))
list_1 = [1, 6, 0]
list_2 = []
print(len(list_1))
print(len(list_2))

# difference & average
difference = row_2[4] - row_1[4]
average_rating = (row_1[4] + row_2[4]) / 2
print(difference)
print(average_rating)

rating_1 = row_1[3]
rating_2 = row_2[3]
rating_3 = row_3[3]

total = rating_1 + rating_2 + rating_3
average = total / 3
print(total)
print(average)

fb_rating_data = [row_1[0], row_1[3], row_1[-1]]
insta_rating_data = [row_2[0], row_2[3], row_2[-1]]
pandora_rating_data = [row_5[0], row_5[3], row_5[-1]]

avg_rating = (fb_rating_data[1] + insta_rating_data[1] + pandora_rating_data[1]) / 3

print(avg_rating)

'''
list slicing ==>> When we selected the first three elements, we sliced a part of the list
    To retrieve any list slice we want:
        1. We first need to identify the first and the last element of the slice.
        2. We then need to identify the index numbers of the first and the last element of the slice.
        3. Finally we can retrieve the list slice we want by using the syntax a_list[m:n], where:
            1. m represents the index number of the first element of the slice; and
            2. n represents the index number of the last element of the slice plus one 
            (if the last element has the index number 2, then n will be 3, if the last element 
            has the index number 4, then n will be 5, and so on).
    Shortcuts
        1. a_list[:x] when we want to select the first x elements.
        2. a_list[-x:] when we want to select the last x elements.
        '''

first_4_fb = row_1[:4]
last_3_fb = row_1[-3:]
pandora_3_4 = row_5[2:4]

#LISTS OF LISTS
#we retrieved 3.5 in two steps:
#   1. we first retrieved data_set[0]
#   2.we retrieved fb_row[-1]

data_set = [row_1, row_2, row_3, row_4, row_5]
print(data_set)

fb_row = data_set[0]
print(fb_row)
fb_rating = fb_row[-1]
print(fb_rating)

#to retrieve the same value of 3.5 by chaining the two indices ([0] and [-1]):

print(data_set[0][-1])

avg_rating = (app_data_set[0][-1] + app_data_set[1][-1] + app_data_set[2][-1] + app_data_set[3][-1]
+ app_data_set[4][-1]) / 5
