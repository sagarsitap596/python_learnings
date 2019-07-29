
#create empty list two ways
list1=[]
list2=list()

names=["aa","bb","cc","dd","dd"]
print(names)

#Added new value
names.append("ee")
print(names)

#delete value
del names[1]

#find count
names.count("dd")


#insert at specific position
names.insert(0,"zz")
print(names)

#get value at index
print(names[3])



lettesr_list=list("Welcome to python")
print(lettesr_list)


menu=[]
menu.append(["food1","food2"])
menu.append(["food1","food3"])
menu.append(["food5","food3","food4"])
menu.append("foo10")


for meal in menu:
    if "food1" not in meal:
        print(meal)


book_list=["book1","book2","book3","book4","book5"]

book_itr=iter(book_list)

for book in range(0,len(book_list)):
    print(next(book_itr))

print("+"*30)

List_1=[2,6,7,8]
List_2=[2,6,7,8]
print(List_1[-2])
print(List_2[2])
print(List_1[-2] + List_2[2])

print("="*80)

# define a list
my_list = [4, 7, 0, 3]

# get an iterator using iter()
my_iter = iter(my_list)

for item in my_iter:
    print(item)

print("="*80)
list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three']

test = zip(list1, list2)  # zip the values

testList = list(test)

a, b = zip( *testList )
print('The first list was ', list(a));
print('The second list was ', list(b));
