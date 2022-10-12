# b) Подумайте как наделить бота ""интеллектом""

import random
candies = 2021
comp = 0
motion = random.randint(1,2)
if motion==1:
    print("Первым ходит игрок!")
    while candies > 0:
        print(f"Всего осталось конфен: {candies}!")
        number = int(input('Сколько конфет от 1 до 28 вы заберете? : '))
        while number < 0 or number > 28:
            number = int(input('Не жульничайте!!! Нужно забрать от 1 до 28 конфет! : '))
        candies -= number
        if candies<1:
            print('Поздравляем!!! Вы победили!!!')
            break
        print(f"Всего осталось конфен: {candies}!")
        if candies <= 85 and candies >= 58:
            comp = candies-29*2
        elif candies <= 57 and candies >= 30:
            comp = candies-29
        elif candies < 29:
            comp = candies
        else:
            comp = random.randint(1,28)
        print(f"Компьютер забрал конфет: {comp}!")
        candies = candies - comp
        if candies<1:
            print('Сожалею!!! Вы проиграли!!!')
            break   
else:
    print("Первым ходит компьютер!")
    while candies > 0:
        print(f"Всего осталось конфен: {candies}!")
        if candies <= 85 and candies >= 58:
            comp = candies-29*2
        elif candies <= 57 and candies >= 30:
            comp = candies-29
        elif candies < 29:
            comp = candies
        else:
            comp = random.randint(1,28)
        print(f"Компьютер забрал конфет: {comp}!")
        candies = candies - comp
        if candies<1:
            print('Сожалею!!! Вы проиграли!!!')
            break        
        print(f"Всего осталось конфен: {candies}!")
        number = int(input('Сколько конфет от 1 до 28 вы заберете? : '))
        while number < 0 or number > 28:
            number = int(input('Не жульничайте!!! Нужно забрать от 1 до 28 конфет! : '))
        candies -= number
        if candies<1:
            print('Поздравляем!!! Вы победили!!!')
            break