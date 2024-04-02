balance=0
while True:
    print("1.depsit")                #واریزی
    print("2.whithdraw")             #برداشت
    print("3.check balance")         #موجودی
    print("4.exit")
    choice=input("enter choice(1/2/3/4):")
    if choice=='1':
       amount=float(input("enter amount to deposit:"))
       balance+=amount
       print("credited amount your acount:",balance)
    elif choice=='2':
       amount=float(input("enter amount to whithdraw:"))
       if amount>balance:
        print("insufficient inventory.")
       else:
        balance-=amount
        print("deducted amount from your account:",balance)
    elif choice=='3':
      print("your account balance:",balance)
    elif choice=='4':
      print("exiting the bank acount system.")

      break
