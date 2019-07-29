

fileName = "resource/data.txt"
# eventSet=set()
# with open(fileName,'r') as events:
#     for data in events:
#         eventSet.add(data.lstrip())


# eventList=[]
# with open(fileName,'r') as events:
#     data=events.readline()
#     eventList.append(data)
#     if "</Reason>" not in data:
#         data=events.readline()
#         while "</Reason>" not in data:
#             eventList.append(data)
#
#         eventList.append(data)
#
#
# eventMap=dict()
# with open(fileName,'r') as eventData:
#     for line in eventData:
#         key=line.split(",")[1]
#         value=line.split(",")[0]
#         if eventMap.__contains__(key):
#             eventMap[key].add(value)
#         else:
#             eventMap[key]=set([value])
#
#
# for type in eventMap:
#     print("{0} --> {1} ".format(type,eventMap[type]))



#
# even_numbers = []
# n= 0
# while( n <= 100):
#   if(n % 2 == 0):
#     even_numbers.append(n)
#
# print(even_numbers)


l = []
map = {"asd": "asdadd"}

print(map.keys().__contains__("asd"))
# print(map.values().for)
