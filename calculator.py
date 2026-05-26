while True:

    print("Type stop to exit")

    a = input("Enter your number: ")

    if a == "stop":
        break

    try:
        a = float(a)
    except:
        print("Enter only valid numbers")
        continue


    b = input("Enter your next number: ")

    if b == "stop":
        break

    try:
        b = float(b)
    except:
        print("Enter only valid numbers")
        continue


    op = input("Enter operation (+,-,*,/,%): ")

    if op == "stop":
        break

    if op == "+":
        print(a + b)

    elif op == "-":
        print(a - b)

    elif op == "*":
        print(a * b)

    elif op == "/":

        if b == 0:
            print("Not divisible by zero")
            continue

        print(a / b)

    elif op == "%":
        print(a % b)

    else:
        print("Operator isn't available")