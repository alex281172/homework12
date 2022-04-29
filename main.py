import sys
from class_card_generation import Card
from barrel_generation import barrel_generation
from design_themes import printing_space
from main_game import main_game
from main_game_robot import main_game_robot

print('*' * 50)
print('                      ИГРА ЛОТО')
print('*' * 50)
print('Выберите вариант ИГРЫ:')
print('1 - ОДИН ИГРОК')
print('2 - ИГРОК против ИГРОКА')
print('3 - ИГРОК против РОБОТА')
print('4 - РОБОТ против РОБОТА')
print('5 - ЛЮБОЕ КОЛИЧЕСТВО ИГРОКОВ')
print('6 - выход')

choise = input('Ваш выбор -> ')
if choise == '1':
    main_game(1)

elif choise == '2':
    main_game(2)

elif choise == '3':
    name1 = input('имя игрока: ')
    name2 = input('имя робота: ')

    # name1 = player1
    # name2 = player2
    player1 = Card()
    player2 = Card()
    # print(f'Карточка ИГРОКА {name1}')
    player1.card_generation_class()
    # print(f'Карточка ИГРОКА {name2}')
    player2.card_generation_class()
    printing_space(50)

    print('*' * 50)
    print('              Начинаем ИГРУ ЛОТО')
    print(f'\033[91m\033[1m              {name1} против {name2}\033[0;0m')
    print('*' * 50)

    step = 1
    while step < 91:
        print('*' * 50)
        print(f'             В мешке  {91 - step} бочат')
        print('*' * 50)
        printing_space(1)

        game_digit = barrel_generation()

        print(f'\033[91m\033[1mКарточка ИГРОКА {name1}\033[0;0m')

        print('-' * 20)
        print(*player1.new_card[0:27:3])
        print(*player1.new_card[1:27:3])
        print(*player1.new_card[2:27:3])
        print('-' * 20)

        print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')

        print(f'ИГРОК {name1}')
        answer1 = player1.player_answer_class()
        if game_digit in player1.new_card and answer1 == 'y':
            for count in range(27):
                if game_digit == player1.new_card[count]:
                    player1.new_card[count] = 'x'
            print(f'\033[92m\033[1mВерно! {name1}, такое число есть!\033[0;0m')

        elif game_digit not in player1.new_card and answer1 == 'n':
            print(f'\033[92m\033[1mВерно! {name1}, такого числа нет! Продолжаем игру. \033[0;0m')

        elif answer1 == 'n' and game_digit in player1.new_card:
            print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такое число есть! \033[0;0m')
            sys.exit(0)
        elif answer1 == 'y' and game_digit not in player1.new_card:
            print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такого числа нет!\033[0;0m')

            sys.exit(0)

        end_of_game = 0
        for count in player1.new_card:
            if count == 'quantity_robots':
                end_of_game += 1
        if end_of_game == 15:
            print(f'\033[95m\033[1mИгра окончена! {name1}, Вы победили!\033[0;0m')
            sys.exit(0)

        printing_space(1)

        print(f'\033[91m\033[1mКарточка РОБОТА {name2}\033[0;0m')

        print('-' * 20)
        print(*player2.new_card[0:27:3])
        print(*player2.new_card[1:27:3])
        print(*player2.new_card[2:27:3])
        print('-' * 20)

        print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')

        print(f'РОБОТ {name2}')

        answer2 = player2.robot_answer_class()

        if game_digit in player2.new_card:
            for count in range(27):
                if game_digit == player2.new_card[count]:
                    print(f'\033[92m\033[1mТакое число есть! Мой выбор \'y\'\033[0;0m')
                    answer = 'y'
                    print(f'\033[92m\033[1mВерно! Такое числа есть! Продолжаем игру.\033[0;0m')
                    player2.new_card[count] = 'x'

        else:
            print(f'\033[92m\033[1mТакого числа нет! Мой выбор \'n\'\033[0;0m')
            answer = 'n'
            print(f'\033[92m\033[1mВерно! Такого числа нет! Продолжаем игру.\033[0;0m')

        end_of_game = 0
        for count in player2.new_card:
            if count == 'quantity_robots':
                end_of_game += 1
        if end_of_game == 15:
            print(f'\033[95m\033[1mИгра окончена! РОБОТ {name2}!\033[0m')
            sys.exit(0)

        step += 1

elif choise == '4':
    main_game_robot(2)

if choise == '5':
    main_game(int(input('Укажите количество игроков -> ')))


elif choise == '6':
    sys.exit(0)
