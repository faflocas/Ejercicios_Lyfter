def get_menu(counter):
    print("The calculator is currently: ")
    print(counter)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    choice = input("Choose an option: ")
    return choice


def get_number():
    try:
        number = float(input("Enter a number: ")) 
        return number
    except ValueError:
        print("Wrong input, enter a valid number ")
        return 0


def addition(counter):
    number = get_number()
    counter += number 
    return counter


def subtraction(counter):
    number = get_number()
    counter -= number 
    return counter


def multiplication(counter):
    number = get_number()
    counter *= number 
    return counter

def division(counter):
    number = get_number()
    if number == 0:
        print("Cannot divide by 0")
        return counter
    else:
        counter /= number 
        return counter

def main():
    counter = 0
    while True:
        choice = get_menu(counter)
        if choice == "1":
            counter = addition(counter)
        elif choice == "2":
            counter = subtraction(counter)
        elif choice == "3":
            counter = multiplication(counter)
        elif choice == "4":
            counter = division(counter)
        elif choice == "5":
            counter = 0
        else:
            print("Enter a valid option")


main()