
try :
    a = 12
    s = "hello"
    print(a+s)
except Exception as ExceptionA:
    print(" a is not a string !!! ")
    a = str(a)
finally:
    print(a+s)
