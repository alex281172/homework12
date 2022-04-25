import sys
from class_card_generation import Card
from barrel_generation import barrel_generation
from design_themes import printing_space

if __name__ != '__main__':

    def main_game(quantity_players):
        # quantity_players = int(input('Укажите количество игроков -> '))
        spisok = []
        player = []
        looser = []
        looser_count = 0

        for count in range(1, quantity_players + 1, 1):
            name = input(f'Введите имя игрока {count}: ')
            spisok.append(name)

        printing_space(50)
        print('*' * 50)
        print('              Начинаем ИГРУ ЛОТО')
        print('*' * 50)

        for count in range(quantity_players):
            player.append(count)
            player[count] = Card()
            player[count].card_generation_class()

        print('*' * 50)
        print('              Начинаем ИГРУ ЛОТО')
        print('                \033[91m\033[1mВ игре участвуют:\033[0;0m')
        for count in range(quantity_players):
            print(f'{count + 1}. \033[91m\033[1m{spisok[count]}\033[0;0m')
        print('*' * 50)

        step = 1
        while step < 91:
            print('*' * 50)
            print(f'             В мешке  {91 - step} бочат')
            print('*' * 50)
            printing_space(1)

            game_digit = barrel_generation()

            for count in range(quantity_players):

                if count not in looser:

                    print(f'\033[91m\033[1mКарточка ИГРОКА {spisok[count]}\033[0;0m')
                    print('-' * 20)
                    print(*player[count].new_card[0:27:3])
                    print(*player[count].new_card[1:27:3])
                    print(*player[count].new_card[2:27:3])
                    print('-' * 20)

                    print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')

                    print(f'ИГРОК {spisok[count]}')

                    answer1 = player[count].player_answer_class()

                    if game_digit in player[count].new_card and answer1 == 1:
                        for count1 in range(27):
                            if game_digit == player[count].new_card[count1]:
                                player[count].new_card[count1] = 'x'

                        print(f'\033[92m\033[1mВерно! {spisok[count]}, такое число есть!\033[0;0m')
                        print('*' * 50)
                        printing_space(1)

                    elif game_digit not in player[count].new_card and answer1 == 2:

                        print(f'\033[92m\033[1mВерно! {spisok[count]}, такого числа нет! Продолжаем игру. \033[0;0m')
                        print('*' * 50)
                        printing_space(1)

                    elif answer1 == 2 and game_digit in player[count].new_card:
                        print(f'\033[91m\033[1mСтоп игра! {spisok[count]}, Вы проиграли! Такое число есть! \033[0;0m')
                        print('*' * 50)
                        printing_space(1)
                        looser.append(count)
                        looser_count += 1
                        # sys.exit(0)

                    elif answer1 == 1 and game_digit not in player[count].new_card:
                        print(f'\033[91m\033[1mСтоп игра! {spisok[count]}, Вы проиграли! Такого числа нет!\033[0;0m')
                        print('*' * 50)
                        printing_space(1)
                        looser.append(count)
                        looser_count += 1
                        # sys.exit(0)

                    if looser_count == quantity_players:
                        print(f'\033[95m\033[1mИгра окончена! Победивших нет!\033[0m')
                        sys.exit(0)

                    end_of_game = 0
                    for count2 in player[count].new_card:
                        if count2 == 'x':
                            end_of_game += 1
                    if end_of_game == 15:
                        print(f'\033[95m\033[1mИгра окончена! {spisok[count]}, Вы победили!\033[0m')
                        sys.exit(0)
            step += 1
