bankAccount = {"Account owner" : "Arshia Amoozad", "Account ID" : "1234567", "Account balance" : 100 }

commands = [0, 1, 2, 3]

while True:
    
    print("---Welcome to your Bank Account---")
    print("Choose which service you want to use :")
    command = int(input("1-Account balance \n2-Cash withdrawal \n3-Deposit cash \n0-Quit \n"))
    

    while command not in commands:
        print("Invalid input. Please choose carefully.")
        print("Choose which service you want to use :")
        command = int(input("1-Account balance \n2-Cash withdrawal \n3-Deposit cash \n0-Quit \n"))

    if command == 0:
        break
    
    
