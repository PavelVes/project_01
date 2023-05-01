# Домашняя работа по задачи 1.2 п.А  курса Python 3

# Задача 1.2.

# Пункт A. (Условие)
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]


# Решение 1
print('\n') # Пустая строка для разделения вывода в консоли

import random # Раз уж речь про случайный выбор.


count = 3 # Указываем количество песен для подсчета
time = 0
for i in range(count):
    num_song = random.randint(0, len(my_favorite_songs) - 1) # Определяем случайную песню
    time_song = my_favorite_songs[num_song][1] # Выбираем значение длительности выбранной песни
    minuts = int(time_song) # Округляем время до минут
    seconds = int((time_song - minuts + .00001) * 100) # Получаем остаток секунд в целых числах
    time_in_seconds = minuts * 60 + seconds # Получаем полное время в секундах
    time += time_in_seconds # Суммируем общее время
    #print(num_song, time_song, minuts, seconds, time_in_seconds, time, sep=' \n', end=' \n\n')
    # Выше временный проверочный Print для отладки.


print('Три песни звучат {0} минут'.format(time//60 + time % 60 / 100))
# Тут логичней вместо "три" подставить 'count', но -> 
# тогда нужна функция для исправления окончаний последующих слов в русском языке 


# Конец решения




# Ну, или проще: поискать модуль для работы со временем (преобразованием)
# Или написать соответствующую функцию: (Исходя из того, что агрумент изначально будет правильным)

# Решение 2.
def convert_time_to_seconds(time: float): # !Нужна проверка на тип и что бы дробная часть была меньше 60.
    '''Преобразование времени формата мин.сек в секунды'''
    time = float(round(time, 2)) + 0.00001
    minuts = int(time) # Округляем время до минут
    seconds = int((time - minuts) * 100) # Получаем остаток секунд в целых числах
    time_in_seconds = minuts * 60 + seconds # Получаем полное время в секундах
    #print('func', time, minuts, seconds, time_in_seconds, sep='\n', end='\n\n') # временно для проверки
    return time_in_seconds


def convert_seconds_to_time(seconds: int): # Тут тоже без проверки - формально, для примера.
    '''Преобразование количества секунд во время формата мин.сек'''
    time = seconds // 60 + seconds % 60 / 100 # Тут еще нужна проверка на ноль поле запятой, -> + еще 0
    return time


# Проверка работы функций (временные строки)
# f = convert_time_to_seconds
# time = 10.59
# a = f(time)

# f1 = convert_seconds_to_time
# seconds = 69
# b = f1(seconds)

# print(' time1= ', time, '\n', 'secods1 = ', a, '\n', 'secods2 = ', seconds, '\n', 'time2 = ', b)



# Тогда решение задачи будет выглядеть следующим образом:
print('\n') # Пустая строка для разделения вывода в консоли

count = 3 # Указываем количество песен для подсчета
time = 0
for i in range(count):
    num_song = random.randint(0, len(my_favorite_songs) - 1) # Определяем случайную песню
    time_song = my_favorite_songs[num_song][1] # Выбираем значение длительности выбранной песни
    time += convert_time_to_seconds(time_song)
    #print(num_song, time_song, sep=' \n', end=' \n\n') # временно проверка значений

print('Три песни звучат ', convert_seconds_to_time(time), ' минут')





print('\n') # Пустая строка для разделения вывода в консоли