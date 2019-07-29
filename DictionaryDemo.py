studentMap={11:"sagar",22:"shyam",33:"ram"}
print(studentMap)
print("-"*40)

#add new entry
studentMap[44]="Tom"
print(studentMap)
print("-"*40)


#delete entry
print("deleting ",studentMap[11]," from studenMap")
del studentMap[11]
print(studentMap)
print("-"*40)

#get value for given key
print(studentMap.get(22))
print("-"*40)


#update existing key if present or add
studentMap[44]="updated Tom"
studentMap.update({33:"ram2",55:"got"})
print(studentMap)
print("-"*40)

#get length
print(len(studentMap))
print("-"*40)

#keys
print(studentMap.keys())
print("-"*40)

#values
print(studentMap.values())
print("-"*40)

#iterate 1
for id in studentMap:
    print(id,"----"+studentMap[id])

print("-"*40)

#iterator 2 -- sorted
for id in sorted(studentMap.keys()):
    print(id,"----"+studentMap[id])


print("+"*30)
area = { 'living' : [400, 450], 'living' : [650, 800], 'kitchen' : [300, 250], 'garage' : [250, 0]}
print(area['living'])

