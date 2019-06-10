types_of_people = 10 #define the number of people
x = f"There are {types_of_people} types of people" #function of how many people (1)
binary = "binary" #defines variable binary as "binary"
do_not = "don't" #defines don't and do not
y = f"Those who know {binary} and those who {do_not}" # (2)
print(x) #prints X
print(y) #printsy y
print(f"I said: {x}") #prints I said X (3)
print(f"I also said: '{y}'") #prints I said Y (4)
hilarious = False #defines hilarious as false
joke_evaluation = "Isn't that joke so funny?! {}" #defines joke evaluation as string
print(joke_evaluation.format(hilarious)) #using the string and the hilarious format into the {} (5)

w = "This is the left side of..." #left side of the string
e = "a string with a right side" #right side of the string
print(w + e) #adding two strings together
