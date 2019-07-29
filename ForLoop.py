
# {:50} will add space as per number present in {}. Eg. in below code 50 spaces are appended
# for i in range(-1,5):
#    print(" Number {} squared is {} and cube is {:50}".format(i,i**2,i**3))
#    print(" calculation completed!!")

# print("Operation completed successfully.")

data = ('hi i am sagar mahadev sitap hi i am sagar mahadev sitap hi i am sagar mahadev sitap' 
        ' hi i am sagar mahadev sitap hi i am sagar mahadev sitap hi i am sagar mahadev sitap ')

for i in range(10):
    print(i)


asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]

d='0'
for asteroid in asteroids:
    if asteroid == 9617:
        print("Grahamchapman")
    elif asteroid == 9618:
        print("Johncleese")
    elif asteroid == 9619:
        print("Terrygilliam")
        d='1'
        break
    elif asteroid == 9620:
        print("Ericidle")
    elif asteroid == 9621:
        print("Michaelpalin")
    else:
        print("Terryjones")
if d == '1':
    print("MontyPython")