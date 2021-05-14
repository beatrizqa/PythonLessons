# METHODS
#     1. provide the functionality of what customers can do or what we can do with customers
#     2. CONSTRACTOR (Initializer):
#         1. It is a method
#         2. It is a section of code that it is executed whenever we create a new customer
#     3. to create a method you use the name and () ==>> 'Customer()'
#     4. variables defined in a method we are creating are known as PARAMETERS (name, membershipType)
#     5. the values assigned to the parameters are ARGUMENTS (Caleb, Gold)
# STATIC METHODS
# 1. Methods that are not attached to any individuak object but instead are invoked on the class itself
# STR METHOD
#     1. def __str__(self):
#         1. this will be invoked anytime we try to convert a customer to a string
#         2. it needs to return something (return self.name + " " + self.membershipType)

class Customer:
    def __init__(self, name, membershipType):
        self.name = name
        self.membershipType = membershipType

    def updateMembership(self, newMembership):
        self.membershipType = newMembership

    def __str__(self):
        # print("converting to string") this was just to show the function works
        return self.name + " " + self.membershipType

    def printAllCustomers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):  # 'Other' refers to what we are comparing our customer to. This will see
        # if 2 customers are equal
        # if you are comparing 2 customers and they have the same name and the
        # same membership type, you can assume they are the same customer and returns
        # TRUE
        # Any attributes we are comparing will need to be defined in the __init__ method
        if self.name == other.name and self.membershipType == other.membershipType:
            return True
        return False


customers = [Customer("Caleb", "Gold"),
             Customer("Brad", "Bronze")]

print(customers[0] == customers[1])

# it will print the customers defined in 33 & 34
Customer.printAllCustomers(customers)
# print(customers[1])  # this is for the __str__ method
# customers[1].updateMembership("Gold")
# print(customers[1].membershipType)
