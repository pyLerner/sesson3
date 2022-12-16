list_length = int(input('Введите количество цифр: '))
list_ = []

for i in range(list_length):
    element = int(input(f'Введите {i+1} элемент: '))
    list_.append(element)

list_.sort()
print(list_)
