import sys
from class_card_generation import Card
from barrel_generation import barrel_generation
from design_themes import printing_space

if __name__ != '__main__':

    def main_game_robot(quantity_players):
        # quantity_players = 2
        spisok = []
        player = []

        for count in range(1, quantity_players + 1, 1):
            name = input(f'Введите имя робота {count}: ')
            spisok.append(name)

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

                print(f'\033[91m\033[1mКарточка РОБОТА {spisok[count]}\033[0;0m')
                print('-' * 20)
                print(*player[count].new_card[0:27:3])
                print(*player[count].new_card[1:27:3])
                print(*player[count].new_card[2:27:3])
                print('-' * 20)

                print(f'\033[91m\033[1mБоченок {game_digit}\033[0;0m')

                print(f'РОБОТ {spisok[count]}')

                player[count].robot_answer_class()

                if game_digit in player[count].new_card:
                    for count1 in range(27):
                        if game_digit == player[count].new_card[count1]:
                            print(f'\033[92m\033[1mТакое число есть! Мой выбор \'1\'\033[0;0m')
                            int(1)
                            print(f'\033[92m\033[1mВерно! Такое число есть! Продолжаем игру.\033[0;0m')
                            player[count].new_card[count1] = 'x'

                elif game_digit not in player[count].new_card:
                    print(f'\033[92m\033[1mТакого числа нет! Мой выбор \'2\'\033[0;0m')
                    int(2)
                    print(f'\033[92m\033[1mВерно! Такого числа нет! Продолжаем игру.\033[0;0m')

                # while True:
                #     print('\033[1mНажмите \033[91m\'n\'\033[0;0m \033[1mдля следующего хода\033[0;0m')
                #     keyboard.wait('n')
                #     keyboard.write('\nНажата клавиша n\n')
                #     time.sleep(0.2)
                #     break

                end_of_game = 0
                for count2 in player[count].new_card:
                    if count2 == 'x':
                        end_of_game += 1

                if end_of_game == 15:
                    print(f'\033[95m\033[1mИгра окончена! РОБОТ {spisok[count]} победил!\033[0m')
                    sys.exit(0)

            step += 1
