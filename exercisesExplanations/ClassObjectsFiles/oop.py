#  OOP ==>> helps us to represent things in our code
#     1. How do we represent data in our code?
#         1. With simple variable types:
#             1. 5
#             2. "Hello"
#             3. [5, "hello"]
#         2. with more complex types:
#             1. oop
#     2. Allows us to represent data as a one-to-one relationship to business problems
#     3. 2 main things in OOP:
#         1. Classes ==>>
#             1. represent something such as a 'customer'
#             2. by creating classes we can group things in logical units
#         2. Objects ==>>
#             1. specific examples of that 'customer'
#             2. objects have specific values (the name and other details for that customer)
#      4. Atributes provide the data and the values we need to store about a customer
#      5. METHODS provide the functionality of what customers can do or what we can do with customers
# class = customer
#     attribute 1 = name
#     attribute 2 = membership type
# OBJECT 1
#     Caleb
#     Gold
# OBJECT 2
#     Brad
#     Bronze

# CLASSES
#     1. Create a class ('customer)
#     2. give it attributes ('name', 'membership type')

class Customer:  # within the class you define the attributes
    def __init__(self, name, memershipType):
        # everytime we create a customer this function will be invoke
        # every code we want to use everytime a customer is created we put it in this function
        # 'self' refers to whatever customer we are creating
        # any attributes you want to define you put them in ()self.name

        self.name = name
        self.memershipType = memershipType
        # inside the body of the function we take the attributes in () and assign them to that customer
        # 'self.name' ==>> we are referring to whatever customer is being created
        # print("Customer created") ==>> In the init function we do not use the print function


# Outside the class we create a variable 'c' and we assign the value 'Customer()'
# this is how we create a new customer, but we have to pass some parameters from the
# function above
c = Customer("Caleb", "Gold")
print(c.name, c.memershipType)

c2 = Customer("Brad", "Bronze")
print(c2.name, c2.memershipType)

# Way to create customers with LISTS
customers = [Customer("Caleb", "Gold"), Customer("Brad", "Bronze")]
print(customers[0].name)  # '0' is Caleb's details,
