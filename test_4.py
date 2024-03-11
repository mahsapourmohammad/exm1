choice=input("enter choice('f','c'):")
if choice=='f':
    c=float(input("enter c:"))
    f=(1.8*c)+32
    print(f)
if choice=='c':
    f=float(input("enter f:"))
    c=(f-32)/1.8
    print(c)



