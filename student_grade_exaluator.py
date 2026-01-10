score = input("what is your score?")
score = int(score)
absence = input("what is your absence?")
absence = int(absence)

if score > 90 and absence < 10 :
    print("you are exellent.")
elif score < 90 or absence < 10 or 12 > 6:
    print("you are good.")
else :
    print("you are bad.")
