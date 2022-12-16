#  печать уникальных символов строки пользователя

input_str = input('Введите элементы списка через запятую, точку с запятой или обратный слэш ')
delimeter = ','     # по умолчанию

if ';' in input_str:
    delimeter = ';'
elif '/' in input_str:
    delimeter = '/'

input_str = input_str.replace(' ', '').split(delimeter) # убрали пробелы, разбили строку в список по разделителю
end_list = str(set(input_str))
print(end_list.replace('{','').replace('}','').replace('\'',''))
