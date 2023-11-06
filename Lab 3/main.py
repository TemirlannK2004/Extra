def sum():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    return x+y

def subtraction():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    return x-y

def multiplication():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    return x*y

def divide():
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    return x/y

def fib(x):
    return fib(x-1)+fib(x-2) if x>2 else 1


def main(option)-> int:
    match option:
        case 1:
            print('Result:',sum())
        case 2:
            print('Result:',subtraction())
        case 3:
            print('Result:',multiplication)
        case 4:
            print('Result:',divide())
        case 5:
            x = int(input('Enter number: '))
            print('Result:',fib(x))  
        case 6:
            print('Bye!')
            return False
        case _:
            print('Invalid credentials. Try Again!')

while True:
    options = [1,2,3,4,5,6,7]
    print('\nOptions:')
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Fibonacci")
    print("6. Exit")
    user_choice = int(input('Choose option : '))

    if main(user_choice)==False:
        break            
    



#Another approach
while True:
    options = [1,2,3,4,5,6,7]
    print('\nOptions:')
    print("1. Sum")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Fibonacci")
    print("6. Exit")

    user_choice = int(input('Choose option : '))

    if (user_choice not in options) and user_choice != type(int):
        print('Invalid credentials,try again')

    if user_choice==6:
        print('Bye!')
        break

    elif user_choice==1:
        print('Sum: x + y')
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('Result:' ,sum(x,y))

    elif user_choice==2:
        print('Subtraction: x - y')
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('Result:' ,subtraction(x,y))
    
    elif user_choice==3:
        print('Multiplication x * y')
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('Result:' , multiplication(x,y))

    elif user_choice==4:
        print('Devide: x / y')
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        print('Result:' , divide(x,y))

    elif user_choice==5:
        x = int(input('Enter first number: '))
        print('Result:',fib(x))

                

