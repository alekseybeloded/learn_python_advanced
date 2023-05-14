from random import randint

human_list = []
ai_list = []

print('1|2|3')
print('=====')
print('4|5|6')
print('=====')
print('7|8|9')
first_move = input('Выше изображена игральная доска с номерами возможных ходов. Сделайте свой ход - введите значение от 1 до 9\n')
first_move = int(first_move)
human_list.append(first_move)

while True:
    first_move_ai = randint(1, 9)
    if first_move_ai != first_move:
        break
    else:
        continue

ai_list.append(first_move_ai)