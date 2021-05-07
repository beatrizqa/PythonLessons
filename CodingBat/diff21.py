'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
    diff21(19) → 2
    diff21(10) → 11
    diff21(21) → 0
'''
def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2
print(diff21(6))  # output = 15
print(diff21(30))  # output = 18 (difference is 8 and because n > 21 you multiply 9 by 2)