# https://github.com/natkaida/pandas/tree/main/challenge_1
# https://proglib.io/p/samouchitel-po-pandas-dlya-nachinayushchih-chast-25-osnovy-analiza-dannyh-s-pandas-2023-07-24
# https://proglib.io/p/instrumenty-data-zhurnalista-1-jupyter-notebook-i-biblioteka-pandas-2021-04-05

import pandas as pd

# создаем DataFrame из словаря
data = {'Имя': ['Егор', 'Анна', 'Никита', 'Марина'],
        'Возраст': [25, 30, 28, 35],
        'Город': ['Москва', 'Самара', 'Ростов', 'Нижний Новгород']}
df = pd.DataFrame(data)
# выводим DataFrame на экран 
# print(df)

data = [35000, 6000, 3000, 2000]
labels = ['Ноутбуки', 'Мониторы', 'Принтеры', 'Клавиатуры']
series = pd.Series(data, index=labels)
# print(series['Принтеры'])  # выводим значение 3000, обращаясь к элементу с меткой 'Принтеры'

# создаем MultiIndex с двумя уровнями
index = pd.MultiIndex.from_tuples([('Москва', 'Ноутбуки'), ('Москва', 'Настольные ПК'),
                                   ('Санкт-Петербург', 'Ноутбуки'), ('Санкт-Петербург', 'Настольные ПК')])
# создаем DataFrame с MultiIndex
data = [[1000, 200000], [3000, 400000], [5000, 600000], [7000, 800000]]
df = pd.DataFrame(data, index=index, columns=['Продажи', 'Прибыль'])
# print(df) 


dataframe = pd.read_csv('data.csv')
series_1 = dataframe['столбец_1']
series_2 = dataframe['столбец_2']
series_3 = dataframe['столбец_3']

# print(series_1)
# print(series_2)
# print(series_3)
# print(dataframe)
# '''
# Если в head() и tail() не передавать нужное количество строк, по умолчанию
# будут выведены первые (или последние) 5 строк.
# '''
# # Вывод первых 2 строк DataFrame
# print(dataframe.head(2))
# # Вывод последних 2 строк DataFrame
# print(dataframe.tail(2))


# читаем Excel файл
# pip install openpyxl
df = pd.read_excel('data.xlsx')
# выводим DataFrame
print(df)
# print(df.shape)
print(f'mean age = {df['AGE'].mean():.1f}')

# вывод основных статистических показателей
print(df['AGE'].describe())

