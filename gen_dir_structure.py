#Generates all 52 folders needed for the exercises in the book. 
#if you want to delete all folders again, run the command "rm -rf exc_*")
#All content in that folders will also be gone. 

import os

for num in range (0, 53):
  os.system("mkdir exc_" + str(num))
