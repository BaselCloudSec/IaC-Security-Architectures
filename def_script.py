def addition(num1, num2=0):
    print(num1 + num2)

addition(2, 3)



def registration(username=False, password=False, emil=False):
    if username and emil and password :
       print("Registration Successful")
    else :
        print("Registration Failed")


registration(username = "john",emil = "bb@gmail.com", password= 6666)
