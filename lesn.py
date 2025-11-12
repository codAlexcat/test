import random
print("Привет теперь у тебя есть Visual Studio code! \nДавай разомнем мозги, сыграем в игру, тебе нужно будет решать примерчики")
point = 3
quantity = 0
not_quantity = 0
while point > 0:
    num1 = random.randint(-100, 100)
    num2 = random.randint(-100, 100)
    answer = num1 + num2
    answer_user = int(input(f"{num1} + {num2} = "))
    if answer_user == answer:
        point += 1
        quantity += 1
    elif answer_user != answer:
        point -= 1
        not_quantity += 1

print("Вы проиграли так как ващи очки закончились!")
if quantity % 10 == 1 and quantity % 100 != 11:
    print(f"Вы решили {quantity} пример правельно")
elif 2 <= quantity % 10 <= 4 and (quantity % 100 < 10 or quantity % 100 > 20):
    print(f"Вы решили {quantity} примера правельно")
else:
    print(f"Вы решили {quantity} примеров правельно")

if not_quantity % 10 == 1 and not_quantity % 100 != 11:
    print(f"Вы решили {not_quantity} пример неправельно")
elif 2 <= not_quantity % 10 <= 4 and (not_quantity % 100 < 10 or not_quantity % 100 > 20):
    print(f"Вы решили {not_quantity} примера неправельно")
else:
    print(f"Вы решили {not_quantity} примеров неправельно")

