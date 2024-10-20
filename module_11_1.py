import requests                           #импортируем библиотеку requests для работы с запросами
import pandas as pd                       #обработки и анализа структурированных данных, ее
                                          # название происходит от «panel data» («панельные данные»
import numpy as np                        # содержит многомерные структуры данных массива


# r = requests.get('https://skillbox.ru')
# print(r)                                  #получаем данные из указанного источника
# print(r.status_code)                      #код ответа на запрос (200-запрос прошел)
# print(r.headers['content-type'])          #заголовок страницы (тип страницы)
# print(r.encoding)                         #тип кодировки страницы
# print(r.content)                          #содержимое страницы в виде байтов
# print(r.text)                             #декодируем байты страницы в строки
# print(r.headers)                          #заголовок страницы (все параметры)
# print(r.json)                             #декодер JSON, на случай, если ответ приходит в виде данных JSON

#pandas
# pd.DataFrame({'A': [1, 2, 3]})
# print(pd.DataFrame({'A': [1, 2, 3]}))
# index = pd.date_range("1/1/2000", periods=8)
# print(index)                                #idx = pandas.date_range(start=None, end=None, periods=None,
#                                             #                       freq=None, tz=None, normalize=False,
#                                             #                       name=None, inclusive='both', *, unit=None, **kwargs)
# my_series = pd.Series([5, 6, 7, 8, 9, 10])  #cлева в колонке находятся индексы элементов, а справа — сами элементы.
# print(my_series)
# my_series2 = pd.Series(([5, 6, 7, 8, 9, 10]), index=['a', 'b', 'c', 'd', 'e', 'f'])
# print(my_series2)

#numpy
a = np.array([[1, 2, 3],[4, 5, 6]])            #input
print(a.shape)                                 #размеры массива, его форма
print(a.ndim)                                  #число измерений
print(a.size)                                  #кол-во элементов массива