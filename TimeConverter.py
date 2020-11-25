import os
os.system("color 05")
x = 1
op = 1
y = float("60")
z = float("24")
q = float("7")
def tsec(x, y):
    return x * y
def tmins(x, y):
    return x / y
def tdays(x, z):
    return x / z
def tweeks(x, q):
    return x / q
def fdays(x, z):
    return x * z
def fweeks(x, q):
    return x * q


def calc(x, op):
    while True:
        print("                             ")
        print("1.Seconds -> Minutes")
        print("1.Seconds <- Minutes")
        print("3.Minutes -> Hours")
        print("4.Minutes <- Hours")
        print("5.Hours -> Days")
        print("6.Hours <- Days")
        print("7.Days -> Weeks")
        print("8.Days <- Weeks")
        op = input("1/2/3/4/5/6/7/8: ")
        if op in ("1", "2", "3", "4", "5", "6", "7", "8"):
            x = input("Int: ")

            try:
                x = float(x)

                if op == "2":
                    print(x, "converted to seconds is", tsec(x, y))
                elif op == "1":
                    print(x, "converted to minutes is", tmins(x, y))
                elif op == "3":
                    print(x, "converted to hours is", tmins(x, y))
                elif op == "4":
                    print(x, "converted to minutes is", tsec(x, y))
                elif op == "5":
                    print(x, "converted to days is", tdays(x, z))
                elif op == "6":
                    print(x, "converted to hours is", fdays(x, z))
                elif op == "7":
                    print(x, "converted to weeks is", tweeks(x,q))
                elif op == "8":
                    print(x, "converted to days is", fweeks(x, q))
            except ValueError:
                print("Invalid Input")
calc(x, op)
