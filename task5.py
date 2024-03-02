import turtle

Raph = turtle.Turtle()
window = turtle.Screen()


while True:

    try:
        clr = input("Choose color of pen : ")
        Raph.color(clr)

    except Exception as error :
        print("Please enter color carefully")
    
    else:
        break

while True:
    try:
        lenRaph = float(input("Enter length of square : "))
    except Exception as error:
        print(error)
    else:
        break

for i in range (4):
    Raph.forward(lenRaph)
    Raph.right(90)
window.mainloop()