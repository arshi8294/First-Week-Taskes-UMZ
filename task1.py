def isList(x:str):
    if "," in x:
        return True
    return False
    

def isFloat(x:str):
    dataBase = [str(i) for i in range(10)]
    dataBase.append(".")
    for i in x:
        if i in dataBase:
            pass
        else:
            return False
    return True


def isInt(x:str):
    dataBase = [str(i) for i in range(10)]
    for i in x:
        if i in dataBase:
            pass
        else:
            return False
    return True

userInput = input("Enter your data : ")

if isList(userInput):
    lst = userInput.split(",")
    lst = [i.strip() for i in lst]
    print(f"Your input is list items and it equals to : {lst} ")
elif isInt(userInput): 
    iNum = int(userInput)
    print(f"Your input is an integer number and it equals to : {iNum}")
elif isFloat(userInput):
    fNum = float(userInput)
    print(f"Your input is a float number and it equals to : {fNum}")
else :
    print(f"Your input is a normal string and it equals to : {userInput}")

