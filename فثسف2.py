import random
import string

while True:
    user_password = input("Enter password: ")

    if len(user_password) != 8:
        print("Password must be 8 characters.")
    else:
        characters = string.punctuation
        digits = string.digits
        letters = string.ascii_letters
        words = string.ascii_lowercase + string.ascii_uppercase

        print("conditions must be met.")

        password = ""
        for i in range(8):
            password += random.choice(password)
        
        break
