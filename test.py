import random
import string



user_pasword=input("enter pass:")

if len(user_pasword)==8:

    if user_pasword:
        characters=string.punctuation  #علائم نگارشی
        digits=string.digits        #عدد صحیح
        leters=string.ascii_letters  
        words=string.ascii_lowercase and string.ascii_uppercase #حروف کوچیک و بزرگ
        pasword = digits+characters+leters+words

        print("the pass is correct ")

    else:
        print("conditions must be met")

else:
    print("pass must be 8 characters")
   
pasword=" "

for i in range(8):
    pasword += ''.join(random.choice(pasword))
print(pasword)
