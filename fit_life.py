WATER_ML_PER_KG = 30
# Cтандартная рекомендация 30 мл воды на 1 кг массы тела
ML_PER_LITER = 1000
# В одном литре 1000 миллилитров
SEPARATOR = ('-' * 48)
# Строка-разделитель для оформления отчёта


def get_user_info():
    """Собрать данные пользователя"""
    # Создали функцию с вычислениями
    print('Приветствую Вас в программе Fit Life!!!')
    # Приветствие пользователя
    user_name = input('Как я могу к Вам обращаться? ').capitalize()
    # Присвоили user_name имя и привели к нужному регистру
    user_age = int(input('Введите Ваш полный возраст '))
    while True:
        try:
            user_weight = float(
                input('Введите ваш вес (в кг) ').replace(',', '.')
            )
            # Присвоили user_weight, перевели в float и заменили ',' на '.'
            if user_weight <= 0:
                print('Вес не может иметь отрицательное значение!')
            else:
                break
        except ValueError:
            print('Введите Ваш вес в числовом значении (например 72.2)')
    # Проверили что пользователь вводит правильные значения
    while True:
        try:
            user_height = float(
                input(
                    'Введите ваш рост в метрах (например 1.75) '
                ).replace(',', '.')
            )
            # Присвоили user_height, перевели в формат float и заменили , на .
            if user_height <= 0:
                print('Рост не может быть отрицательным!')
            else:
                break
        except ValueError:
            print('Введите Ваш рост в числовом значении (например 1.72)')
    # Проверили что пользователь вводит правильные значения
    bmi = round(user_weight / (user_height ** 2), 1)
    # Присвоили bmi индекс массы тела и округлили до одного знака после запятой
    water_ml = user_weight * WATER_ML_PER_KG
    # Рассчитать норму воды в миллилитрах
    water_l = round(water_ml / ML_PER_LITER, 1)
    # Перевели миллилитры в литры и округлили до 1 знака после запятой
    return user_name, user_age, bmi, water_l


if __name__ == "__main__":
    user_name, user_age, bmi, water_l = get_user_info()
    # Теперь можно будет вызывать функцию из других модулей
    print(
        f'{SEPARATOR}\n'
        f'Отчет для пользователя: {user_name} ({user_age} г.)\n'
        f'Ваш Индекс Массы Тела: {bmi}\n'
        f'Рекомендуемая норма воды: {water_l} л. в день\n'
        f'{SEPARATOR}\n'
        'Расчет окончен. Будьте здоровы!',
    )
    # Вывод отчета под один print
