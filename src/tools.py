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