def add(a ,b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

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
    print("Addition = ", add(a,b))
elif c == 2:
    print("Substraction = ", sub(a,b))
elif c == 3:
    print("Multiplication = ", mul(a,b))
elif c == 4:
    print("Division = ", div(a,b))
elif c == 5:
    print("Mudulo = ", mod(a,b))
elif c == 6:
    print("Addition = ", add(a,b))
    print("Substraction = ", sub(a,b))
    print("Multiplication = ", mul(a,b))
    print("Division = ", div(a,b))
    print("Mudulo = ", mod(a,b))
else: print("You didn't chose a right number from the list")
