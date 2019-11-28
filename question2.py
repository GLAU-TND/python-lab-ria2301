try:
    a=int(input("enter a number"))+input()
    a.count()
except AttributeError:
    print("Attribute error handled")
except TypeError:
    print("Type error handled ")
except ValueError:
    print("Value error handled")
