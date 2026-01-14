
def chooseNumber():

    num = input("choose a number between 1 and 10: ")
    num = int(num)

    if num < 1 or num > 10:
        raise ValueError("please choose a number between 1 and 10")
    else :
        print("your number is : " + str(num))

chooseNumber()
