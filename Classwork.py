# KEY: Add comments!

def main():
    problem1()
    # problem2()
def problem1():
    x = 0
    while 1 == 1:
        userInput = input("Enter a number to add: ")
        if userInput.lower() == "q":
            print(x)
            break
        elif int(userInput) >= 0 or int(userInput) < 0:
            x += int(userInput)



# KEY: See README for expected results. This should return a dictionary
def problem2():
    use1 = number1()
    use2 = number2()
    def do_the_math():
        aTotal = add(use1, use2)
        sTotal = sub(use1, use2)
        mTotal = mul(use1, use2)
        dTotal = div(use1, use2)
        print("Here are your results for", use1, "and", use2)
        print("The SUM result is", aTotal)
        print("The DIFFERENCE result is", sTotal)
        print("The PRODUCT result is", mTotal)
        print("The DIVISION result is", dTotal)
    do_the_math()





def number1():
    num1 = int(input("Enter 1st number: "))
    return num1

def number2():
    num2 = int(input("Enter 2nd number: "))
    return num2

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


if __name__ == '__main__':
    main()