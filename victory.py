import random

dates_of_birth = {'П.Л. Чебышев': '16.05.1821',
                  'М.В. Ломоносов': '19.11.1711',
                  'Д.И. Менделеев': '08.11.1834',
                  'А.С. Попов': '16.03.1859',
                  'Н.И. Лобачевский': '01.12.1792',
                  'А.С. Пушкин': '06.06.1799',
                  'М.Ю. Лермонтов': '15.04,1814',
                  'С.А. Есенин': '03.10.1895',
                  'М.М. Зощенко': '10.08.1894',
                  'М.А. Булгаков': '15.05.1891',
                  'В.В. Маяковский': '16.03.1859'
                  }

months_text = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
         7: 'июля',   8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}

days_text = {1: 'первое', 2: 'второе', 3: 'третье', 4: 'четвертое', 5: 'пятое', 6: 'шестое', 7: 'седьмое', 8: 'восьмое',
        9: 'девятое', 10: 'десятое', 11: 'одиннадцатое', 12: 'двенадцатое', 13: 'Тринадцатое', 14: 'Четырнадцатое',
        15: 'Пятнадцатое', 16: 'Шестнадцатое', 17: 'Семнадцатое', 18: 'Восемнадцатое', 19: 'Девятнадцатое',
        20: 'Двадцатое', 21: 'Двадцать первое', 22: 'Двадцать второе', 23: 'Двадцать третье', 24: 'Двадцать четвертое',
        25: 'Двадцать пятое', 26: 'Двадцать шестое', 27: 'Двадцать седьмое', 28: 'Двадцать восьмое',
        29: 'Двадцать девятое', 30: 'Традцатое', 31: 'Тридцать первое'}


names = random.sample(dates_of_birth.keys(), 5)
# print(names)

rights = 0
while True:
    for name in names:
        answer = input(f'Когда родился {name}? ')

        if answer == dates_of_birth[name]:
            print('Верно')
            rights += 1
        else:
            print('Неверно')
            day = int(dates_of_birth[name][:2])
            month = int(dates_of_birth[name][3:5])
            year = int(dates_of_birth[name][-4:])

            day = days_text[day].lower()
            month = months_text[month]

            answer = f'Верный ответ {day} {month} {year} года'
            print(answer)

    # totals = rights / len(names) * 100
    # print(f'Процент правильных ответов: {totals}%')
    text = 'Процент правильных ответов: {:.1%}'.format(rights / len(names))
    print(text)

    continue_desision = input('Повторить? [yes = any_key / no = \'n\'] ')

    if continue_desision == 'n':
        print('Ну как хотите. Выходим.')
        break
    else:
        print('\n\n')   # Отступ перед новой викториной


