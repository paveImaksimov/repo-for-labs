# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator = ','):
    participants_first_group = set(participants_first_group.split(separator))
    participants_second_group = set(participants_second_group.split(separator))
    a = list(participants_first_group.intersection(participants_second_group))
    a.sort()
    return a
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
