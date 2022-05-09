import random
class Card:
    def __init__(self):
        self.digits = []
        self.space_number = []
        self.space_number_for_card = []
        self.digits_for_card = []
        self.answer = []

    def card_generation_class(self, digit_qv = 15, card_size = 27):

        for count in range(1, 91):
            self.digits.append(count)

        # генерирования списка из 15 чисел для карточки
        # случайным образом отбираем 15 цифр для карточки лото ранее сделанного списка
        self.digits_for_card.append(random.sample(self.digits, digit_qv))
        # print(self.digits_for_card)

        # распаковываем вложенный список в обычный список
        self.digits_for_card = [*self.digits_for_card[0]]
        # print(self.digits_for_card)
        # сортируем по возврастанию список
        self.digits_for_card.sort()
        # print(self.digits_for_card)

        # генерируем список номеров от 0 до 26 для определения места пробелов для карточки лото
        for count in range(0, card_size):
            self.space_number.append(count)

        # формировние списка номеров мест будущих 12ти пробелов в карточке
        self.space_number_for_card.append(random.sample(self.space_number, card_size - digit_qv))
        self.space_number_for_card = [*self.space_number_for_card[0]]
        self.space_number_for_card.sort()
        # print(f'Места будущих пробелов {space_number_for_card}')

        # расставляем пробелы и цифры по местам
        self.new_card = []

        x = 0
        for count in range(card_size):
            if count in self.space_number_for_card:
                self.new_card.append(' ')
                x += 1
            else:
                self.new_card.append(self.digits_for_card[count-x])

    def __str__(self):
        return f'{self.digits_for_card} {self.new_card}'

    def __eq__(self, other):
        return self.new_card == other.new_card

    def __len__(self):
        return len(self.new_card)

    def player_answer_class(self, ans1 = 'y', ans2 = 'n'):
        while True:
            self.answer = input('ваш выбор y - ДА | n - НЕТ -> ')
            if self.answer == ans1 or self.answer == ans2:
                break
            else:
                print('сделайте правильный выбор')
        return self.answer

    def robot_answer_class(self):
            self.robot_answer = print('ваш выбор y - ДА | n - НЕТ -> ')
            return self.robot_answer

if __name__ == '__main__':
    card1 = Card()
    card2 = Card()

    card1.card_generation_class()
    card2.card_generation_class()

    print(str(card1))
    print(str(card2))

    print(card1 == card2)
    print(card1 != card2)

    print(len(card1))
    print(len(card2))

    print(len(card1) == len(card2))


