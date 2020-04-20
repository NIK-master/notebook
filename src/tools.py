import pickle

head_dict = ("Телефон", "Адрес")
main_dict = {}
commands = '1.Добавить в справочник контактов\n2.Вывести значения по конаткту\n3.Закончить работу с словарём из справочника\n4.Вывести весь словарь\n5.Очстить словарь.'

tuple_of_numbers = [i for i in range(10)]


def buble_Sort(list_for_sorting=[], list_of_index=[]):
    flag = True
    while flag:
        flag = False
        for i in range(len(list_for_sorting) - 1):
            if list_for_sorting[i] > list_for_sorting[i + 1]:
                list_of_index[i], list_of_index[i + 1] = list_of_index[i + 1], list_of_index[i]
                list_for_sorting[i], list_for_sorting[i + 1] = list_for_sorting[i + 1], list_for_sorting[i]
                flag = True


def make_data(telephone=None, address=None):
    temp_dict = {head_dict[0]: telephone, head_dict[1]: address}
    return temp_dict


def sort_for_number(dict_with_data={}):
    temp_telephones = []
    for name in dict_with_data:
        temp_telephones.append(dict_with_data[name][head_dict[0]])
    index_list_of_telephone = [i for i in range(len(temp_telephones))]
    first_letter = [int(str(temp_telephones[i])[0]) for i in range(len(temp_telephones))]
    buble_Sort(first_letter, index_list_of_telephone)
    names = list(dict_with_data.keys())
    count_ind = 0
    temp_dict = {}
    for i in range(len(dict_with_data)):
        temp_dict.update({names[index_list_of_telephone[count_ind]]: make_data(dict_with_data[names[index_list_of_telephone[count_ind]]][head_dict[0]], dict_with_data[names[index_list_of_telephone[count_ind]]][head_dict[1]])})
        count_ind += 1
    dump_data('save_data.dat', temp_dict)



def load_data(name_of_file=None):
    temp_f_s = open(name_of_file, 'rb')
    temp_data = pickle.load(temp_f_s)
    temp_f_s.close()
    return temp_data


def dump_data(name_of_file=None, data_for_dump=None):
    temp_f_s = open(name_of_file, 'wb')
    pickle.dump(data_for_dump, temp_f_s)
    temp_f_s.close()
