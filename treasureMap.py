# 🚨 Don't change the code below 👇
row1 = ["⬜️", "️⬜️", "️⬜️"]
row2 = ["⬜️", "⬜️", "️⬜️"]
row3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

output = []

myStr = position
print("The input string is:", myStr)
for character in myStr:
    output.append(character)


output1 = int(output[0])
output2 = int(output[1])


if output2 == 1:
    x = row1[output1-1] = "X"

elif output2 == 2:
    x = row2[output1-1] = "X"

elif output2 == 3:
    x = row3[output1-1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
