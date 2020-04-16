import pickle

head_dict = ("Телефон", "Адрес")
main_dict = {}
commands = '1.Добавить в справочник контактов\n2.Вывести значения по конаткту\n3.Закончить работу с словарём из справочника\n4.Вывести весь словарь\n5.Очстить словарь.'


def make_data(telephone=None, address=None):
    temp_dict = {head_dict[0]: telephone, head_dict[1]: address}
    return temp_dict

def load_data(name_of_file=None):
    temp_f_s = open(name_of_file, 'rb')
    temp_data = pickle.load(temp_f_s)
    temp_f_s.close()
    return temp_data


def dump_data(name_of_file=None, data_for_dump=None):
    temp_f_s = open(name_of_file, 'wb')
    pickle.dump(data_for_dump, temp_f_s)
    temp_f_s.close()


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
    else:
        print('Такой команды не существует')
print("Программа закрывается")
