# Create a variable with name types_of_people, the variable holds an integer value of 10. 
types_of_people = 10

# Create a variable (x), in that variable we store the formatted string of: "There are 10 types of people."
# The string only gets formatted since we're creating it with a f(ormat) flag. 
x = f"There are {types_of_people} types of people."

# Create a variable (binary) that holds the value/string 'binary'.
binary = "binary"

# Create a variable (do_not) that holds the value/string 'don't'.
do_not = "don't"

# Create a variable (y), in that, store the following formatted string:
# "Those who know binary and those who don't."
y = f"Those who know {binary} and those who {do_not}."

# Print variable x. 
print(x)

# Print variable y.
print(y)

# Print "I said:", then print the complete variable x.
print(f"I said: {x}")
# Print "I said:", then print the complete variable y.
print(F"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)