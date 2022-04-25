if __name__ != '__main__':
    def player_answer():

        while True:
            answer = int(input('ваш выбор 1 - ДА | 2 - НЕТ -> '))
            if answer == 1 or answer == 2:
                break
            else:
                print('введите правильное число')
        return answer





