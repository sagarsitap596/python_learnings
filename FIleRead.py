
fileName="resource/sample.txt"

jabber = open(fileName,'r')

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()

# with open(fileName, 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')
#
# with open(fileName, 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open(fileName, 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')
#

# with open(fileName, 'r') as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines[::-1]:
#     print(line, end='')

with open(fileName, 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
