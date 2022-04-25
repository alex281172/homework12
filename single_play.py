import sys
from card_generation import card_generation
from player_answer import player_answer
from design_themes import printing_space
from barrel_generation import barrel_generation


def play_for_one():

    #вызов функции генерации карточки лото

    new_card = card_generation()
    step = 1
    while step < 91:
        print('*' * 50)
        print(f'                В мешке  {91 - step} бочат')
        print('*' * 50)
        printing_space(1)

        print('-' * 20)
        print(*new_card[0:27:3])
        print(*new_card[1:27:3])
        print(*new_card[2:27:3])
        print('-' * 20)

        #вызов функции генерации случайного бочонка

        game_digit = barrel_generation()

        print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')

        # вызов функции меню ответа игрока

        answer = player_answer()

        if game_digit in new_card and answer == 1:
            for count in range(27):
                if game_digit == new_card[count]:
                    new_card[count] = 'quantity_players'
            print(f'\033[92m\033[1mВерно! Такое число есть!\033[0;0m')


        elif game_digit not in new_card and answer == 2:
            print(f'\033[92m\033[1mВерно! Такого числа нет! Продолжаем игру. \033[0;0m')


        elif answer == 2 and game_digit in new_card:
            print(f'\033[91m\033[1mСтоп игра! Вы проиграли! Такое число есть! \033[0;0m')
            sys.exit(0)
        elif answer == 1 and game_digit not in new_card:
            print(f'\033[91m\033[1mСтоп игра!Вы проиграли! Такого числа нет!\033[0;0m')
            sys.exit(0)


        end_of_game = 0
        for count in new_card:
            if count == 'quantity_players':
                end_of_game += 1
        if end_of_game == 15:
            print(f'\033[95m\033[1mИгра окончена! Вы победили!\033[0m')
            sys.exit(0)


        step += 1

        print('-' * 20)
        print(*new_card[0:27:3])
        print(*new_card[1:27:3])
        print(*new_card[2:27:3])
        print('-' * 20)








