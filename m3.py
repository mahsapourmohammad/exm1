import random
import time
import string

def calculate_magic_numbers(start,end):
    
    x=0.3
    x=x*((end-start)+start)
    print(x)
calculate_magic_numbers(1,20)


def exam_numbers(random_bin):
    return int(random_bin, 2)

correct_answers=0
wrong_answers=0

print("you only have 20 seconds for enter decimal num")

start_time = time.perf_counter()
random_bin = "{:04b}".format(random.randint(0,10))
while True:
    if correct_answers > 0:

        random_bin = "{:04b}".format(random.randint(0,10))

    x_input =int( input(f"Enter the decimal num of {random_bin}: "))

    if x_input== exam_numbers( random_bin):
        correct_answers+=1
        print("Correct(:")
    else:
        wrong_answers+=1
        print("Wrong!")
    end_time=time.perf_counter()
    if end_time - start_time >=20:
        break
    else :
        print("Number of correct answers:", correct_answers)
        print("Number of wrong answers:", wrong_answers)

user_password = input("Enter password: ")
while True:
    
    if len(user_password) != 8:
        print("Password must be 8 characters.")
    elif user_password:
        characters = string.punctuation
        digits = string.digits
        words = string.ascii_lowercase + string.ascii_uppercase

        print("the pass is correct.")

        break
    else:
        print("conditions must be met.")

        break