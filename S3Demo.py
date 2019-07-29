import boto3
import botocore
import _thread
import re



def getList():
    print("file read started...")
    dataList=set()
    dataFile=open('resource/dummy.log','r')

    for line in dataFile:
        dataList.add(line.strip())

    return dataList

def keyVlidator(key):

    s3 = boto3.resource('s3')

    try:

        s3.Object('here-congestion-artifacts', key).load()
        print("{} found".format(key))
    except botocore.exceptions.ClientError as e:
         if e.response['Error']['Code'] == "404":
             print("{} not found".format(key))
         else:
             print("Somthing else has gone wrong")





if __name__ == '__main__':
    myList = getList()
    dataFile=open("resource/s3_key_nf.txt","w")
    dataFile.truncate()
    for key in myList:
        print(key[27:-37])
        key=key[27:-37]+"\n"
        dataFile.write(key)

    print("----END----")