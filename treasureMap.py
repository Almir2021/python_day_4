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
print("The output is:", output)

output1 = int(output[0])
output2 = int(output[1])

if output1 == 1:
    row1[output1-1] = output[0]
elif output1 == 2:
    row2[output1-1] = output[0]
elif output1 == 3:
    row3[output1-1] = output[0]
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
print(map)
