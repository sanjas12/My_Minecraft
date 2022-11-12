import random
import time

MAX_NUMBER = 100

my_name = input("Введи своё имя:")
print (f"Hi, {my_name}")
time.sleep(1)
print (f"Let's start to mathematica!")
sign_list = ["+", "-"]
all_sample, right_solved, inccorect = 0, 0, 0
time.sleep(1)


while True:
    first_number = random.randint(1, MAX_NUMBER)
    second_number = random.randint(1, MAX_NUMBER)
    sign = random.choice(sign_list)
    if second_number > first_number:
        continue

    
    if sign == "+":
        answer_calc = int(first_number) + int(second_number)
    else:
        answer_calc = int(first_number) - int(second_number)
    
    sample =f"{first_number} {sign} {second_number} = "
    answer = input(sample)
 
    if answer == "q":
        print(f"Всего примеров:{all_sample}")
        print(f"Правильно решено:{right_solved}")
        print(f"Не правильно решено:{all_sample - right_solved}")
        print(f"By, {my_name}!!!!!!")

        exit() 


    if int(answer) == answer_calc:
        right_solved += 1
        all_sample += 1
    else:
        inccorect += 1
        all_sample += 1
