bankAccount = {"Account owner" : "Arshia Amoozad", "Account ID" : "1234567", "Account balance" : 100 }

commands = [0, 1, 2, 3]

print("---Welcome to your Bank Account---")

while True:
    
    print("Choose which service you want to use :")
    command = int(input("1-Account balance \n2-Cash withdrawal \n3-Deposit cash \n0-Quit \n"))
    

    while command not in commands:
        print("Invalid input. Please choose carefully.")
        print("Choose which service you want to use :")
        command = int(input("1-Account balance \n2-Withdrawal money \n3-Deposit cash \n0-Quit \n"))

    if command == 0:
        print("Thank you for choosing us")
        break

    elif command == 1 :
        print("-----------------------------------------------------")
        print(f"Account ID : {bankAccount['Account ID']}\nAccount owner : {bankAccount['Account owner']}\nAccount balance : {bankAccount['Account balance']}$")
        print("-----------------------------------------------------")


    elif command == 2:
        print("-----------------------------------------------------")
        
        amount = float(input("Enter your desired amount to withdrawal : "))

        if amount > bankAccount["Account balance"]:
            print("Your account balance is insufficient")
    
        else :
            bankAccount["Account balance"] -= amount
            print(f"Operation done sucssesfully\nYour account balance is {bankAccount["Account balance"]}")
        print("-----------------------------------------------------")
        
    
    else :
        print("-----------------------------------------------------")
        amount = float(input("Enter your desired amount to deposit : "))
        bankAccount["Account balance"] += amount
        print("Operation done sucssesfully", f"Your account balance is {bankAccount["Account balance"]}")
        print("-----------------------------------------------------")
    
    end = int(input("Do you want to continue? \n1-Yes\n0-No  \n"))
    if not end:
        print("Thank you for choosing us")
        break
    


        



    
