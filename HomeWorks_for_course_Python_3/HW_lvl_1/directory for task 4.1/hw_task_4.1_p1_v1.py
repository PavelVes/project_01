# Домашняя работа по задаче 4.1 курса Python 3

# Задача 4.1. (Полное условие)
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:


# Решение 1. (п.1)
print('\n') # Пустая строка для разделения вывода в консоли
# п.1 - создадим и заполним новую таблицу

import sqlite3


connection = sqlite3.connect('teachers_.db') # БД в основной папке
cursor = connection.cursor()

# Создаем новую таблицу в БД (+ проверка на наличие,
# в т.ч. чтобы не было постоянных ошибок при перезапуске кода)
cursor.execute('''CREATE TABLE IF NOT EXISTS Students ( 
Student_Id INT NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INT NOT NULL PRIMARY KEY
);''')

connection.commit()


# Заполним новую таблицу данными.
students = [
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4')]

cursor.executemany('INSERT INTO Students VALUES(?, ?, ?);', students)

connection.commit()
connection.close()

# Конец Решения 1 (п.1)
print('\n') # Пустая строка для разделения вывода в консоли
