# BMI Calculator
name1 = "YR"
height_m1 = 2
weight_kg1 = 90

name2 = "YR's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YR's brother"
height_m3 = 2.5
weight_kg3 = 160


# this function will take 3 arguments/INPUTS
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)  # it will print the bmi of a given person
    if bmi < 25:
        return name + " is not overweight"  # this will return 'so so' is not overweight
    else:
        return name + " is overweight"


result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)

# The following function converts miles to kilometers
km = 1.6 * miles


def convert(miles):
    return 1.6 * miles


print(convert(20))
