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

first_number = float(input("What's the first number?: "))

operation_list = ["+", "-", "*", "/"]

for operation in operation_list:
    print(operation)

chosen_operation = input("Pick an operation: ")
second_number = float(input("What's the next number: "))

calculated_result = operations_dictionary[chosen_operation](first_number, second_number)
print(f"{first_number} {chosen_operation} {second_number} = {calculated_result}")

continue_game = input(f"Type 'y' to continue calculating with {calculated_result}, or type 'n' to continue with a new calculation: ")