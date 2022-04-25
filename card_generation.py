import random

if __name__ != '__main__':

    def card_generation():
        digits = []
        space_number = []
        digits_for_card = []
        space_number_for_card = []


        # генерируем список от 1 до 90 для последующей случайной выборке цифр для карточки лото
        for count in range(1, 91):
            digits.append(count)

        # генерирования списка из 15 чисел для карточки
        # случайным образом отбираем 15 цифр для карточки лото ранее сделанного списка
        digits_for_card.append(random.sample(digits, 15))
        # распаковываем вложенный список в обычный список
        digits_for_card = [*digits_for_card[0]]
        # сортируеь по возврастанию список
        digits_for_card.sort()

        # генерируем список номеров от 0 до 26 для определения места пробелов для карточки лото
        for count in range(0, 27):
            space_number.append(count)

        # формировние списка номеров мест будущих 12ти пробелов в карточке
        space_number_for_card.append(random.sample(space_number, 12))
        space_number_for_card = [*space_number_for_card[0]]
        space_number_for_card.sort()
        # print(f'Места будущих пробелов {space_number_for_card}')

        # расставляем пробелы и цифры по местам
        new_card = []
        x = 0
        for count in range(27):
            if count in space_number_for_card:
                new_card.append(' ')
                x += 1
            else:
                new_card.append(digits_for_card[count - x])

        # формируем карточу лото

        # print('-' * 20)
        # print(*new_card[0:27:3])
        # print(*new_card[1:27:3])
        # print(*new_card[2:27:3])
        # print('-' * 20)
        return new_card








