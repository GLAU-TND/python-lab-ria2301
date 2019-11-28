class MyException:
    def __init__(self , v):
        self.v = v
        print(self.v)



def Xyz(a,b):
    sum=0
    try:
        sum=a+b
        if sum<150:
            raise MyException("Custom Exception Occured")
        else:
            print(sum)
    except:
            pass
    


a = int(input())
b=int(input())
Xyz(a,b)

