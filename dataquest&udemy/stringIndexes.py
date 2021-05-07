# 'POSITIVE' INDEXES ==>> []
#     1. indexing starts at zero
#     2. indexing from the end starts in -1

#                    1        2
#          01234567890123456789012345
message = "Python is a great language"
print(message[0]) # ==>> prints 'P'
print(message[14]) # ==>> prints 'e' in 'great'
print(message[22]) # ==>> prints 'u'
print()

# CHALLENGE
#     1. use this message to print out another message
#     2. "you are hot" using the indexes of the original string message

print(message[1])
print(message[4])
print(message[22])
print(message[10])
print(message[13])
print(message[14])
print(message[3])
print(message[4])
print(message[2])
print()

# NEGATIVE INDEXES
# Do the same exercise with negative indexes
print(message[-25])
print(message[-22])
print(message[-4])
print()
print(message[-3])
print(message[-13])
print(message[-1])
print()
print(message[-23])
print(message[-22])
print(message[-10])

# SLICING
#   1. Up to but NOT INCLUDING
#   2. Print out the word language using 2 methods

print(message[18:])
print(message[-8:])
print(message[18:26])
print(message[:18] + message[18:])

# STEP
print(message[0:17:2])  # ==>> Pto saget
print(message[0:17:3])  # ==>> Ph  ga







