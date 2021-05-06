'''
1. Assign the string Pandora - Music & Radio to a variable named app_name.
2. Assign the string 4.0 to a variable named average_rating. Make sure you don't mistake a string for a float.
3. Assign the string 1724546 to a variable named total_ratings. Make sure you don't mistake a string for an integer.
4. Assign the string free to a variable named price.
5. Display the app_name variable using print()
'''
app_name = "Pandora - Music & Radio"
average_rating = str("4.0")
total_ratings = str("1724546")
price = "free"

print(app_name)

# The \ character has a special function within a string: it escapes (cancels) the special function of characters.

# + operator
# Concatenation = The process of linking two or more strings together.
print('a' + 'b')  #ab
print('a' + ' ' + 'b') # a b
print('This' + 'is' + 'a' + 'sentence.') # Thisisasentence.
print('This' + ' ' + 'is' + ' ' + 'a' + ' ' + 'sentence.') # This is a sentence.
print('This ' + 'is ' + 'a ' + 'sentence.') # This is a sentence.

'''
 concatenate a string with one or more copies of itself using the * operator, followed 
 by a number which specifies the number of times the string has to be multiplied
 '''
print('a' * 2)  # aa
print ('a' * 5) # aaaaa
print ('a ' * 3) # a a a
print ('a' * 0) # no output
print ('a' * -1) # no output

# Can write strings over many lines using the triple quotation mark symbol (''' or """).
text_1 = '''This is a sentence.
this is another sentence, on a different line.
Yet another sentence'''

text_2 = """ -----------------
Line 1.
Line 2.
Line 3. """

print(text_1)
print(text_2)

'''
1. Assign the string Facebook's rating is to a variable named facebook.
2. Assign the float 3.5 to a variable named fb_rating.
3. Convert fb_rating from a float to a string using the str() command, and assign the converted value to a new variable named fb_rating_str.
4. Concatenate the strings stored in facebook and fb_rating_str to form the string Facebook's rating is 3.5.
5. Assign the concatenated string to a variable named fb.
6. Display the fb variable using print()
'''
facebook = '''Facebook's rating is'''
fb_rating = 3.5
fb_rating_str = str(fb_rating)
fb = facebook + ' ' + fb_rating_str
print(fb)