
try :
    a = 12
    s = "hello"
    print(a+s)
except Exception as ExceptionA:
    print(" TypeError : unsupported operand type :a is not a string ")
    a = str(a)
finally:
    print(a+s)
