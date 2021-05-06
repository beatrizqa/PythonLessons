# “do each”, “do every”, “for all”, “process each”, “do ___ times”, ...



'''
Questions to ask yourself before creating a loop:
1. What is the sequence?
2. What descriptive name can I give to the loop variable?
3. Write the for loop heading. 
4. With this decided, you no longer need to think about the whole program at once: You can focus on what you do for one element, 
   with the name you gave in the loop heading.
5. What do I need to do for a single element of the sequence? Does this involve other variables? If so, how will I initialize them? 
6. Write this action into the body of the loop, using the loop variable.
7. Does the main action involve a variable, other than the loop variable, that needs to change each time through the loop? If so, 
   how do I relate the present and next values, and change the value to be ready for the next time through the loop? 
8. Writing the sequence for a specific example may help. 
9. Finally, code this update.
'''
items = ['red', 'orange', 'yellow', 'green']
number = 1                                   
for item in items:   # print numbered entries
    print(number, item)                      
    number = number + 1   # crucial added line

''' use a function to number the entries in any list'''

def numberList(items):
    '''Print each item in a list items, numbered in order.'''
    number = 1
    for item in items:
        print(number, item)
        number = number + 1

def main():
    numberList(['red', 'orange', 'yellow', 'green']) # function in line 9. 'items' (line 9) = 'red, yellow, orange, green' (line 17)
    print()
    numberList(['apples', 'pears', 'bananas']) #  function in line 9. 'items' (line 9) = 'apples, pears, bananas' (line 19)
# "numberList function" (line 9 with the for loop) is called twice in 'main' with different items

main()

#ACCUMULATION LOOPS
def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum
print(sumList([5, 2, 4, 7, 10, 20]))
    
    