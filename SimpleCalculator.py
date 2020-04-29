def add(a ,b):
    res = print("Addition = ", a + b)
    return res

def sub(a, b):
    res = print("Substraction = ", a - b)
    return res

def mul(a, b):
    res = print("Multiplication = ", a * b)
    return res

def div(a, b):
    res = print("Division = ", a / b)
    return res

def mod(a, b):
    res = print("Mudulo = ", a % b)
    return res

print("Enter first number: ")
a = int(input())
print("Enter second number: ")
b = int(input())

print("First Number = ", a)
print("Second Number = ", b)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulo")
print("6. Perform all operations")
print("Choose any option by entering it's number: ")
c = int(input())

print("Here is the result:")


if c == 1:
    add(a, b)
elif c == 2:
    sub(a, b)
elif c == 3:
    mul(a, b)
elif c == 4:
    div(a, b)
elif c == 5:
    mod(a, b)
elif c == 6:
    add(a, b)
    sub(a, b)
    mul(a, b)
    div(a, b)
    mod(a, b)
else: print("You didn't chose a right number from the list")
