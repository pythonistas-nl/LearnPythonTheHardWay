name = 'Vincent Nieuwenburg'
age = 128 # definitely a lie
height = 89 # inches
weight = 183 # lbs
eyes = 'Green'
teeth = 'White'
hair = 'Blonde'
height_cm = height * 2.54
weight_kg = weight * 0.453592

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall, that's {height_cm} centimeters.")
print(f"He's {weight} pounds heavy, that's {weight_kg} kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")