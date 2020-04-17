from src import tools
s = [random.randint(1, 100) for i in range(10)]
def Sort(список):  
    флаг = True
    while флаг:
        флаг = False
        for i in range(len(список) - 1):
            if список[i] > список[i + 1]:
                список[i], список[i + 1] = список[i + 1], список[i]
                флаг = True

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
            Sort(main_dict)
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
    else:
        print('Такой команды не существует')
print("Программа закрывается")
