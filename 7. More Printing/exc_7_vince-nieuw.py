print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("."* 10) # what'd that do? --> It'll print 10x a dot. 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ' ) 
print(end7 + end8 + end9 + end10 + end11 + end12)

"""
This exercise is kind of tricky since it tricks you into believing that end is just another variable that we're setting.
In fact, end in a print fucnction is a parameter (-> an option we can provide to Python's print statement).
End defines how the print statement is closed. By default, it inserts a newline. 

Try it:
"""
print('########') 
#exc 1
print("a first print statement.")
print("a second print statement on a new line.")

#exc 2
print("a first print statement.", end=" But, this is not ")
print("a second print statement on a new line.")