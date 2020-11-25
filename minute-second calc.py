import os
os.system("color 05")
x = 1
op = 1
y = float("60")
def sec(x, y):
    return x * y
def mins(x, y):
    return x / y

def calc(x, op, y):
    while True:
        print("                             ")
        print("1.Minutes -> Seconds")
        print("2.Seconds -> Minutes")
        op = input("1/2: ")
        if op in ("1", "2",):
            x = input("Int: ")

            try:
                x = float(x)

                if op == "1":
                    print(x, "converted to seconds is ", sec(x, y))
                elif op == "2":
                    print(x, "converted to minutes is ", mins(x, y))
            except ValueError:
                print("Invalid Input")
calc(x, op, y)
