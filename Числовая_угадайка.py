import random
import time

# выбор случайного числа из диапазона
n = random.randint(1, 100)

# Приветствие
print('Добро пожаловать в числовую угадайку')
time.sleep(1.2)
print('Загадано некое число из диапазона от 1 до 100')
time.sleep(1.2)
print('Попробуйте отгадать его')
time.sleep(1.2)


def is_valid(num):
    if num.isdigit() and int(num) in range(1, 101):
        return True
    else:
        return False

count = 1
while True:
    num = input('Введите число от 1 до 100:  ')
    if is_valid(num):
        num = int(num)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if num < n:
        print('ВАШЕ число МЕНЬШЕ загаданного, попробуйте еще разок')
        count += 1
    elif num > n:
        print('ВАШЕ число БОЛЬШЕ загаданного, попробуйте еще разок')
        count += 1
    elif num == n:
        print('Вы угадали c', count, 'раза, поздравляем!')
        time.sleep(1.2)
        play_again = input('Желаете сыграть еще раз? Да(Y), Нет(N):  ')
        if play_again.lower() == 'y':
            n = random.randint(1, 100)
            count = 1
            continue
        else:
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
