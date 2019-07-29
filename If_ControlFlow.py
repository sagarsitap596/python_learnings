# name=input("Please enter you name : ")
# age= int(input("Hey {0}!, how old are you ? ".format(name)))
#
# print(" {0} is {1} years old".format(name,age))


inputData = int(input("Please enter a number between 1 t0 10 : \n"))

print("you entered {0}".format(inputData))

if inputData != 5:
    if inputData > 5:
        inputData = int(input("please enter smaller number :"))
    else:
        inputData = int(input("Please enter greater number :"))

    if inputData != 5:
        print("you have guessed wrong number")
        print("Better luck next time")
    else:
        print("Bingo!!, you guessed right number")
else:
    print("Great , you guessed in first time.")


