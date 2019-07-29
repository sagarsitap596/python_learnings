
class MyException(Exception):
    # def __init__(self,message):
    #     super().__init__(message)
    pass


try:
    num1=10
    num2=0
    print(num1/num2)
except FloatingPointError:
    print(" FloatingPointError :Cannot divide by zero")
except ZeroDivisionError:
    print(" ZeroDivisionError :Cannot divide by zero")
    raise MyException(" - Cannot divide by zero. ")
except BaseException:
    print(" BaseException :Cannot divide by zero")
