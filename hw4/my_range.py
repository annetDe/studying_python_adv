sentinel = object()


class MyRange:
    """аналог функции range"""
    def __init__(self, start: int,  stop: int = sentinel, step: int = 1) -> None:
        if stop is sentinel:  # если задан только один аргумент
            self.__start = 0  # значение для __start по умолчанию == 0
            self.__stop = start - 1  # __stop исключить из диапазона
        else:  # задано два или три аргумента
            self.__start = start
            self.__stop = stop - step
        self.__step = step
        self.__iter = self.__start - step
        if not (isinstance(self.__start, int) and isinstance(self.__stop, int)
                and isinstance(self.__step, int) and step != 0):  # проверка соответствия аргументов
            raise ValueError

    def __next__(self):
        # проверка выхода за границу (__stop) учитывая знак шага (__step)
        if (self.__step > 0 and self.__iter >= self.__stop) or (self.__step < 0 and self.__iter <= self.__stop):
            raise StopIteration
        else:
            self.__iter += self.__step
            return self.__iter

    def __iter__(self):
        return self

    def __str__(self):
        return f'{__class__.__name__}{(self.__start, self.__stop, self.__step)}'


print('MyRange(5):')
for i in MyRange(5):
    print(i, end=' ')

print('\nMyRange(1, 4):')
for i in MyRange(1, 4):
    print(i, end=' ')

print('\nMyRange(-3, 7, 3):')
for i in MyRange(-3, 7, 3):
    print(i, end=' ')

print('\nMyRange(10, -1, -2):')
for i in MyRange(10, -1, -2):
    print(i, end=' ')

print('\nMyRange(0, -10, -1):')
for i in MyRange(0, -10, -1):
    print(i, end=' ')

print('\nMyRange(0):')
for i in MyRange(0):
    print(i, end=' ')

print('\nMyRange(1, 0):')
for i in MyRange(1, 0):
    print(i, end=' ')

# print('\nMyRange(10, -1.5, 1):')
# for i in MyRange(10, -1, 0):
#     print(i, end=' ')
