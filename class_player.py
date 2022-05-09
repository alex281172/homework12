import random

class Player:
    def __init__(self):
        self.name_player = input('укажите имя игрока: ')

        self.digits = []
        self.space_number = []
        self.space_number_for_card = []
        self.digits_for_card = []
        self.new_card = []

        self.barrel = []
        # мешок с бочатами
        self.barrels_bag = []
        self.barrels_bag_new = []

        # формировние мешка с бочатами
        for digits_count in range(1, 91, 1):
            self.barrels_bag.append(digits_count)



    def card_generation_class(self):

        for count4 in range(1, 91):
            self.digits.append(int(count4))

        # генерирования списка из 15 чисел для карточки
        # случайным образом отбираем 15 цифр для карточки лото ранее сделанного списка
        self.digits_for_card.append(random.sample(self.digits, 15))
        # print(self.digits_for_card)

        # распаковываем вложенный список в обычный список
        self.digits_for_card = [*self.digits_for_card[0]]
        # print(self.digits_for_card)
        # сортируем по возврастанию список
        self.digits_for_card.sort()
        # print(self.digits_for_card)

        # генерируем список номеров от 0 до 26 для определения места пробелов для карточки лото
        for count1 in range(0, 27):
            self.space_number.append(count1)

        # формировние списка номеров мест будущих 12ти пробелов в карточке
        self.space_number_for_card.append(random.sample(self.space_number, 12))
        self.space_number_for_card = [*self.space_number_for_card[0]]
        self.space_number_for_card.sort()
        # print(f'Места будущих пробелов {space_number_for_card}')

        # расставляем пробелы и цифры по местам
        self.new_card = []

        x = 0
        for count2 in range(27):
            if count2 in self.space_number_for_card:
                self.new_card.append(' ')
                x += 1
            else:
                self.new_card.append(self.digits_for_card[count2-x])
        # return self.new_card


        # генерирование боченка
    def barrel_generation(self):
        # генерировние боченка
        self.barrel = random.choice(self.barrels_bag)
        self.barrels_bag.remove(self.barrel)
        return self.barrel

    def player_answer_class(self):
        while True:
            self.answer = input('ваш выбор y - ДА | n - НЕТ -> ')
            if self.answer == 'y' or self.answer == 'n':
                break
            else:
                print('сделайте правильный выбор')
        return self.answer




if __name__ == '__main__':
    namelist = []
    cardlist = []
    barrellist = []
    quantity = 4
    looser_list = []
    looser_count = 0
    player_dict = {}



    for count_player in range(quantity):
        player = Player()
        player.card_generation_class()
        namelist.append(player.name_player)
        cardlist.append(player.new_card)
        player_dict.update({player.name_player:player.new_card})
        print(f'Игрок: {player.name_player}, карточка {player.new_card}')


    print(player_dict)
    print(f'В игре участвуют: {namelist}')

    for x in namelist:
        print(player_dict.setdefault(x))



    for count_step in range(90):
        for count_player1 in range(quantity):
            if namelist[count_player1] not in looser_list:
                print('*' * 50)
                print(f'Карточка игрока {namelist[count_player1]}')
                print('-' * 20)
                print(*cardlist[count_player1][0:27:3])
                print(*cardlist[count_player1][1:27:3])
                print(*cardlist[count_player1][2:27:3])
                print('-' * 20)
                player.barrel = player.barrel_generation()

                print(f'Боченок игрока {namelist[count_player1]}: {player.barrel}')
                print('-' * 20)

                player.player_answer_class()

                if player.barrel in cardlist[count_player1] and player.answer == 'y':
                    for count1 in range(27):
                        if player.barrel == cardlist[count_player1][count1]:
                            cardlist[count_player1][count1] = 'x'

                    print(f'\033[92m\033[1mВерно! {player.name_player}, такое число есть!\033[0;0m')
                    print('*' * 50)

                elif player.barrel not in cardlist[count_player1] and player.answer == 'n':

                    print(f'\033[92m\033[1mВерно! {player.name_player}, такого числа нет! Продолжаем игру. \033[0;0m')
                    print('*' * 50)

                elif player.answer == 'n' and player.barrel in cardlist[count_player1]:
                    print(f'\033[91m\033[1mСтоп игра! {player.name_player}, Вы проиграли! Такое число есть! \033[0;0m')
                    print('*' * 50)
                    looser_list.append(namelist[count_player1])
                    looser_count += 1

                elif player.answer == 'y' and player.barrel not in cardlist[count_player1]:
                    print(f'\033[91m\033[1mСтоп игра! {player.name_player}, Вы проиграли! Такого числа нет!\033[0;0m')
                    print('*' * 50)

                    looser_list.append(namelist[count_player1])
                    looser_count += 1


