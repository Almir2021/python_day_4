# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
numberOfBankers = len(names)
ranndomInteger = random.randint(0, numberOfBankers-1)

nameDetermined = names[ranndomInteger]
print(f"{nameDetermined} is going to buy the meal today!")
