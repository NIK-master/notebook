import pickle

head_dict = ("Телефон", "Адрес")
main_dict = {}
commands = '1.Добавить в справочник контактов\n2.Вывести значения по конаткту\n3.Закончить работу с словарём из справочника\n4.Вывести весь словарь\n5.Очстить словарь.'

tuple_of_numbers = [i for i in range(10)]


def buble_Sort_w_index(list_for_sorting=[], list_of_index=[]):
    flag = True
    while flag:
        flag = False
        for i in range(len(list_for_sorting) - 1):
            if list_for_sorting[i] > list_for_sorting[i + 1]:
                list_of_index[i], list_of_index[i + 1] = list_of_index[i + 1], list_of_index[i]
                list_for_sorting[i], list_for_sorting[i + 1] = list_for_sorting[i + 1], list_for_sorting[i]
                flag = True

def buble_Sort(list_for_sorting=[]):
    flag = True
    while flag:
        flag = False
        for i in range(len(list_for_sorting) - 1):
            if list_for_sorting[i] > list_for_sorting[i + 1]:
                list_for_sorting[i], list_for_sorting[i + 1] = list_for_sorting[i + 1], list_for_sorting[i]
                flag = True


tuple_of_numbers = (i for i in range(10))
def make_data(telephone=None, address=None):
    temp_dict = {head_dict[0]: telephone, head_dict[1]: address}
    return temp_dict


#[132, 113, 323] --> [113, 123, 132]
# 1. [1, 1, 3] --> buble_sort --> [1, 1, 3].
# 2. prev[1, 1, 3], cur[3, 1, 2] --> if prev[0] == prev[1] --> buble_sort(cur)
#                       1, 3, 2
#                      [1, 0, 2, 3]
#
#
#

def sort_for_number(dict_with_data={}):
    temp_telephones = []
    for name in dict_with_data:
        temp_telephones.append(dict_with_data[name][head_dict[0]])
    index_list_of_telephone = [i for i in range(len(temp_telephones))]
    len_of_numbers = [len(str(i)) for i in temp_telephones]
    buble_Sort(len_of_numbers)
    len_of_short_number = len_of_numbers[0]
    temp_letter = [0, 0]
    temp_ind_cur = index_list_of_telephone.copy()
    flag_not_comapre = False
    for i in range(len_of_short_number):
        temp_letter_current = [int(str(temp_telephones[j])[i]) for j in range(len(temp_telephones))]
        temp_letter_previous = temp_letter_current.copy()
        if i == 0:
            buble_Sort_w_index(temp_letter_current, temp_ind_cur)
        else:
            for ind_l in range(len(temp_letter_previous)):
                if ind_l + 1 >= len(temp_letter_previous):
                    break
                elif temp_letter_previous[ind_l] == temp_letter_previous[ind_l + 1]:
                    print(f'Меняю {ind_l} и {ind_l + 1} местами в символе {i}')
                    temp_ind = [ind_l, ind_l + 1]
                    temp_letter[0] = temp_letter_previous[ind_l]
                    temp_letter[1] = temp_letter_previous[ind_l + 1]
                    buble_Sort_w_index(temp_letter, temp_ind)
                    temp_ind_cur.pop(ind_l)
                    temp_ind_cur.pop(ind_l)
                    temp_ind_cur.insert(ind_l - 1, temp_ind[0])
                    temp_ind_cur.insert(ind_l, temp_ind[1])
                else:
                    flag_not_comapre = True
        if flag_not_comapre:
            break
    index_list_of_telephone.clear()
    index_list_of_telephone = temp_ind_cur.copy()
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


def buble_Sort(list_for_sorting=[], list_of_index=[]):
    flag = True
    while flag:
        flag = False
        for i in range(len(list_for_sorting) - 1):
            if list_for_sorting[i] > list_for_sorting[i + 1]:
                list_of_index[i], list_of_index[i + 1] = list_of_index[i + 1], list_of_index[i]
                list_for_sorting[i], list_for_sorting[i + 1] = list_for_sorting[i + 1], list_for_sorting[i]
                flag = True


def sort_number(telephone_number = None, dict_with_data = None):
    temp_telephones = []
    for name in dict_with_data:
        temp_telephones.append(dict_with_data[name][head_dict[1]])
    index_list_of_telephone = [i for i in range(len(temp_telephones))]
    first_letter = [str(temp_telephones[i])[0] for i in range(len(temp_telephones))]
    buble_Sort(first_letter, index_list_of_telephone)
    names = list(dict_with_data.keys())
    count_ind = 0
    temp_dict = {}
    for name in dict_with_data:
        temp_dict.update({names[count_ind]: make_data(dict_with_data)) dict_with_data[name][head_dict[0]]]
        count_ind = 1
    print(temp_dict)
    print(index_list_of_telephone)
    print(first_letter)

