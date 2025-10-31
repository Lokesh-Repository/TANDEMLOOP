a = float(input("Enter first No: "))
b = float(input("Enter second No: "))
symbol = input("Enter Symbol of Operation (+,-,*,/): ")

class Operations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "The Numberator Cannot be 0"
        else:
            return a/b

if symbol == "+":
    print("Result:", int(Operations().add(a, b)))
elif symbol == "-":
    print("Result:", int(Operations().subtract(a, b)))
elif symbol == "*":
    print("Result:", int(Operations().multiply(a, b)))
elif symbol == "/":
    print("Result:", int(Operations().divide(a, b)))
else:
    print("Invalid operation")
