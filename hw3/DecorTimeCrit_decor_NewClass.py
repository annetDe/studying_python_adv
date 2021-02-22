from time import time, sleep


def DecorTimeCrit(critical_time):
    '''функция  принимает аргумент и возвращает декоратор'''

    def check_time(func, crit_time):
        '''функция для декорирования методов декорируемого класса'''

        def helper(*args, **kwargs):
            start = time()
            res = func(*args, **kwargs)
            runtime = time() - start
            if runtime > crit_time:
                print(f'WARNING! {func.__name__} slow. Time = {runtime} sec.')
            return res

        return helper

    def decorator(cls):
        class NewTest:
            '''новый класс, которым заменим декорируемый класс'''
            def __init__(self, *args, **kwargs):
                self.__obj = cls(*args, **kwargs)  # создали экземпляр декорируемого класса

            def __getattribute__(self, item):
                try:
                    is_my_attr = super().__getattribute__(item)  # папа, у меня есть атрибут s?
                except AttributeError:
                    pass  # нет сынок, это не твой атрибут -> надо задекорировать
                else:
                    return is_my_attr  # да сынок, это твое -> декорировать не надо

                attr = self.__obj.__getattribute__(item)  # получить атрибут у декорируемого класса

                if callable(attr):  # если это метод, а не поле
                    return check_time(attr, critical_time)  # вернуть задекорированный метод
                else:
                    return attr  # вернуть неизменным
        return NewTest
    return decorator


@DecorTimeCrit(critical_time=0.45)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


t = Test()

t.method_1()
t.method_2()


# slow method start
# slow method finish
# WARNING! method_1 slow. Time = ??? sec.
# fast method start
# fast method finish
