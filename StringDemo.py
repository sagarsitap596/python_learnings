print("Hello sagar , welcome to pythod. Explore , learn and evolve!!!")

# Using strings

name="sagar mahadev sitap"

address="mumbai"

#string append
contactPerson=name+" "+address

print(contactPerson)

#String replace
name.replace("sagar","Mr.Sagar")

print(name)

# string
# index of m
print(" index of m = ",name.index("m"))

#last index of  " "
print("last index of space is = ",name.rindex(" "))
print("last index of space is = ",name.rfind(" "))

#first index of  " "
print("last index of space is = ",name.find(" "))


# get first name
print(name[:name.index(" ")])

#get middle name
print(name[name.index(" ")+1:name.rindex(" ")])

#get last name
print(name[name.rindex(" ")+1:len(name)])

#repeating word/char of string
repeated=name+" "*3
print(repeated)




