# не уверен в решении, так как вроде бы уникальность в этой задаче не требуется

input_str_1 = input('Введите элементы 1-го списка через запятую ')
input_str_2 = input('Введите элементы 2-го списка через запятую ')

delimeter = ','     # по умолчанию

input_str_1 = input_str_1.replace(' ', '').split(delimeter)  # убрали пробелы, разбили строку в список по разделителю
input_str_2 = input_str_2.replace(' ', '').split(delimeter)

end_set_1 = set(input_str_1)
end_set_2 = set(input_str_2)

end_set = end_set_1.difference(end_set_2)  # Набор элементов, которых нет во втором списке
end_str = str(end_set)
print(end_str.replace('{','').replace('}','').replace('\'',''))  # просто красивый вывод на печать