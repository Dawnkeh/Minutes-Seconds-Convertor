import os
os.system("color 05")
x = 1
op = 1
dp = 1
def stm(x):
    return x / 60
def sth(x):
    return x / 3600
def std(x):
    return x / 3600 / 24
def stw(x):
    return x / 3600 / 24 / 7
def mts(x):
    return x * 60
def mth(x):
    return x / 60
def mtd(x):
    return x / 60 / 24
def mtw(x):
    return x / 60 / 24 / 7
def hts(x):
    return x * 3600
def htm(x):
    return x * 60
def htd(x):
    return x / 24
def htw(x):
    return x / 24 / 7
def dts(x):
    return x * 24 * 60 * 60
def dtm(x):
    return x * 24 * 60
def dth(x):
    return x * 24
def dtw(x):
    return x / 7
def wts(x):
    return x * 7 * 24 * 3600
def wtm(x):
    return x * 7 * 24 * 60
def wth(x):
    return x * 7 * 24
def wtd(x): 
    return x * 7


def calc(x, op, dp):
    while True:
        print("                             ")
        print("There Will be 2 inputs, X to Y")
        print("1.Seconds")
        print("2.Minutes")
        print("3.Hours")
        print("4.Days")
        print("5.Weeks")
        op = input("1|2|3|4|5 X: ")
        dp = input("1|2|3|4|5 Y: ")
        if op in ("1", "2", "3", "4", "5"):

            if dp in ("1", "2", "3", "4", "5"):
                try:
                    x = input("Value of X: ")
                    x = float(x)
                    if op == "1" and dp == "1":
                        print("I think you already know the answer to that question is ", x)
                    elif op == "1" and dp == "2":
                        print(x, " Converted to Minute is ", stm(x))
                    elif op == "1" and dp == "3":
                        print(x, " Converted to Hour is ", sth(x))
                    elif op == "1" and dp == "4":
                        print(x, " Converted to Day is ", std(x))
                    elif op == "1" and dp == "5":
                        print(x, " Converted to Week is ", stw(x))
                    elif op == "2" and dp == "1":
                        print(x, " Converted to Second is ", mts(x))
                    elif op == "2" and dp == "2":
                        print("I think you already know the answer to that question is ", x)
                    elif op == "2" and dp == "3":
                        print(x, " Converted to Hour is ", mth(x))
                    elif op == "2" and dp == "4":
                        print(x, " Converted to Day is ", mtd(x))
                    elif op == "2" and dp == "5":
                        print(x, " Converted to Week is ", mtw(x))
                    elif op == "3" and dp == "1":
                        print(x, " Converted to Second is ", hts(x))
                    elif op == "3" and dp == "2":
                        print(x, " Converted to Minute is ", htm(x))
                    elif op == "3" and dp == "3":
                        print("I think you already know the answer to that question is ", x)
                    elif op == "3" and dp == "4":
                        print(x, " Converted to Day is ", htd(x))
                    elif op == "3" and dp == "5": 
                        print(x, " Converted to Week is ", htw(x))
                    elif op == "4" and dp == "1":
                        print(x, " Converted to Second is ", dts(x))
                    elif op == "4" and dp == "2":
                        print(x, " Converted to Minute is ", dtm(x))
                    elif op == "4" and dp == "3":
                        print(x, " Converted to Hour is ", dth(x))
                    elif op == "4" and dp == "4":
                        print("I think you already know the answer to that question is ", x)
                    elif op == "4" and dp == "5":
                        print(x, " Converted to Week is ", dtw(x))
                    elif op == "5" and dp == "1":
                        print(x, " Converted to Second is ", wts(x))
                    elif op == "5" and dp == "2":
                        print(x, " Converted to Minute is ", wtm(x))
                    elif op == "5" and dp == "3":
                        print(x, " Converted to Hour is ", wth(x))
                    elif op == "5" and dp == "4":
                        print(x, " Converted to Day is ", wtd(x))
                    elif op == "5" and dp == "5":
                        print("I think you already know the answer to that question is ", x)
                except ValueError:
                    print("Invalid Input")        
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
calc(x, op, dp)
