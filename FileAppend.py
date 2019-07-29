

with open("resource/dataAppend.txt","a") as dataFile:
    dataFile.writelines("\n")

    for i in range(1,11):

        for j in range(0,11):

            print("{0} times {1} is {2}".format(j,i,i*j),file=dataFile)

        print("="*40,file=dataFile)