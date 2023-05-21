# Домашняя работа по задаче 4.1 курса Python 3

# Задача 4.1. (Первая часть условия)
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4



# Решение 2. (п.1)
print('\n') # Пустая строка для разделения вывода в консоли
# п.1 - напишем ф-ю для внесения данных в таблицу

import sqlite3
path = 'teachers_.db'


# Создадим, обычным образом, новую таблицу для БД.
connection = sqlite3.connect(path) # БД в основной папке
cursor = connection.cursor()
# Создаем новую таблицу в БД (+ проверка на наличие,
# в т.ч. чтобы не было постоянных ошибок при перезапуске кода)
cursor.execute('''CREATE TABLE IF NOT EXISTS Students ( 
Student_Id INT NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INT NOT NULL PRIMARY KEY
);''')
connection.commit()
connection.close()



# Напишем ф-ю для заполнения Таблицы в БД.
def insert_into_table(dataset: list|tuple, table_name: str, path_to_db: str, replace=False) -> None:
    '''Добавляет данные в указанную Таблицу БД.
    
    Принимает список или список кортежей данных.

    (replace=True - Перезапишет уже существующие значния (по умолчанию: проигнорирует))
    '''
    try: 
        nested = False # Флаг для разных команд execut...()
        # Посчитаем, сколько д.б. столбцов в таблице (из входящих значений)
        if isinstance(dataset[0], list|tuple): # Проверяем на вложение (для кол-ва столбцов)
            if len(min(dataset)) == len(max(dataset)): # Проверяем на совпадение длин вложений
                count = len(dataset[0]) # Если внутри списки, считаем кол-во эл. внутри любого
                nested = True # Если значений несколько
            else: # Возвращаем Ошибку
                print('ОШИБКА: Не совпадают количества Столбцов для таблицы')
                raise Exception
        else: count = len(dataset) # Иначе, считаем кол-во эл. внутри единственного списка
        
        # Составим запрос к БД (с проверокой на игнорирование или замену имеющихся значений)
        if replace == True: add_ = 'OR REPLACE'
        else: add_ = 'OR IGNORE'
        req = f"INSERT {add_} INTO {table_name} VALUES({', '.join(list('?'*count))});"
        
        # Подключимся к БД, выполним вставку, сохранимся и отключимся от БД
        con = sqlite3.connect(path_to_db) # Подключаемся к БД
        cur = con.cursor() # Создаем "указатель"

        if nested: cur.executemany(req, dataset) # Выполняем запрос к БД для списков
        else: cur.execute(req, dataset) # Выполняем запрос к БД для 1 списка

        con.commit() # Сохраняем обновленную БД
        con.close() # Отключаемся от БД.
        return f'Данные успешно добавлены в Таблицу "{table_name}"' # м.б. убрать эту строку
    except: print('Неверный запрос для БД') # 



# Проверка Решения 2. (п.1)
table_ = 'Students'

# Заполним новую таблицу данными.
students = [
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4',)]

# student = '201', 'Иван', '1', # Для примера - 1 студент


print(insert_into_table(students, table_, path)) # Проверка на "успешное" выполнение


# Конец Решения 2. (п.1)
print('\n') # Пустая строка для разделения вывода в консоли
