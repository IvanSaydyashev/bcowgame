import random


def check(number_player, number_computer):
    """ Находим количество коров и быков в числе """

    # индексы коров и быков
    n_c, n_b = [], []

    try:
        # переводим наши числа в список из символов.
        number_player_list = list(str(number_player))
        number_computer_list = list(str(number_computer))

        # проходимся по числ
        for index in range(len(number_player_list)):

            # если в разных числа в одинаковых индексах цифры ровны, то это бык
            if number_computer_list[index] == number_player_list[index]:
                n_b.append(index)
            # если в числах есть одинаковые цифры, но на разных местах, то это корова
            elif number_player_list[index] in number_computer_list:
                n_c.append(index)

        # возвращаем списки индексов коров и быков
        print(f"Найдено {len(n_c)} коров и {len(n_b)} быков")
        return n_c, n_b
    except:
        return n_c, n_b


def is_valid(number):
    """ Проверка числа на уникальность. Все 4 цифры
    числа должны быть разные """

    try:
        # переводим наше число в список из символов. сравниваем с множеством.
        # (в множестве нет повторяющихся символов)
        number_list = list(str(number))
        if len(set(number_list)) == 4:
            return True
        return False

    except:
        return False


def main():
    # переменные
    number_player, number_computer, n = 0, 0, 0

    # списки
    n_c, n_b = [], []

    # генерируем число, которое нужно отгадать
    while not is_valid(number_computer):
        number_computer = random.randint(1000, 9999)

    # вводим число
    while not is_valid(number_player):
        number_player = int(input("Введите число\n"))

    # главный цикл, работает, пока не будет 4 быка, то есть
    # два числа не будут ровны между собой

    # получаем списки индексов коров и быков
    n_c, n_b = check(number_player, number_computer)

    while len(n_b) != 4:
        # пересобираем число из имеющихся данных
        number_player = int(input("Введите число\n"))

        # получаем списки индексов коров и быков
        n_c, n_b = check(number_player, number_computer)
        n += 1

    print(number_player)


if __name__ == '__main__':
    main()
