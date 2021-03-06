"""Testing github and repl integration features to better understand version control."""
from art import logo

#calculator

# add function
def add(num1, num2):
    return num1 + num2

# subtract function
def subtract(num1, num2):
    return num1 - num2

# multiply function
def multiply(num1, num2):
    return num1 * num2

# divide function
def divide(num1, num2):
    if num2 == 0:
        return "undefined"
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    continue_calculating = True
    print(logo)
    num1 = float(input("\nWhat is the first number?: " ))

    while continue_calculating:
        print("")
        for symbol in operations:
            print(symbol)
        operator = input(f"\nChoose an operation to perform on {num1}: " )
        num2 = float(input("\nWhat is the next number?: "))

        calculate = operations[operator]
        answer = calculate(num1, num2)
        print(f"\n{num1} {operator} {num2} is {answer}.")

        keep_going = input("\nDo you want to continue calculating with this number? \n(Y/N, or S to start a new calculation): ").lower()
        if keep_going == "n":
            continue_calculating = False
            print("T%erminating program.")
        elif keep_going == "s":
            continue_calculating = False
            print("")
            calculator()
        elif keep_going != "y" and keep_going != "n":
            continue_calculating = False
            print("There was an error in your answers, and the program is terminating.")
        else:
            num1 = answer

calculator()