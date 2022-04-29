import sys
from class_card_generation import Card
from barrel_generation import barrel_generation
from design_themes import printing_space


def main_game(quantity_players):
    checklist = []
    player = []
    looser = []
    looser_count = 0

    for count_name in range(1, quantity_players + 1, 1):
        name = input(f'Введите имя игрока {count_name}: ')
        checklist.append(name)

    printing_space(50)
    print('*' * 50)
    print('              Начинаем ИГРУ ЛОТО')
    print('*' * 50)

    #генерируем игровые карточки игроков

    for count_card in range(quantity_players):
        player.append(count_card)
        player[count_card] = Card()
        player[count_card].card_generation_class()
    # выводим список игроков
    print('*' * 50)
    print('              Начинаем ИГРУ ЛОТО')
    print('                \033[91m\033[1mВ игре участвуют:\033[0;0m')
    for count_players in range(quantity_players):
        print(f'{count_players + 1}. \033[91m\033[1m{checklist[count_players]}\033[0;0m')
    print('*' * 50)

    #пошаговая игра
    step = 1
    while step < 91:
        #вывод количества оставшихся бочат
        print('*' * 50)
        print(f'             В мешке  {91 - step} бочат')
        print('*' * 50)
        printing_space(1)
        #генерация боченка. Один боченок на всех игроков. при
        game_digit = barrel_generation()
        #начало цикла опроса одного игрока
        for count in range(quantity_players):
            #проверка на отсутсвие игрока в списке проигравших
            if count not in looser:
                #распечатываем карточку игрока
                print(f'\033[91m\033[1mКарточка ИГРОКА {checklist[count]}\033[0;0m')
                print('-' * 20)
                print(*player[count].new_card[0:27:3])
                print(*player[count].new_card[1:27:3])
                print(*player[count].new_card[2:27:3])
                print('-' * 20)
                #выводим боченок
                print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
                #выводим имя игрока
                print(f'ИГРОК {checklist[count]}')
                #вызов диалога и выбора ответа
                answer1 = player[count].player_answer_class()
                #анализ ответа. 4 варианта ответа: 2 правильных да/да нет/нет и два ошибочных нет/да да/нет
                if game_digit in player[count].new_card and answer1 == 'y':
                    for count1 in range(27):
                        if game_digit == player[count].new_card[count1]:
                            player[count].new_card[count1] = 'x'

                    print(f'\033[92m\033[1mВерно! {checklist[count]}, такое число есть!\033[0;0m')
                    print('*' * 50)
                    printing_space(1)

                elif game_digit not in player[count].new_card and answer1 == 'n':

                    print(f'\033[92m\033[1mВерно! {checklist[count]}, такого числа нет! Продолжаем игру. \033[0;0m')
                    print('*' * 50)
                    printing_space(1)

                elif answer1 == 'n' and game_digit in player[count].new_card:
                    print(f'\033[91m\033[1mСтоп игра! {checklist[count]}, Вы проиграли! Такое число есть! \033[0;0m')
                    print('*' * 50)
                    printing_space(1)
                    # looser.append(count)
                    looser_count += 1

                elif answer1 == 'y' and game_digit not in player[count].new_card:
                    print(f'\033[91m\033[1mСтоп игра! {checklist[count]}, Вы проиграли! Такого числа нет!\033[0;0m')
                    print('*' * 50)
                    printing_space(1)
                    looser.append(count)
                    looser_count += 1

                if looser_count == quantity_players:
                    print(f'\033[95m\033[1mИгра окончена! Победивших нет!\033[0m')
                    sys.exit(0)

                #проверка на зачеркивание всех чисел в карточке
                end_of_game = 0
                for count_x in player[count].new_card:
                    if count_x == 'x':
                        end_of_game += 1

                if end_of_game == 15:
                    print(f'\033[95m\033[1mИгра окончена! {checklist[count]}, Вы победили!\033[0m')
                    sys.exit(0)
        step += 1
