


###### using write method

# dataFile=open("resource/dataWrite.txt","w")
# for i in range(1,11):
#
#     for j in range(0,11):
#
#         dataFile.write("{0} times {1} is {2} \n".format(j,i,i*j))
#
#     dataFile.write("="*40)
#
# dataFile.close()

##### using writelines method

# dataFile=open("resource/dataWrite.txt","w")
# listOfString=[]
# for i in range(1,11):
#
#     for j in range(0,11):
#
#         listOfString.append("{0} times {1} is {2}".format(j,i,i*j))
#
#     listOfString.append("="*40)
#
# dataFile.writelines("\n".join(listOfString))
# dataFile.close()

#### using print with file attribute
with open("resource/dataWrite.txt","w") as dataFile:

    for i in range(1,11):

        for j in range(0,11):

            print("{0} times {1} is {2}".format(j,i,i*j),file=dataFile)

        print("="*40,file=dataFile)