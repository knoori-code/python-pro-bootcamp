def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# multiply 4 * 8
# print(operations_dictionary["*"](4, 8))

def calculator():
    first_number = float(input("What's the first number?: "))
    continue_game = True

    while continue_game:
        for symbol in operations_dictionary:
            print(symbol)

        chosen_operation = input("Pick an operation: ")
        second_number = float(input("What's the next number: "))

        calculated_result = operations_dictionary[chosen_operation](first_number, second_number)
        print(f"{first_number} {chosen_operation} {second_number} = {calculated_result}")

        choice = input(f"Type 'y' to continue calculating with {calculated_result}, or type 'n' to continue with a new calculation: ").lower()
        if choice == "y":
            first_number = calculated_result
        else:
            continue_game = False
            print("\n" * 20)
            calculator()

calculator()