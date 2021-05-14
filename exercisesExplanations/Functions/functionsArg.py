'''PASSING ARGUMENTS TO A FUNCTION
                def helloFunc():
                    return "Hello Function."
    1. create parameters within the parentheses ()
        1. we want to customise the greeting that our function returns
        2. we create a parameter called 'greeting' inside the ()
        3. now in our function we will return a string where we will use our greeting instead of 
            our 'Hello Function'
                def helloFunc(greeting):
                    return "{} Function.".format(greeing)
                print (helloFunc("Hi"))  ===>>> this will return 'Hi Function.'    
    2. This greeting parameter is a required argument because it does not have a default value
        1. If we had a default value then it would just fall back to the default value whenever
            we did not pass that argument in
        2. EXAMPLE:
            1. we also want to pass a name to our 'helloFunc'
            2. this will return a greeting and a return
            3. in our def helloFunc(greeting, name = 'You'): we add a new parameter called name
            4. if we do not have a name we want the name to be default to 'YOU'
            5. RETURN will change because we need to add the parameter 'name' to it
                         return "{}, {}.".format(greeing, name)
            6. The function below will return a 'Hi, You' because we did not entered a value for name
                        def helloFunc(greeting):
                                return "{} Function.".format(greeing)
                            print (helloFunc("Hi"))
            7. {} in return are 'place holders' '''

# EXAMPLE
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]
