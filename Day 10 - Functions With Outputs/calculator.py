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

first_number = int(input("What's the first number?: "))

operation_list = ["+", "-", "*", "/"]

for operation in operation_list:
    print(operation)

chosen_operation = input("Pick an operation: ")




