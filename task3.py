
lst_operators = ["sum", "difference", "multiple", "divide"]
operation = input(f"Enter an operator from {lst_operators} : ")

while operation not in lst_operators :
    print("Invalid operator. Please insert operator again.")
    operation = input(f"Enter an operator from {lst_operators} : ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if operation == 'sum':
    print("a + b = " , num1 + num2)
elif operation == 'difference':
    print("a - b = " , num1 - num2)
elif operation == 'multiple':
    print("a * b = " , num1 * num2)
elif operation == 'divide':
    print("a / b = " , num1 / num2)
else:
    print("Numbers couldn't be divided by zero")
