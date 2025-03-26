import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = { "+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
}
def calculator():
    print(art.logo)
    n1 = float(input("What is the first number?\n"))
    calc_continue = True
    while calc_continue:
        for key in calc_dict:
            print(key)
        operation = input("Pick an operation.\n")
        n2 = float(input("What is the second number?\n"))
        equals = calc_dict[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {equals}")
        repeat = input(f"Type 'y' to continue calculating with {equals}, or type 'n' to start a new calculation:").lower()
        if repeat == "y":
            n1 = equals
        else:
            calc_continue = False
            print("\n" * 20)
            calculator()
calculator()
