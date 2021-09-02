"""
1 stone = 6.3503 kg
1 pound = 0.4540 kg
1 feet  = 30.48 cm
1 inch  = 2.54 cm
"""

"""
This program converts stones and pounds to kg, feet and inches to cm
and also converts cm to meters then finally returns a BMI value.
"""


# Weight stones to kg
weight_stones = float(input("Weight in stones: "))
weight_stones_kg = weight_stones * 6.3503 # converting stones to kg

# Weight extra pounds to kg
extra_pounds = float(input("Extra pounds: "))
extra_pounds_kg = extra_pounds * 0.4540 # converting pounds to kg

# Weight feet to cm
height_feet = float(input("Height in feet: "))
height_feet_cm = height_feet * 30.48 # converting feet to cm


# Weight extra inches to cm
extra_inches = float(input("Extra inches: "))
extra_inches_cm = extra_inches * 2.54 # converting inches to cm

kg = weight_stones_kg + extra_pounds_kg
cm = height_feet_cm + extra_inches_cm
bmi = kg / (cm/100)**2 # divide by 100 to get meters

print("kg: ", round(kg, 1))
print("cm: ", round(cm, 1))
print("BMI: ", round(bmi, 1))

