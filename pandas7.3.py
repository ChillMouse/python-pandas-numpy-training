import pandas as pd

books = pd.read_excel('/home/chillmouse/Desktop/python/nstu/books.xlsx')
print(books.sort_values(by='BookName', kind='stable'))
print(books.sort_values(by='Rate', kind='stable', ascending=False)[:10:])
print('By year')
print(books[books['Year'].str.contains(r'(18[789]\d|1900)', regex=True)].sort_values(by='Year'))

print(books['Author'].value_counts())

print(books[books['Rate'] > 2])

print(books.loc[books['Author'] == str(input('Введите имя автора: '))])


# 3. Используя данные сайта https://www.100bestbooks.ru/ , сформировать файл Excel с выборкой 100 книг. 
# Загрузить данные файла excel, используя pandas. Отсортируйте данный список по названию книги. Используя полученные данные вывести:
# • десять книг с наибольшем количеством голосов;
# • данные за 1870-1900 года;
# • количество книг каждого автора;
# • наименования книг со средним баллов выше 2;
# • все произведения автора по введенному имени. (запрос на ввод имени)  