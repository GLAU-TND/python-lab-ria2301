class MyException(Exception):
    def __init__(self , v):
        self.v = v
    def __str__(self):
        return self.v



def Xyz(a,b):
    sum=0
    sum=a+b
    if sum<150:
        raise MyException("Custom Exception Occured")
    else:
        print(sum)

a = int(input())
b=int(input())
Xyz(a,b)

