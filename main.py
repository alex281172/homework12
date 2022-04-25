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
    # printing_space(50)
    # print('*' * 50)
    # print('              Начинаем ИГРУ ЛОТО')
    # print('*' * 50)
    #
    # player1 = input('имя игрока 1: ')
    # name1 = player1
    # player1 = Card()
    # # print(f'Карточка ИГРОКА {name1}')
    # player1.card_generation_class()
    # printing_space(50)
    #
    # print('*' * 50)
    # print('              Начинаем ИГРУ ЛОТО')
    # print('*' * 50)
    #
    # step = 1
    # while step < 91:
    #     print('*' * 50)
    #     print(f'             В мешке  {91 - step} бочат')
    #     print('*' * 50)
    #     printing_space(1)
    #
    #     game_digit = barrel_generation()
    #
    #     print(f'\033[91m\033[1mКарточка ИГРОКА {name1}\033[0;0m')
    #
    #     print('-' * 20)
    #     print(*player1.new_card[0:27:3])
    #     print(*player1.new_card[1:27:3])
    #     print(*player1.new_card[2:27:3])
    #     print('-' * 20)
    #
    #     print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
    #
    #     print(f'ИГРОК {name1}')
    #     answer1 = player1.player_answer_class()
    #     if game_digit in player1.new_card and answer1 == 1:
    #         for count in range(27):
    #             if game_digit == player1.new_card[count]:
    #                 player1.new_card[count] = 'quantity_players'
    #         print(f'\033[92m\033[1mВерно! {name1}, такое число есть!\033[0;0m')
    #
    #     elif game_digit not in player1.new_card and answer1 == 2:
    #         print(f'\033[92m\033[1mВерно! {name1}, такого числа нет! Продолжаем игру. \033[0;0m')
    #
    #     elif answer1 == 2 and game_digit in player1.new_card:
    #         print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такое число есть! \033[0;0m')
    #         sys.exit(0)
    #     elif answer1 == 1 and game_digit not in player1.new_card:
    #         print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такого числа нет!\033[0;0m')
    #
    #         sys.exit(0)
    #
    #     end_of_game = 0
    #     for count in player1.new_card:
    #         if count == 'quantity_players':
    #             end_of_game += 1
    #     if end_of_game == 15:
    #         print(f'\033[95m\033[1mИгра окончена! {name1}, Вы победили!\033[0m')
    #         sys.exit(0)
    #     step += 1

elif choise == '2':
    main_game(2)
    # player1 = input('имя игрока 1: ')
    # player2 = input('имя игрока 2: ')
    # name1 = player1
    # name2 = player2
    # player1 = Card()
    # player2 = Card()
    # # print(f'Карточка ИГРОКА {name1}')
    # player1.card_generation_class()
    # # print(f'Карточка ИГРОКА {name2}')
    # player2.card_generation_class()
    # printing_space(50)
    #
    # print('*' * 50)
    # print('              Начинаем ИГРУ ЛОТО')
    # print(f'\033[91m\033[1m              {name1} против {name2}\033[0;0m')
    # print('*' * 50)
    #
    # step = 1
    # while step < 91:
    #     print('*' * 50)
    #     print(f'             В мешке  {91 - step} бочат')
    #     print('*' * 50)
    #     printing_space(1)
    #
    #     game_digit = barrel_generation()
    #
    #     print(f'\033[91m\033[1mКарточка ИГРОКА {name1}\033[0;0m')
    #
    #     print('-' * 20)
    #     print(*player1.new_card[0:27:3])
    #     print(*player1.new_card[1:27:3])
    #     print(*player1.new_card[2:27:3])
    #     print('-' * 20)
    #
    #     print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
    #
    #     print(f'ИГРОК {name1}')
    #     answer1 = player1.player_answer_class()
    #     if game_digit in player1.new_card and answer1 == 1:
    #         for count in range(27):
    #             if game_digit == player1.new_card[count]:
    #                 player1.new_card[count] = 'quantity_players'
    #         print(f'\033[92m\033[1mВерно! {name1}, такое число есть!\033[0;0m')
    #
    #     elif game_digit not in player1.new_card and answer1 == 2:
    #         print(f'\033[92m\033[1mВерно! {name1}, такого числа нет! Продолжаем игру. \033[0;0m')
    #
    #     elif answer1 == 2 and game_digit in player1.new_card:
    #         print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такое число есть! \033[0;0m')
    #         sys.exit(0)
    #     elif answer1 == 1 and game_digit not in player1.new_card:
    #         print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такого числа нет!\033[0;0m')
    #
    #         sys.exit(0)
    #
    #     end_of_game = 0
    #     for count in player1.new_card:
    #         if count == 'quantity_players':
    #             end_of_game += 1
    #     if end_of_game == 15:
    #         print(f'\033[95m\033[1mИгра окончена! {name1}, Вы победили!\033[0m')
    #         sys.exit(0)
    #
    #     printing_space(1)
    #
    #     print(f'\033[91m\033[1mКарточка ИГРОКА {name2}\033[0;0m')
    #
    #     print('-' * 20)
    #     print(*player2.new_card[0:27:3])
    #     print(*player2.new_card[1:27:3])
    #     print(*player2.new_card[2:27:3])
    #     print('-' * 20)
    #
    #     print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
    #
    #     print(f'ИГРОК {name2}')
    #     answer2 = player2.player_answer_class()
    #
    #     if game_digit in player2.new_card and answer2 == 1:
    #         for count in range(27):
    #             if game_digit == player2.new_card[count]:
    #                 player2.new_card[count] = 'quantity_players'
    #         print(f'\033[92m\033[1mВерно! {name2}, такое число есть!\033[0;0m')
    #
    #     elif game_digit not in player2.new_card and answer2 == 2:
    #         print(f'\033[92m\033[1mВерно! {name2}, такого числа нет! Продолжаем игру.\033[0;0m')
    #
    #     elif answer2 == 2 and game_digit in player2.new_card:
    #         print(f'\033[91m\033[1mСтоп игра! {name2}, Вы проиграли! Такое число есть!\033[0;0m')
    #         sys.exit(0)
    #     elif answer2 == 1 and game_digit not in player2.new_card:
    #         print(f'\033[91m\033[1mСтоп игра! {name2}, Вы проиграли! Такого числа нет!\033[0;0m')
    #         sys.exit(0)
    #
    #     printing_space(3)
    #
    #     end_of_game = 0
    #     for count in player2.new_card:
    #         if count == 'quantity_players':
    #             end_of_game += 1
    #     if end_of_game == 15:
    #         print(f'\033[95m\033[1mИгра окончена! {name2}, Вы победили!\033[0m')
    #         sys.exit(0)
    #
    #     step += 1

elif choise == '3':
    player1 = input('имя игрока: ')
    player2 = input('имя робота: ')

    name1 = player1
    name2 = player2
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
        if game_digit in player1.new_card and answer1 == 1:
            for count in range(27):
                if game_digit == player1.new_card[count]:
                    player1.new_card[count] = 'x'
            print(f'\033[92m\033[1mВерно! {name1}, такое число есть!\033[0;0m')

        elif game_digit not in player1.new_card and answer1 == 2:
            print(f'\033[92m\033[1mВерно! {name1}, такого числа нет! Продолжаем игру. \033[0;0m')

        elif answer1 == 2 and game_digit in player1.new_card:
            print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такое число есть! \033[0;0m')
            sys.exit(0)
        elif answer1 == 1 and game_digit not in player1.new_card:
            print(f'\033[91m\033[1mСтоп игра! {name1}, Вы проиграли! Такого числа нет!\033[0;0m')

            sys.exit(0)

        end_of_game = 0
        for count in player1.new_card:
            if count == 'quantity_players':
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
                    print(f'\033[92m\033[1mТакое число есть! Мой выбор \'1\'\033[0;0m')
                    answer = int(1)
                    print(f'\033[92m\033[1mВерно! Такое числа есть! Продолжаем игру.\033[0;0m')
                    player2.new_card[count] = 'x'

        else:
            print(f'\033[92m\033[1mТакого числа нет! Мой выбор \'2\'\033[0;0m')
            answer = int(2)
            print(f'\033[92m\033[1mВерно! Такого числа нет! Продолжаем игру.\033[0;0m')

        end_of_game = 0
        for count in player2.new_card:
            if count == 'quantity_players':
                end_of_game += 1
        if end_of_game == 15:
            print(f'\033[95m\033[1mИгра окончена! РОБОТ {name2}!\033[0m')
            sys.exit(0)

        step += 1

elif choise == '4':
    main_game_robot(2)
    # player1 = input('имя робота 1: ')
    # player2 = input('имя робота 2: ')
    #
    # name1 = player1
    # name2 = player2
    # player1 = Card()
    # player2 = Card()
    # # print(f'Карточка ИГРОКА {name1}')
    # player1.card_generation_class()
    # # print(f'Карточка ИГРОКА {name2}')
    # player2.card_generation_class()
    # printing_space(50)
    #
    # print('*' * 50)
    # print('              Начинаем ИГРУ ЛОТО')
    # print(f'\033[91m\033[1m              {name1} против {name2}\033[0;0m')
    # print('*' * 50)
    #
    # step = 1
    # while step < 91:
    #     print('*' * 50)
    #     print(f'             В мешке  {91 - step} бочат')
    #     print('*' * 50)
    #     printing_space(1)
    #
    #     game_digit = barrel_generation()
    #
    #     print(f'\033[91m\033[1mКарточка РОБОТА {name1}\033[0;0m')
    #
    #     print('-' * 20)
    #     print(*player1.new_card[0:27:3])
    #     print(*player1.new_card[1:27:3])
    #     print(*player1.new_card[2:27:3])
    #     print('-' * 20)
    #
    #     print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
    #
    #     print(f'ИГРОК {name1}')
    #
    #     answer1 = player1.robot_answer_class()
    #
    #     if game_digit in player1.new_card:
    #         for count in range(27):
    #             if game_digit == player1.new_card[count]:
    #                 print(f'\033[92m\033[1mТакое число есть! Мой выбор \'1\'\033[0;0m')
    #                 answer = int(1)
    #                 print(f'\033[92m\033[1mВерно! Такое числа есть! Продолжаем игру.\033[0;0m')
    #                 player1.new_card[count] = 'x'
    #
    #     else:
    #         print(f'\033[92m\033[1mТакого числа нет! Мой выбор \'2\'\033[0;0m')
    #         answer = int(2)
    #         print(f'\033[92m\033[1mВерно! Такого числа нет! Продолжаем игру.\033[0;0m')
    #
    #     end_of_game = 0
    #     for count in player1.new_card:
    #         if count == 'quantity_players':
    #             end_of_game += 1
    #     if end_of_game == 15:
    #         print(f'\033[95m\033[1mИгра окончена! {name1}, Вы победили!\033[0m')
    #         sys.exit(0)
    #
    #     printing_space(1)
    #
    #     print(f'\033[91m\033[1mКарточка РОБОТА {name2}\033[0;0m')
    #
    #     print('-' * 20)
    #     print(*player2.new_card[0:27:3])
    #     print(*player2.new_card[1:27:3])
    #     print(*player2.new_card[2:27:3])
    #     print('-' * 20)
    #
    #     print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
    #
    #     print(f'ИГРОК {name2}')
    #
    #     answer2 = player2.robot_answer_class()
    #
    #     if game_digit in player2.new_card:
    #         for count in range(27):
    #             if game_digit == player2.new_card[count]:
    #                 print(f'\033[92m\033[1mТакое число есть! Мой выбор \'1\'\033[0;0m')
    #                 answer = int(1)
    #                 print(f'\033[92m\033[1mВерно! Такое число есть! Продолжаем игру.\033[0;0m')
    #                 player2.new_card[count] = 'x'
    #
    #     else:
    #         print(f'\033[92m\033[1mТакого числа нет! Мой выбор \'2\'\033[0;0m')
    #         answer = int(2)
    #         print(f'\033[92m\033[1mВерно! Такого числа нет! Продолжаем игру.\033[0;0m')
    #
    #     while True:
    #         print('\033[1mНажмите \033[91m\'n\'\033[0;0m \033[1mдля следующего хода\033[0;0m')
    #         keyboard.wait('n')
    #         keyboard.write('\nНажата клавиша n\n')
    #         time.sleep(0.2)
    #
    #         break
    #
    #     # завершение игры: проверка на количество зачеркнутых номеров, сообщение о победе
    #     end_of_game = 0
    #     for count in player2.new_card:
    #         if count == 'quantity_players':
    #             end_of_game += 1
    #     if end_of_game == 15:
    #         print(f'\033[95m\033[1mИгра окончена! {name2}, Вы победили!\033[0m')
    #         sys.exit(0)
    #
    #     step += 1


if choise == '5':
    main_game(int(input('Укажите количество игроков -> ')))
    # printing_space(50)
    # print('*' * 50)
    # print('              Начинаем ИГРУ ЛОТО')
    # print('*' * 50)
    #
    # quantity_players = int(input('Укажите количество игроков -> '))
    # spisok = []
    # for count in range(1, quantity_players + 1, 1):
    #     name = input(f'Введите имя игрока {count}: ')
    #     spisok.append(name)
    #
    # player = []
    # looser = []
    # looser_count = 0
    #
    # for count in range(quantity_players):
    #     player.append(count)
    #     player[count] = Card()
    #     player[count].card_generation_class()
    #
    # print('*' * 50)
    # print('              Начинаем ИГРУ ЛОТО')
    # print('                \033[91m\033[1mВ игре участвуют:\033[0;0m')
    # for count in range(quantity_players):
    #     print(f'{count + 1}. \033[91m\033[1m{spisok[count]}\033[0;0m')
    # print('*' * 50)
    #
    # step = 1
    # while step < 91:
    #     print('*' * 50)
    #     print(f'             В мешке  {91 - step} бочат')
    #     print('*' * 50)
    #     printing_space(1)
    #
    #     game_digit = barrel_generation()
    #
    #     for count in range(quantity_players):
    #
    #         if count not in looser:
    #
    #             print(f'\033[91m\033[1mКарточка ИГРОКА {spisok[count]}\033[0;0m')
    #             print('-' * 20)
    #             print(*player[count].new_card[0:27:3])
    #             print(*player[count].new_card[1:27:3])
    #             print(*player[count].new_card[2:27:3])
    #             print('-' * 20)
    #
    #             print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')
    #
    #             print(f'ИГРОК {spisok[count]}')
    #
    #             answer1 = player[count].player_answer_class()
    #
    #             if game_digit in player[count].new_card and answer1 == 1:
    #                 for count1 in range(27):
    #                     if game_digit == player[count].new_card[count1]:
    #                         player[count].new_card[count1] = 'quantity_players'
    #
    #                 print(f'\033[92m\033[1mВерно! {spisok[count]}, такое число есть!\033[0;0m')
    #                 print('*' * 50)
    #                 printing_space(1)
    #
    #             elif game_digit not in player[count].new_card and answer1 == 2:
    #
    #                 print(f'\033[92m\033[1mВерно! {spisok[count]}, такого числа нет! Продолжаем игру. \033[0;0m')
    #                 print('*' * 50)
    #                 printing_space(1)
    #
    #             elif answer1 == 2 and game_digit in player[count].new_card:
    #                 print(f'\033[91m\033[1mСтоп игра! {spisok[count]}, Вы проиграли! Такое число есть! \033[0;0m')
    #                 print('*' * 50)
    #                 printing_space(1)
    #                 looser.append(count)
    #                 looser_count += 1
    #                 # sys.exit(0)
    #
    #             elif answer1 == 1 and game_digit not in player[count].new_card:
    #                 print(f'\033[91m\033[1mСтоп игра! {spisok[count]}, Вы проиграли! Такого числа нет!\033[0;0m')
    #                 print('*' * 50)
    #                 printing_space(1)
    #                 looser.append(count)
    #                 looser_count += 1
    #                 # sys.exit(0)
    #
    #             if looser_count == quantity_players:
    #                 print(f'\033[95m\033[1mИгра окончена! Победивших нет!\033[0m')
    #                 sys.exit(0)
    #
    #             end_of_game = 0
    #             for count in player[count].new_card:
    #                 if count == 'quantity_players':
    #                     end_of_game += 1
    #             if end_of_game == 15:
    #                 print(f'\033[95m\033[1mИгра окончена! {spisok[count]}, Вы победили!\033[0m')
    #                 sys.exit(0)
    #     step += 1

elif choise == '6':
    sys.exit(0)
