import pandas as pd
import numpy.random as rand
import numpy as np

a = pd.Series(rand.randint(1, 100, 10))
b = pd.Series(rand.randint(1, 100, 8))

print(a.add(b))
print(a.sub(b))
print(a.multiply(b))

dict_groups = {
    'group1': {
        'student1': {"name": 'Анциферов Максим Дмитриевич'},
        'student2': {"name": 'Батова Кристина Алексеевна'},
        'student3': {"name": 'Бут Валерия Сергеевна'}
    },
    'group2': {
        'student1': {"name": 'Гринда Алёна Игоревна'},
        'student2': {"name": 'Гунгер Кирилл Андреевич'},
        'student3': {"name": 'Деменев Владислав Вячеславович'}
    },
    'group3': {
        'student1': {"name": 'Долбик Артём Евгеньевич'},
        'student2': {"name": 'Донельчук Артём Вячеславович'},
        'student3': {"name": 'Духов Денис Юрьевич'}
    },
    'group4': {
        'student1': {"name": 'Итегелова Виктория Олеговна'},
        'student2': {"name": 'Каменева Наталья Анатольевна'},
        'student3': {"name": 'Картанкова Лидия Евгеньевна'}
    }
}

df = pd.DataFrame.from_dict(dict_groups)
for group in df:
    for student in df[group]:
        print(student)
        r = rand.randint(1, 101, 3)
        student['math'] = r[0]
        student['eng'] = r[1]
        student['prog'] = r[2]
print(df)

for group in df:
    for student in df[group]:
        student['overall'] = student['math'] + student['eng'] + student['prog']
        print(student)
overalls = list()
for row in df.values.ravel():
    overalls.append(row['overall'])
print('Статистика:')
for group in df:
    for student in df[group]:
        if student['overall'] == np.max(overalls):
            print(student)

for group in df:
    for student in df[group]:
        if student['overall'] == np.min(overalls):
            print(student)

for group in df:
    for student in df[group]:
        if student['name'].startswith('Бут'):
            print(student)
# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)
 
# Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
 
# Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
print(df['group1'])

# 1. Создать две серии со случайным целочисленным значением элементов. Одна серия сдержит 10 элементов, вторая 8 элементов. Произвести арифметические действия с двумя сериями (сложение, вычитание, умножение).
# 2. Создать набор данных, состоящий из четырех групп, в каждой группе по три студента (ФИО). Добавить информацию успеваемости по трем предметам (баллы от 0 до 100 сформированные случайным набором элементов целочисленных значений). Вычислить общий балл по трем предметам и добавить данные в набор. Используя полученные данные вывести:
# • статистические сведения о студентах;
# • информацию о студенте с максимальным общим баллом;
# • информацию о студенте с минимальным общим баллом;
# • информацию о студенте используя его фамилию;
# • информацию по успеваемости одной группы.
# 3. Используя данные сайта https://www.100bestbooks.ru/ , сформировать файл Excel с выборкой 100 книг. 
# Загрузить данные файла excel, используя pandas. Отсортируйте данный список по названию книги. Используя полученные данные вывести:
# • десять книг с наибольшем количеством голосов;
# • данные за 1870-1900 года;
# • количество книг каждого автора;
# • наименования книг со средним баллов выше 2;
# • все произведения автора по введенному имени. (запрос на ввод имени)  
# 4. Загрузить данные по лучшим фильмам. В качестве источника данных можно использовать ресурс wikipedia. Используя полученные данные вывести:
# • десять лучших фильмов;
# • наименования фильмов и год по запросу жанра фильма;
# • информацию за выбранный промежуток времени;
# • количество фильмов по режиссёрам;
# • количество фильмов по жанрам.
# Сохранить данные в таблице Excel. 
