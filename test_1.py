x = input("Enter input: ")
try:
    float(x)
    if "." in x:
        print(x)
        print("type x:float")
    else:
        print(x)
        print("type x:int")
except:
    if x[0]=='[' and x[-1]==']' in x:
        print(x)
        print("type x:list")
    else:
        print(x)
        print("type x:string")