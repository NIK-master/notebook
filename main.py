from src.tools import *


while True:
    print(commands)
    command = int(input('Введите номер команды: '))
    if command == 1:
        try:
            main_dict = load_data('save_data.dat')
            main_dict.update(
                {input('Введите имя: '): make_data(int(input('Введите телефон: ')), input('Введите адрес: '))})
            dump_data('save_data.dat', main_dict)
        except EOFError:
            main_dict = load_data('save_data.dat')
        except FileNotFoundError:
            dump_data('save_data.dat', main_dict)
            main_dict = load_data('save_data.dat')
            main_dict.update({input('Введите имя: '): make_data(int(input('Введите телефон: ')), input('Введите адрес: '))})
            dump_data('save_data.dat', main_dict)
    elif command == 2:
        main_dict = load_data('save_data.dat')
        try:
            print(main_dict[input('Введите имя пользователя: ')])
        except KeyError:
            print('Такого контакта не существует')
        f_saving.close()
    elif command == 3:
        break
    elif command == 4:
        main_dict = load_data('save_data.dat')
        for i in main_dict:
            print(f'Имя: {i} Телефон: {main_dict[i][head_dict[0]]} Адрес: {main_dict[i][head_dict[1]]}')
    elif command == 5:
        main_dict = load_data('save_data.dat')
        main_dict.clear()
        dump_data('save_data.dat', main_dict)
    elif command == 6:
        main_dict = sort_for_number(main_dict)
    else:
        print('Такой команды не существует')
print("Программа закрывается")
