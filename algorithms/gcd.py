
def calculateGCD(a,b):

    remainder=None
    print("Calculating GCD for {} {}".format(a,b))

    while(b>0):

        remainder=a%b
        a=b
        b=remainder

    print("GCD is {}".format(a))

    

def main():
        calculateGCD(5,12)

if __name__ == '__main__':
    main()
