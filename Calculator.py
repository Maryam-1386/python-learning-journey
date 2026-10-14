def Addition(a, b):
    return a + b

def Subtraction(a, b):
    return a - b

def Multiplication(a, b):
    return a * b

def Division(a, b):
    if b == 0:
        return "error: b can not 0"
    return a / b

def Exponentiation(a, b):
    return a ** b

while True:
    print("choos one number:\n 1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponentiation\n6.Exit\n")
    
    try:
        choice = int(input())
        
        if choice == 6:
            print("Exit")
            break
        
        if 1 <= choice <= 5:
            a = float(input("number 1: "))
            b = float(input("number 2: "))
            
            if choice == 1:
                result = Addition(a, b)
                print(f"resulte: {a} + {b} = {result}")
            elif choice == 2:
                result = Subtraction(a, b)
                print(f"resulte: {a} - {b} = {result}")
            elif choice == 3:
                result = Multiplication(a, b)
                print(f"resulte: {a} * {b} = {result}")
            elif choice == 4:
                result = Division(a, b)
                print(f"result: {a} ÷ {b} = {result}")
            elif choice == 5:
                result = Exponentiation(a, b)
                print(f"result: {a} ^ {b} = {result}")
        else:
            print("please enter number bittwen 1 and 6")
            
    except ValueError:
        print("error:pleas number valiuable ")
    except Exception as e:
        print(f"Unexpected error:{e}")