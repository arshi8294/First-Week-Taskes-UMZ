# (C) = (F - 32) / 1.8

print("1-Celcius to Farenhiet", "2-Farenhiet to Celcius", "---------------------" , sep="\n")

direction = int(input("Select one of directions to convert : "))

while direction not in [1, 2]:
    print("Direction not found")
    direction = int(input("Select one of directions of convert : "))

print("-------------------------------")
userInput = float(input("Enter degree : "))
if direction == 1:
    Farenhiet = (userInput*1.8) + 32
    print(f"{userInput} C = {Farenhiet} F")
else :
    Celcius = (userInput - 32)/1.8
    print(f"{userInput} F = {Celcius} C")
print("-------------------------------")

