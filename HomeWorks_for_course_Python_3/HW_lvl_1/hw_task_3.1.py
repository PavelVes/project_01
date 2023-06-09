# Домашняя работа по задаче 3.1 курса Python 3

# Задача 3.1. (Условие)
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

print('\n') # Пустая строка для разделения вывода в консоли


# Решение. 
# можно по-разному подходить к данной задаче (но, раз надо проявить фантазию :)....)
 
# Что нам нужно?
# + Нужно создать Базовый Класс в коротом определить основные матричные методы
# + Создать инициатор, в котором будет создана матрица (список списков)
# + Создать вывод (__str__), что бы можно было видеть, что мы имеем, просто напечатав объект

# Далее: создать методы из задания (+ свои):
# 1. + Замена строки (столбца) значениями (самих значений в матрицу в виде строки или столбца)
# 2. + Добавление (изменение) значения для конкретной ячейки (новые значения)
# 3. + Добавление новых строк (столбцов) со значениями к уже имеющимся (расширение матрицы)
# 4. + Сдвиг Строки (столбца) (Шифт) внутри Матрицы 
# 5. + Удаление Строки (Столбца) и/или ячейки (вместе со строкой и столбцом одновременно)
# 6. + Поменять столбцы (строки или ячейки) местами (по заданным индексам)
# 7. + Отражение по строкам (столбцам), - (зеркальная симметрия)
# 8. + Поворот на 90, по и против часовой стрелки
# 9. + Транспонирование (диагональная симметрия)
# 10. + Сортировка (как в екселе) по конкретной строке (столбцу), с сохранением отношения позиций эл. 
# 11. + Возвращение "куска" матрицы в виде Матрицы (по индексам начала и конца) + (по индексу начала и размеру)

# Часть 2. 
# 1. + Создать дочерний класс (согласно заданию), чисто для цифр
# 2. + Определить в нем свои (математические) методы (для сложения, умножения и т.п.,) для:
#  а. + Матрицы и Матрицы
#  б. + Матрицы и числа
#  в. + Матрицы (конкретной строки/стобца) с заданной строкой/столбцом  
#  г. + Матрицы (всех строк/столбцов) с заданной строкой/столбцом
# 3. + Добавить свои методы для сложения числа со строкой, столбцом или ячейкой.



class BaseMatrix():
    '''Базовая Матрица, принимающая в себя любые значения и типы данных''' 

    def __init__(self, column:int = 1, row: int = 1, filling=None): # Создаем Инициализатор и таблицу
        # Проверка на размерность (int) и не отрицательные значения
        if type(column) == int and type(row) == int and column > 0 and row > 0: 
            self._column = column
            self._row = row
            self._filling = filling
            # print(f'Создана Матрица {self._column} x {self._row}, состоящая из {self._filling}')
            self._matrix = [[filling for col in range(column)] for row in range(row)] # ч-з список списков
        else: raise IndexError('Размеры матрицы должны указываться только положительными целыми числами')


    # пере_Определим некоторые "магические методы" для удобства.
    
    def __repr__(self): # Определим (выведем) отладочную информацию
        return f'{self.__class__}: ({self.column} x {self.row})'
    
    def __str__(self): # Определим (выведем) информацию для пользователя (собственно вид Матрицы)
        return '\n'.join([f'{row}' for row in self._matrix]) # Каждую "строку" отдельной строкой
    
    def __len__(self): # Переопределим способ подсчета длины (тут: по кол-ву ячеек в матрице)
        return self._row * self._column


    # Напишем 2 ф-и для проверки индексов (стр. и стлб.), чтобы не повторять эти проверки в каждом методе
    # М.б их надо было как-то в декораторы превратить, но я пока не понимаю - как. (?)
    
    def _check_row_index(self, row_number:int = 0, min_index=True) -> int: # ф-я для проверки индекса строк
        '''Проверяем индекс строки на допустимое значение и тип
        
        min_index = True (по умолчанию) - допускает отрицательные индексы (иначе мин. = 0)'''
        if min_index == True: _min_ind_ = -(self._row) # Проверка на мин. индекс
        else: _min_ind_ = 0 # В некоторых методах отрицательные индексы не правильно работают (для них сделано)

        if type(row_number) == int: # Сначала проверяем на ТИП значения
            if _min_ind_ <= row_number < (self._row): # Проверка индекса (внутри размеров, в обе стороны)
                return row_number
            else: raise IndexError(f'Индекс {row_number} для строки вне допустимых пределов')
        else: raise TypeError(f'Индекс "{row_number}" должен быть целым числом')


    def _check_column_index(self, column_number:int = 0, min_index=True) -> int: # ф-я для проверки индекса строк
        '''Проверяем индекс столбца на допустимое значение и тип
        
        min_index = True (по умолчанию) - допускает отрицательные индексы (иначе мин. = 0)'''
        if min_index == True: _min_ind_ = -(self._column) # Проверка на мин. индекс
        else: _min_ind_ = 0 # В некоторых методах отрицательные индексы не правильно работают (для них сделано)

        if type(column_number) == int:  # Сначала проверяем на ТИП значения
            if _min_ind_ <= column_number < (self._column): # Проверка индекса (внутри размеров, в обе стороны)
                return column_number
            else: raise IndexError(f'Индекс {column_number} для столбца вне допустимых пределов')
        else: raise TypeError(f'Индекс "{column_number}" должен быть целым числом')


    # Создадим методы для получения числа строк, солбцов и общего размера

    @property
    def column(self) -> int: # get_column_count
        '''Получаем кол-во Колонок в Матрице'''
        return self._column
    
    @property
    def row(self) -> int: # get_row_count
        '''Получаем кол-во Строк в Матрице'''
        return self._row
    
    @property
    def size(self) -> tuple: # get_size_count (Кортеж размеров)
        '''Получаем кортеж размера Матрицы'''
        return (self._column, self._row,)

    
    # Создадим методы возврата ячейки, строки или столбца, или куска матрицы по индексу(ам).

    def get_row(self, row_number:int=0) -> list:
        '''Возвращает указанную строку в виде списка значений'''
        self._check_row_index(row_number) # Проверка индекса стр. на тип и значение
        return self._matrix[row_number]


    def get_column(self, column_number:int=0) -> list:
        '''Возвращает указанный столбец в виде списка значений'''
        self._check_column_index(column_number) # Проверка индекса стлб. на тип и значение
        return [row[column_number] for row in self._matrix]


    def get_cell(self, column_number:int=0, row_number:int=0):
        '''Возвращает значение указанной ячейки'''
        self._check_column_index(column_number) # Проверка индекса стлб. на тип и значение
        self._check_row_index(row_number) # Проверка индекса стр. на тип и значение
        return self._matrix[row_number][column_number]
    

    def get_matrix_part_by_indexes(self, column_start:int=0, row_start:int=0, column_end:int=0, row_end:int=0):
        '''Возвращает часть матрицы, по индексам начала и конца (включительно)'''
        self._check_column_index(column_start, 0) # Проверка индекса 1 cстлб. на тип и значение
        self._check_row_index(row_start, 0) # Проверка индекса 1 стр. на тип и значение
        self._check_column_index(column_end, 0) # Проверка индекса 2 стлб. на тип и значение
        self._check_row_index(row_end, 0) # Проверка индекса 2 стр. на тип и значение
        
        _NewBaseMatrix = BaseMatrix((column_end - column_start + 1), (row_end - row_start + 1)) # Создадим Матрицу для возврата
        for row in range(row_start, row_end + 1):
            _new_row = [] # Создадим пустую строку для будущей матрицы
            for column in range(column_start, column_end + 1):
                _new_row.append(self._matrix[row][column]) # заполним строку значениями (элем. столбца)
            _NewBaseMatrix.replace_row(_new_row, (row - row_start)) # добавим заполненную строку в новую матрицу (как строку)
        return _NewBaseMatrix # Возвращает Тип = BaseMatrix


    def get_matrix_part_by_size(self, column_start:int=0, row_start:int=0, columns_count:int=1, rows_count:int=1):
        '''Возвращает часть матрицы, по стартовым индексам и указанному размеру (включительно)
        
        При превышении размера матрицы, вернет от указанного индекса и до последнего'''
        self._check_column_index(column_start, 0) # Проверка индекса 1 cстлб. на тип и значение
        self._check_row_index(row_start, 0) # Проверка индекса 1 стр. на тип и значение

        if columns_count < 1 or rows_count < 1: # Размеры должны быть положительными и больше 0
            raise IndexError('Количество Столбцов и/или Строк для выборки должно быть больше 0')
        else: # Выполняем основной код.
            if (column_start + columns_count -1) >= self.column: # Зададим индекс последнего столбца
                column_end = self.column -1
            else: column_end = column_start + columns_count -1
            
            if (row_start + rows_count -1) >= self.row: # Зададим индекс последней строки
                row_end = self.row -1
            else: row_end = row_start + rows_count -1
            
            return self.get_matrix_part_by_indexes(column_start, row_start, column_end, row_end)
    

    # Создадим методы для изменения (добавления) значений в Матрице (не меняют размеры Матрицы)

    def replace_row(self, row: list|tuple, row_number:int=0): # Метод для замены строки
        '''Заменяет значения в указанной строке на заданные'''
        self._check_row_index(row_number) # Проверка индекса стр. на тип и значение
        if len(row) == self._column: # Проверка на совпадение длин списков (входящего и существующего)
            for i, value in enumerate(row):
                self._matrix[row_number][i] = value
        else: raise ValueError('Не совпадение с количеством столбцов')
        return self


    def replace_column(self, column: list|tuple, column_number:int=0): # Метод для замены столбца
        '''Заменяет значения в указанном столбце на заданные'''
        self._check_column_index(column_number) # Проверка индекса стлб. на тип и значение
        if len(column) == self._row: # Проверка на совпадение длин списков (входящего и существующего)
            for i, value in enumerate(column):
                self._matrix[i][column_number] = value
        else: raise ValueError('Не совпадение с количеством строк')
        return self


    def replace_cell(self, value, column_number:int=0, row_number:int=0): # Метод для замены Ячейки
        '''Заменяет значение выбранной ячейки на заданное'''
        self._check_column_index(column_number) # Проверка индекса стлб. на тип и значение
        self._check_row_index(row_number) # Проверка индекса стр. на тип и значение
        self._matrix[row_number][column_number] = value
        return self


    # Создадим методы добавления новых строки и столбца по индексу (!_Меняют размеры матрицы_!)

    def insert_row(self, row: list|tuple, row_number:int=0): # Метод для добавления строки
        '''Добавляет новую строку со значениями по индексу. Меняет размерность Матрицы!'''
        self._row += 1 # Увеличим размер Матрицы (кол-во строк)
        self._check_row_index(row_number, 0) # Проверка индекса стр. на тип и значение
        if len(row) == self._column: # Проверка на совпадение длин списков (входящего и существующего)
            self._matrix.insert(row_number, list(row)) # Вставляем новую строку
        else: raise ValueError('Не совпадение с количеством столбцов')
        return self


    def insert_column(self, column: list|tuple, column_number:int=0): # Метод для замены столбца
        '''Добавляет новый столбец со значениями по индексу. Меняет размерность Матрицы!'''
        self._column += 1 # Увеличим размет Матрицы (кол-во столбцов)
        self._check_column_index(column_number, 0) # Проверка индекса стлб. на тип и значение
        if len(column) == self._row: # Проверка на совпадение длин списков (входящего и существующего)
            for i, value in enumerate(column): # Вставляем новый столбец
                self._matrix[i].insert(column_number, value)
        else: raise ValueError('Не совпадение с количеством строк')
        return self


    # Добавим методы для удаления Строки, Столбца и Ячейки (вместе со строкой и столбцом) из Матрицы

    def del_row(self, row_number:int):
        '''Удаляет указанную строку из Матрицы. Меняет размерность Матрицы'''
        self._check_row_index(row_number) # Проверка индекса стр. на тип и значение
        self._matrix.pop(row_number) # Удалим строку по индексу
        self._row -= 1 # Уменьшим размер Матрицы (кол-во строк)
        if self._row < 1: print('Вы удалили последнюю строку Матрицы')
        return self


    def del_column(self, column_number:int):
        '''Удаляет указанный столбец из Матрицы. Меняет размерность Матрицы'''
        self._check_column_index(column_number) # Проверка индекса стлб. на тип и значение
        for i in range(self._row):
            self._matrix[i].pop(column_number) # Удалим столбец по индексу
        self._column -= 1 # Уменьшим размер Матрицы (кол-во строк)
        if self._column < 1: print('Вы удалили последний столбец Матрицы')
        return self


    def del_cell(self, column_number:int, row_number:int):
        '''Удаляет строку и столбец из Матрицы по индексу ячейки. Меняет размерность Матрицы'''
        self.del_row(row_number)
        self.del_column(column_number)
        return self


    # Добавим методы для Реверса (Зеркальности)

    def reverse_by_row(self):
        '''Зеркально разворачивает Матрицу по ширине'''
        for i in range(self._row):
            self._matrix[i].reverse()
        return self


    def reverse_by_column(self):
        '''Зеркально разворачивет Матрицу по высоте'''
        self._matrix.reverse()
        return self

    
    # Добавим методы сдвига строк (столбцов) внутри Матрицы

    # Сначала напишем просто ф-ю для сдвига эл.списка, чтобы подставить ее в методы (ниже).
    @staticmethod # Или - использовать отдельно
    def list_shift(_list_:list|tuple, reverse=True)-> list:
        '''Сдвигает все элементы списка на один вперед (меняет первый на последний)
        
        reverse = False - Сдвиг в обратную сторону'''
        _list_ = list(_list_) # Сделаем списком (на случай кортежа или др.)
        if reverse == True:
            _temp_ = _list_[-1] # Временная переменная (последнее значение)
            for i in range(len(_list_)): # Проходим по списку
                try:
                    _list_[-(i+1)] = _list_[-(i+1) - 1] # Проходим по списку в обратном порядке
                except: break # при ошибке (не сущестующего индекса) прерываем цикл
            _list_[0] = _temp_ # Меняем первый элемент на последний 

        else:
            _temp_ = _list_[0] # Временная переменная (первое значение)
            for i in range(len(_list_)): # Проходим по списку
                try:
                    _list_[i] = _list_[i+1] # Переприсваиваем значения (на следующее)
                except: break # Последнее значение не поменяется (останется 2 одинаковых)
            _list_[-1] = _temp_ # Меняем последний элемент на первый 

        return _list_ # Возвращаем измененный список
            

    def shift_rows(self, reverse=True): # Для сдвига вверх-вниз по Матрице 
        '''Cдвигает строки Матрицы на одну вниз
        (последняя строка станет первой)
        
        reverse = False - сдвиг вверх'''
        self.list_shift(self._matrix, reverse)
        return self


    def shift_columns(self, reverse=True): # !!! Не доделано еще!
        '''Сдвигает столбцы Матрицы на один вправо
        (последний столбец станет первым)
        
        reverse = False - сдвиг влево'''
        for row in range(self.row):
            self.list_shift(self._matrix[row], reverse)
        return self


    # Добавим методы для замены двух строк (столбцов, ячеек) местами (по индексам)

    def change_rows(self, row1:int, row2:int):
        '''Меняте две строки местами. По их индексу.'''
        self._check_row_index(row1) # Проверка индекса 1 стр. на тип и значение
        self._check_row_index(row2) # Проверка индекса 2 стр. на тип и значение
        self._matrix[row1], self._matrix[row2] = self._matrix[row2], self._matrix[row1]
        return self


    def change_columns(self, column1:int, column2:int):
        '''Меняте две строки местами. По их индексу.'''
        self._check_column_index(column1) # Проверка индекса 1 стлб. на тип и значение
        self._check_column_index(column2) # Проверка индекса 2 стлб. на тип и значение
        for i in range(self.row): # Для каждой строки попарно меняем значения по индексам
            self._matrix[i][column1], self._matrix[i][column2] = \
                self._matrix[i][column2], self._matrix[i][column1]
        return self
            

    def change_cells(self, column1:int, row1:int, column2:int, row2:int):
        '''Меняте две строки местами. По их индексу.'''
        self._check_column_index(column1) # Проверка индекса 1 стлб. на тип и значение
        self._check_row_index(row1) # Проверка индекса 1 стр. на тип и значение
        self._check_column_index(column2) # Проверка индекса 2 стлб. на тип и значение
        self._check_row_index(row2) # Проверка индекса 2 стр. на тип и значение
        self._matrix[row1][column1], self._matrix[row2][column2] = \
                self._matrix[row2][column2], self._matrix[row1][column1]
        return self

    
    # Добавим методы для сортировки Матрицы по Строке или Столбцу (в обе стороны) 

    def sorted_by_row(self, row_index: int=0, reverse=True):
        '''Сортирует Матрицу по указанной строке, по возрастанию. Сохраняет отношение позиций элементов.
          
        reverse = False - Меняет направление сортировки'''
        self._check_row_index(row_index) # Проверка индекса стр. на тип и значение
        if reverse == True: # Метод для Прямой сортировки (по возрастанию)
            for i in range(self.column - 1): # Пузырьковая стортировка по элементам конкретной строки
                for j in range(self.column - i - 1): # Проходим по кол-ву Столбцов (т.к. см. строку)
                    if isinstance(self._matrix[row_index][j], int|float) and \
                        isinstance(self._matrix[row_index][j+1], int|float): # Для корректного сравнения любых чисел
                        if self._matrix[row_index][j] > self._matrix[row_index][j+1]: # Сравниваем если 2 числа
                            self.change_columns(j, j+1) # Меняем данные столбцы местами
                    else: # Если два соседних элемента не являются числами (и все пр.), то сравниваем их ч-з Тип строки.
                        if str(self._matrix[row_index][j]) > str(self._matrix[row_index][j+1]): # Тут сразу сравниваем значения строк
                            self.change_columns(j, j+1) # а меняем оригинальные элементы (столбцы)
        else:
            self.sorted_by_row(row_index, True) # Для обратной сортировки, вызовем Прямую
            self.reverse_by_row() # И просто отзеркалим всю Матрицу (правильнее бы: взять код выше с другим знаком сравнения)
        return self # Возвращаем сортированную Матрицу
    

    def sorted_by_column(self, column_index: int=0, reverse=True):
        '''Сортирует Матрицу по указанному столбцу, по возрастанию. Сохраняет отношение позиций элементов.
          
        reverse = False - Меняет направление сортировки'''
        self._check_column_index(column_index) # Проверка индекса стлб. на тип и значение
        if reverse == True: # Метод для Прямой сортировки (по возрастанию)
            for i in range(self.row - 1): # Пузырьковая стортировка по элементам конкретного столбца
                for j in range(self.row - i - 1): # Проходим по кол-ву Строк (т.к. см. столбец)
                    if isinstance(self._matrix[j][column_index], int|float) and \
                        isinstance(self._matrix[j+1][column_index], int|float): # Для корректного сравнения чисел
                        if self._matrix[j][column_index] > self._matrix[j+1][column_index]: # Сравниваем если 2 числа
                            self.change_rows(j, j+1) # Меняем данные строки местами
                    else: # Если два соседних элемента не являются числами (и все пр.), то сравниваем их ч-з Тип строки.
                        if str(self._matrix[j][column_index]) > str(self._matrix[j+1][column_index]): # Тут сразу сравниваем значения строк
                            self.change_rows(j, j+1) # а меняем оригинальные элементы (строки)
        else:
            self.sorted_by_column(column_index, True) # Для обратной сортировки, вызовем Прямую
            self.reverse_by_column() # И просто отзеркалим всю Матрицу
        return self # Возвращаем сортированную Матрицу


    # Добавим метод для Транспонирования Матрицы

    def get_transpose_matrix(self):
        '''Возвращает новую транспонированную матрицу
        
        (изначальная не меняется)'''
        _new_matrix = BaseMatrix(self.row, self.column) # Создадим новую Матрицу с поменянными размерами
        # _new_matrix = [[self._matrix[row][col] for row in range(self.row)] for col in range(self.column)]
        for i, row in enumerate(self._matrix): # Получим Строки (и индексы) из изначальной матрицы
            _new_matrix.replace_column(row, i) # Подставим их вместо столбцов для Новой Матрицы
        return _new_matrix # Вернем Новую Транспонированную Матрицу


    # Добавим метод для поворота Матрицы (как для картинки)

    def get_turn_matrix(self, change_direction=False): # ПОка не работает (правильно)
        '''Поворачивает матрицу по часовой стрелке (по умолчанию)
        
        change_direction = True - поворачивает против часовой стрелки
        
        (Возвращает новую матрицу. Изначальная не меняется)'''
        _turn_matrix = BaseMatrix(self.row, self.column) # Создадим новую Матрицу с поменянными размерами
        if change_direction == False: # По часовой стрелке
            for i, row in enumerate(self._matrix): # Получим Строки (и индексы) из изначальной матрицы
                _turn_matrix.replace_column(row, -(i+1)) # Подставим их вместо столбцов для Новой Матрицы
        else: # Против часовой стрелки
            for i, row in enumerate(self._matrix): # Получим Строки (и индексы) из изначальной матрицы
                row.reverse() # Развернем полученную строку
                _turn_matrix.replace_column(row, i) # Подставим ее вместо столбцов для Новой Матрицы
        return _turn_matrix # Вернем новую Повернутую Матрицу




# Создадим Дочерний Класс числовой Матрицы на основе Базового.

class NumMatrix(BaseMatrix):
    '''Числовая Матрица, принимающая в себя только числа (int, float) или None''' 

    def __init__(self, column:int = 1, row: int = 1, filling: int|float|None=None): 
        super().__init__(column, row, filling) # Создаем Инициализатор и таблицу
        if isinstance(filling, int|float|None): # Проверка на число (заполнителя)
            self._filling = filling
        else: raise TypeError('Элементы матрицы могут быть только числами (или None)')
        # ! Не работает проверка на число: если мы вставляем значение уже после задания Матрицы
        # т.е. можно вставить любой элемент. (либо это оставить на "взрослость", либо как-то править.?) 
    

    # Т.к. Матрица подразумевается чисто числовой, можно определить некоторые математические операции с ней. (по своему)

    def __add__(self, other): # Определим способ сложения равных матриц или матрицы с числом 
        '''Складывать можно две равных матрицы или матрицу и число.
        
        Во втором случае число будет прибавлено к каждой ячейке основной матрицы.
        
        Если одна из ячеек = None, ее значение будет заменено на второе слагаемое или на 0'''

        if not isinstance(other, (int, float, NumMatrix)): # Проверка на ТИП
            raise ArithmeticError('Второе слагаемое должно быть числом или матрицей равного размера')

        if isinstance(other, int|float): # Если просто число, создаем из него матрицу
            other = NumMatrix(self.column, self.row, other)
        
        if (self.row == other.row) and (self.column == other.column): # Проверка на совпадение размеров матриц
            for row in range(self.row):
                for col in range(self.column):
                    if self._matrix[row][col] == None: self._matrix[row][col] = 0 # для подстановки вместо None
                    if other._matrix[row][col] == None: other._matrix[row][col] = 0 # для подстановки вместо None

                    _cell_ = self._matrix[row][col] + other._matrix[row][col] # Определяем результат операции
                    self.replace_cell(_cell_, col, row) # Заменяем все ячейки новыми значениями (результатом)
        else: raise IndexError('Не совпадают размеры таблиц')
        return  self # Возвращаем матрицу с обновленными элементами

    def __radd__(self, other): # Определим сложение с перестановкой слагаемых
        return self + other
    
    def __iadd__(self, other): # Определим сложение ч-з инкремент (хотя вроде и так работает)
        return self + other


    def __mul__(self, other): # Определим способ умножения равных матриц или матрицы с числом 
        '''Умножать можно две равных матрицы или матрицу и число.
        
        Во втором случае число будет умножено на каждую ячейку основной матрицы
        
        Если одна из ячеек = None, ее значение будет заменено на второй множитель или на 1'''

        if not isinstance(other, (int, float, NumMatrix)): # Проверка на ТИП
            raise ArithmeticError('Второй множитель должен быть числом или матрицей равного размера')

        if isinstance(other, int|float): # Если просто число, создаем из него матрицу
            other = NumMatrix(self.column, self.row, other)
        
        if (self.row == other.row) and (self.column == other.column): # Проверка на совпадение размеров матриц
            for row in range(self.row):
                for col in range(self.column):
                    if self._matrix[row][col] == None: self._matrix[row][col] = 1 # для подстановки вместо None
                    if other._matrix[row][col] == None: other._matrix[row][col] = 1 # для подстановки вместо None

                    _cell_ = self._matrix[row][col] * other._matrix[row][col] # Определяем результат операции
                    self.replace_cell(_cell_, col, row) # Заменяем все ячейки новыми значениями (результатом)
        else: raise IndexError('Не совпадают размеры таблиц')
        return  self # Возвращаем матрицу с обновленными элементами

    def __rmul__(self, other): # Определим умножение с перестановкой множителей
        return self * other
    
    def __imul__(self, other): # Определим умножение ч-з (*=)
        return self * other


    def __sub__(self, other): # Определим способ вычитания равных матриц или матрицы с числом (не коммутативно) 
        '''Вычитать можно две равных матрицы или матрицу и число. Положение имеет значение!
        
        Во втором случае операция будет выполнена для каждой ячейки основной матрицы с этим числом
        
        Если одна из ячеек = None, ее значение будет заменено на второй элемент или на 0'''
        
        if not isinstance(other, (int, float, NumMatrix)): # Проверка на ТИП
            raise TypeError('Второй элемент должен быть числом или матрицей равного размера')

        if isinstance(other, int|float): # Если просто число, создаем из него матрицу
            other = NumMatrix(self.column, self.row, other)
            
        if (self.row == other.row) and (self.column == other.column): # Проверка на совпадение размеров матриц
            for row in range(self.row):
                for col in range(self.column):
                    if self._matrix[row][col] == None: self._matrix[row][col] = 0 # для подстановки вместо None
                    if other._matrix[row][col] == None: other._matrix[row][col] = 0 # для подстановки вместо None

                    _cell_ = self._matrix[row][col] - other._matrix[row][col] # Определяем результат операции
                    self.replace_cell(_cell_, col, row) # Заменяем все ячейки новыми значениями (результатом)
        else: raise IndexError('Не совпадают размеры таблиц')
        return  self # Возвращаем матрицу с обновленными элементами (результат зависит от положения)

    def __rsub__(self, other): # Определим вычитание ч-з (-=)
        return (-1)*self + other
    
    def __isub__(self, other): # Определим вычитание ч-з (-=)
        return self - other
   

    def __truediv__(self, other): # Определим способ вычитания равных матриц или матрицы с числом (не коммутативно) 
        '''Делить можно две равных матрицы или матрицу и число. Положение имеет значение!
        
        Во втором случае операция будет выполнена для каждой ячейки основной матрицы с этим числом
        
        Если одна из ячеек = None, ее значение будет заменено на второй элемент или на 1'''
        
        if not isinstance(other, (int, float, NumMatrix)): # Проверка на ТИП
            raise TypeError('Второй элемент должен быть числом или матрицей равного размера')

        if isinstance(other, int|float): # Если просто число, создаем из него матрицу
            other = NumMatrix(self.column, self.row, other)
            
        if (self.row == other.row) and (self.column == other.column): # Проверка на совпадение размеров матриц
            for row in range(self.row):
                for col in range(self.column):
                    if self._matrix[row][col] == None: self._matrix[row][col] = 1 # для подстановки вместо None
                    if other._matrix[row][col] == None: other._matrix[row][col] = 1 # для подстановки вместо None

                    _cell_ = self._matrix[row][col] / other._matrix[row][col] # Определяем результат операции
                    self.replace_cell(_cell_, col, row) # Заменяем все ячейки новыми значениями (результатом)
        else: raise IndexError('Не совпадают размеры таблиц')
        return  self # Возвращаем матрицу с обновленными элементами (результат зависит от положения)


    def __rtruediv__(self, other): # Определим вычитание ч-з (-=)
        if not isinstance(other, (int, float, NumMatrix)): # Проверка на ТИП
            raise TypeError('Второй элемент должен быть числом или матрицей равного размера')

        if isinstance(other, int|float): # Если просто число, создаем из него матрицу
            other = NumMatrix(self.column, self.row, other)

        if (self.row == other.row) and (self.column == other.column): # Проверка на совпадение размеров матриц
            for row in range(self.row):
                for col in range(self.column):
                    if self._matrix[row][col] == None: self._matrix[row][col] = 1 # для подстановки вместо None
                    if other._matrix[row][col] == None: other._matrix[row][col] = 1 # для подстановки вместо None

                    _cell_ = other._matrix[row][col] / self._matrix[row][col] # Определяем результат операции
                    self.replace_cell(_cell_, col, row) # Заменяем все ячейки новыми значениями (результатом)
        else: raise IndexError('Не совпадают размеры таблиц')
        return  self # Возвращаем матрицу с обновленными элементами (результат зависит от положения)

    def __itruediv__(self, other): # Определим вычитание ч-з (-=)
        return self / other

    # Схожим образом можно доопределить и прочие математически (базовые) операции с числовыми Матрицами
    # (тут не буду усложнять код,  и так - слишком длинный уже) (мат.методы я свои придумал)


    # Но! Добавим несколько своих методов для сложения строки (столбца или ячейки) с конкретным в Матрице

    def _check_input_type(self, arg: list|tuple): # Добавим метод для проверки входящих значений на число
        '''Проверка на число для входящих значений'''
        if isinstance(arg, int|float): # Для одиночного значения
            return arg
        else:
            _list_ = list(arg)
            for val in _list_: # Проходим по всем входящим элементам 
                if  not isinstance(val, int|float): # Проверяем на НЕ число
                    _res_ = False # Возвращаем ЛОЖЬ (если есть не число)
                    raise ValueError(f'Все входящие элементы должны быть числами') # И - выводим ошибку
            return _list_
        # Тут м.б. сделать проверку на любой нужный тип для входящих элементов  (определить аргумент класса)
        # и вынести этот метод в Базовый Класс с добавлением отдельного аргумента для всех методов ввода (замены)
        # элементов Матрицы. А в дочерних классах менять аргумент класса на нужный тип для подстановки в данный метод.        
    
     
    def sum_rows(self, row: list|tuple, row_index: int = 0):
        '''Складыват указанную строку Матрицы с заданной Строкой'''
        self._check_row_index(row_index) # Проверка на вхождение индексов в размеры Матрицы
        self._check_input_type(row) # Проверка на число для входящих элементов
        _row_M_ = NumMatrix(self.column, self.row, 0) # Создадим новую "пустую" Матрицу
        _row_M_.replace_row(row, row_index) # Применим метод для замены строки для новой Матрицы
        return self + _row_M_ # Получим результат, сложив две матрицы (м.б. не самый эффективный подход...)


    def sum_columns(self, column: list|tuple, column_index: int = 0):
        '''Складыват указаный столбец Матрицы с заданным Столбцом'''
        self._check_column_index(column_index) # Проверка на вхождение индексов в размеры Матрицы  
        self._check_input_type(column) # Проверка на число для входящих элементов
        _column_M_ = NumMatrix(self.column, self.row, 0) # Создадим новую "пустую" Матрицу
        _column_M_.replace_column(column, column_index) # Применим метод для замены столбца для новой Матрицы
        return self + _column_M_ # Получим результат, сложив две матрицы
    

    def sum_number_and_row(self, number: int|float, row_index: int = 0):
        '''Складыват строку Матрицы (поэлементно) с заданным числом'''
        self._check_row_index(row_index)  # Проверка на вхождение индексов в размеры Матрицы
        self._check_input_type(number) # Проверка на число для входящих элементов
        _row_M_ = NumMatrix(self.column, self.row, 0) # Создадим новую "пустую" Матрицу
        _row_ = [number for i in range(self.column)] # Сгенерируем строку из заданого числа
        _row_M_.replace_row(_row_, row_index) # Применим метод для замены строки для новой Матрицы
        return self + _row_M_ # Получим результат, сложив две матрицы
    

    def sum_number_and_col(self, number: int|float, column_index: int = 0):
        '''Складыват столбец Матрицы (поэлементно) с заданным числом'''
        self._check_column_index(column_index)  # Проверка на вхождение индексов в размеры Матрицы
        self._check_input_type(number) # Проверка на число для входящих элементов
        _column_M_ = NumMatrix(self.column, self.row, 0) # Создадим новую "пустую" Матрицу
        _column_ = [number for i in range(self.row)] # Сгенерируем столбец из заданого числа
        _column_M_.replace_column(_column_, column_index) # Применим метод для замены столбца
        return self + _column_M_ # Получим результат, сложив две матрицы
    

    def sum_number_and_cell(self, number: int|float, column_index: int = 0, row_index: int = 0):
        '''Складыват значение указаной ячейки Матрицы с заданным числом'''
        self._check_column_index(column_index) # Проверка на вхождение индексов в размеры Матрицы 
        self._check_row_index(row_index) # Проверка на вхождение индексов в размеры Матрицы
        self._check_input_type(number) # Проверка на число для входящих элементов
        _column_M_ = NumMatrix(self.column, self.row, 0) # Создадим новую "пустую" Матрицу
        _column_M_.replace_cell(number, column_index, row_index) # Применим метод для замены ячейки
        return self + _column_M_ # Получим результат, сложив две матрицы
    

    def sum_row_and_matrix(self, row: list|tuple):
        '''Складыват заданную строку с каждой стройкой Матрицы'''
        if len(row) == self.column: # Проверка на совпадение длины строки
            self._check_input_type(row) # Проверка на число для входящих элементов
            for i in range(self.row): # Проходим по каждой строке 
                self.sum_rows(row, i)
        else: raise ValueError('Не совпадение с количеством столбцов')
        return self # Получим результат
    

    def sum_column_and_matrix(self, column: list|tuple):
        '''Складыват заданный столбец с каждым столбцом Матрицы'''
        if len(column) == self.row: # Проверка на совпадение длины столбца
            self._check_input_type(column) # Проверка на число для входящих элементов
            for i in range(self.column): # Проходим по каждому столбцу
                self.sum_columns(column, i)
        else: raise ValueError('Не совпадение с количеством строк')
        return self # Получим результат


    # Схожим образом можно определить и прочие математические операции для числовой Матрицы,
    # как со списком, так и с числом (для строки, столбца или ячейки Матрицы)
    # Наверняка я использовал не самый рациональный подход (с точки зрения эффективности), 
    # зато быстро и читаемо (вроде) :).

    # Другие методы определены в Базовом Классе (BaseMatrix) 
    # Можно так же добавить прочих методов (по необходимости), но для учебного примера, думаю, достаточно.






# Проверка работы методов Классов (ниже), числовой Матрицы и базовой Матрицы

nm = NumMatrix(5,4, ) # Создадим 1ю числовую матрицу

for row in range(nm.row): # Заполним числовую матрицу упорядоченными значениями
    for col in range(nm.column):
        nm.replace_cell((col+1)*(row+1),  col, row) # Заменив все ячейки в ней.

# for i in range(nm.row): # Заполним Матрицу строками (одинаковыми)
#     nm.replace_row([i for i in range(nm.column)], i)

print('1я Числовая Матрица', '\n')
print(nm) # Вывод полученной Матрицы для проверки (просмотра)
print('Size =', nm.size, '\n') # Вывод текущего размера матрицы 

n1 = NumMatrix(5,4, 20) # Создадим 2ю числовую Матрицу (с одинаковыми значениями)
print('2я Числовая Матрица', '\n') # Вывод полученной Матрицы для наглядности
print(n1, '\n')

nn =  nm + n1  # Зададим мат.операцию с матрицами (и/или числом)
# nm /= 2

print('Матрица после математической операции','\n')
print(nm) # Вывод полученной Матрицы для проверки (просмотра)

row1 = [10, 20, 30, 40, 50] # Для суммирования (Строка)
col1 = [100, 200, 300, 400] # Для суммирования (Столбец)

print('\n', 'Матрица после сложения строк','\n')
nn.sum_rows(row1, 0) # Сложим строки (Матрицы и заданной)
# nn.replace_row(row1, -1) # Проверка на замену строки
print(nn)

print('\n', 'Матрица после сложения столбцов','\n')
nn.sum_columns(col1, 3) # Сложим столбцы (Матрицы и заданного)
# nn.replace_column(col1, 1) # Проверка на замену строки
print(nn)

print('\n', 'Матрица после сложения строки с числом','\n')
nn.sum_number_and_row(50, 1) # Прибавим число к Строке в Матрице
print(nn)

print('\n', 'Матрица после сложения столбца с числом','\n')
nn.sum_number_and_col(100, -1) # Прибавим число к Столбцу в Матрице
print(nn)

print('\n', 'Матрица после сложения ячейки с числом','\n')
nn.sum_number_and_cell(500, -1, -1) # Прибавим число к Ячейке в Матрице
print(nn)

print('\n', 'Матрица после сложения со Строкой','\n')
nn.sum_row_and_matrix(row1)
print(nn)

print('\n', 'Матрица после сложения со Столбцом','\n')
col2 = nn.list_shift(nn.list_shift(col1)) # изменим Столбец (х2 сдвиг) для наглядности и - проверки метода
nn.sum_column_and_matrix(col2)
print(nn)


nn.replace_cell('d') # Если подставить в числовую Матрицу не число - оно подставится (что делать (ли) ?)
print('\n', '!! Матрица с НЕ_Числовой ячейкой !!', '\n')
print(nn)

# Конец проверки методов Числовой Матрицы



# !!! Тестовая проверка работы всех методов для Класса BaseMatrix. (ниже) !!!
print('\n') # Пустая строка для разделения вывода в консоли

m = BaseMatrix(4, 5, 'go') # Создадим экземпляр класса Базовой Матрицы со своим заполнением.
# n = BaseMatrix(8, 10, 1)

print('Новая Матрица с базовыми значениями', '\n') # Подпись + Пустая строка 
print(m) # Вывод только что созданной "пустой" Матрицы

a = m.column # Получаем кол-во строк (базовых)
b = m.row   # Получаем кол-во столбцов (базовых)
s = m.size  # Получаем кортеж размера матрицы (базовой)

new_row = (1,2,3,4) # Создаем "строку" для Переопределения
new_col = ('a','b','c','d','e') # Создаем "столбец" для Переопределения

new_r2 = ('q','w','e','r') # Создаем "Строку" для ВСТАВКИ
new_c2 = (6,5,4,3,2,1) # Создаем "Столбец" для ВСТАВКИ (уже увеличенной длины, т.к. была +стр)

print('\n') # Пустая строка для разделения вывода в консоли
print(f"строк = {b}, столбцов = {a}") # Печать размеров по-элементно
print('Size =',m.size) # Печать размеров отдельным методом
print('\n') # Пустая строка для разделения вывода в консоли

m.replace_row(new_row,) # Меняем строку в Матрице (базовой)
m.replace_column(new_col, ) # Меняем Столбец в Матрице (после строки)
m.replace_cell('Hi!',1, -3) # Меняем Ячейку в Матрице ()

print('Матрица после трех замен','\n', m) # Выводим Матрицу (базового размера) с изменениями

m.insert_row(new_r2, 1) # ! Добавляем новую Строку (расширяем Матрицу)
print('\n', "Матрица с добавленной строкой", '\n', m)
print('\n', 'Новый размер Матрицы =', m.size) # Выводим новый размер Матрицы

m.insert_column(new_c2, 2) # ! Добавляем новый Столбец (расширяем Матрицу)
print('\n', "Матрица с добавленным столбцом", '\n', m)
print('\n', 'Новый размер Матрицы =', m.size) # Выводим новый размер Матрицы

m.del_row(2) # Удаляем строку из матрицы
print('\n', "Матрица с Удаленной строкой", '\n', m)
print('\n', 'Новый размер Матрицы =', m.size) # Выводим новый размер Матрицы

m.del_column(3) # Удаляем столбец из матрицы
print('\n', "Матрица с Удаленным столбцом", '\n', m)
print('\n', 'Новый размер Матрицы =', m.size ) # Выводим новый размер Матрицы

m.del_cell(3, 3) # Удаляем строку и столбец из матрицы, по индексу ячейки
print('\n', "Матрица с Удаленной ячейкой", '\n', m)
print('\n', 'Новый размер Матрицы =', m.size, '\n') # Выводим новый размер Матрицы

m.insert_column([0,0,0,0], 3) # Добавим доп.столбец (последним) для наглядности
m.insert_row([2,2,2,2], 3) # Добавим доп.строку (последней) для наглядности
print('\n', 'Расширим Матрицу', '\n', m)
print('\n', 'Новый размер Матрицы =', m.size, '\n') # Выводим новый размер Матрицы

m.reverse_by_row() # Отзеркалим по Х
print('Зеркально по Х', '\n', m)
print() # Разделитель (пустая строка)
m.reverse_by_column() # Отзеркалим по Y
print('Зеркально по Y', '\n',m)

m.shift_rows() # Сдвинем по вертикали 
print('\n', 'Сдвинуто по Y +', '\n', m)
m.shift_rows(0) # Сдвинем по вертикали обратно
print('\n', 'Сдвинуто по Y -', '\n', m)

m.shift_columns() # Сдвинем по горизонтали
print('\n', 'Сдвинуто по Х +', '\n', m)
m.shift_columns(0) # Сдвинем по горизонтали обратно
print('\n', 'Сдвинуто по Х -', '\n', m)

m.change_rows(2, 3) # Поменяем две строки местами
print('\n', 'Строки поменяны местами', '\n', m)
m.change_columns(0, 1) # Поменяем два столбца местами
print('\n', 'Столбцы поменяны местами', '\n', m)
m.change_cells(0, -1, -1, 0) # Поменяем две ячейки местами
print('\n', 'Ячейки поменяны местами', '\n', m)

m.sorted_by_row(-1, ) # Сортируем всю Матрицу по 1 из ее Строк
print('\n', 'Сортированная по Строке Матрица', '\n')
print(m) # Выводим сортированную Матрицу

m.sorted_by_column(-1, 0) # Сортируем всю Матрицу по 1 из ее Столбцов
print('\n', 'Сортированная по Столбцу Матрица', '\n')
print(m) # Выводим сортированную Матрицу


print('\n', 'Новая Транспонированая Матрица')
print('Размер предыдущий Матрицы =', m.size , '\n') # Выводим новый размер Матрицы
t = m.get_transpose_matrix() # Получаем новую Транспонируем Матрицу
print(t)
print('Размер новый Матрицы =', t.size) # Выводим новый размер Матрицы !!!! (Не меняется)

print('\n', 'Новая Повернутая Матрица')
print('Размер предыдущий Матрицы =', m.size , '\n') # Выводим новый размер Матрицы
r = m.get_turn_matrix(1) # Повернем транспонированную Матрицу по часовой стрелке 
print(r)
print('Размер новый Матрицы =', r.size) # Выводим размер новый Матрицы

print('\n', 'Проверим, что "Старая" Матрица не изменилась')
print(m) # Выведем "старую" матрицу для проверки
print('Размер "старой" Матрицы =', r.size)


print('\n') # Пустая строка для разделения вывода в консоли
r = m.get_row(3) # Получаем Строку из Матрицы (измененной)
c = m.get_column() # Получаем Столбец из Матрицы (измененной)
cell = m.get_cell(1,2) # Получаем Ячейку (по индекскам) из Матрицы (измененной)
print('Ячейка = ', cell)
print('Строка = ', r, )
print('Столбец =', c)


m1 = m.get_matrix_part_by_indexes(1,1,2,3) # Получим Новую Матрицу из части Основной (не меняет основную)
print('\n', 'Возвращенная матрица (по индексам):', '\n')
print(m1) # Выводим Возвращеную матрицу (как Матрицу)
print('\n', 'type (Возвращенной матрицы) =', type(m1)) # Проверка Типа возвращенной матрицы

m2 = m.get_matrix_part_by_size(0,2,3,2) # Получим Новую Матрицу из части Основной (не меняет основную)
print('\n', 'Возвращенная матрица (по размерам):', '\n')
print(m2) # Выводим Возвращеную матрицу (как Матрицу)
print('\n', 'type (Возвращенной матрицы) =', type(m2)) # Проверка Типа возвращенной матрицы


print('\n', 'Проверка работы СтатикМетода для сдвига строки', '\n') # Пустая
bu = (1,2,3,4,5,6,7)
print(bu)
b1 = BaseMatrix.list_shift(bu)
print(b1)
b2 = BaseMatrix.list_shift(bu, 0) 
print(b2)


# Конец проверок работы методов Матриц. Конец Решения задачи 3.1
print('\n') # Пустая строка для разделения вывода в консоли
