
name=input("Enter name")
age=int(input("Hey {} , Whats your age?".format(name)))


if age not in range (18,31):
   print ("Age not valid for holidays")
else:
    print("Hey {} , you can go on a holiday ".format(name))
