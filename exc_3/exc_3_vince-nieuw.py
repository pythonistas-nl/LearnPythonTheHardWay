"""
Author: Vince-Nieuw
Version: 2.0
Comment: Rewritten for use with floats.
"""

# Prints a single line of text. 
print("I will now count my chickens:" )

# Print the string "Hens" , then prints the result of 25 + (30 / 6) . 
# Python respects the order of  mathematical calculation as we know it. 
print("Hens", 25.0 + 30.0 / 6.0) 

# Prints the string "Roosters", then prints the result of 100 - (25 * 3 % 4). 
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0 )

# Prints the below sentence.
print(" Now I will count the eggs:")
#
# Prints only the sentence. Does NOT actually calculate anything here. 
print("Is it true that (3.0 + 2.0 ) < ( 5.0 - 7.0 )")
#
# The actual calculation is done below. The result is printed on a new line. 
print( 3.0 + 2.0 < 5.0 - 7.0 ) 
#
# Prints the string "What is 3 + 2?". It then prints the outcome of the sum. 
# This is initiated by the calculation we provide after the comma.
print("What is 3 + 2?" , 3.0 + 2.0) 

# Same as previous line. 
print(" What is 5 - 7?", 5.0 - 7.0)

# Prints the sentence "Oh, that's why it's False." 

# Prints the sentence "How about some more".
print("How about some more.")

# Prints the sentence "Is it greater" , then prints "True" on the same line. This is because it is true that 5 > -2.
print("Is it greater" , 5.0 > -2.0)

# Here they added the '='  sign in the comparison. This means that if the number is equal, it is also true.
# Try it:
"""
3 > 3  ---> Will be false
3 >= 3  --> Will be true.
"""

# Explanation provided in above docstring.
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)



