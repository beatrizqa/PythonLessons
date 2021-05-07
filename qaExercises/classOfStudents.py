'''.git\class Dog:
    energy = "high"

    def speak(self):
        print("woof")

bilbo_waggins = Dog()
print(bilbo_waggins.energy)
bilbo_waggins.speak()
'''
class Students:
    #class_ = "student"
    def __init__(self, name, age, class_ = "student"):
        self.name = name
        self.age = age
        self.class_ = class_
    
    def avgtestscore(self):
        testscore = [85, 70, 99]
        avgtestscore = testscore[0:3] / 3
        print(avgtestscore)
        
Antonio = Students("Antonio", 24)
Maria = Students("Maria", 55)
Pablo = Students("Pablo", 23)

print(getattr(Maria, "class_"))




