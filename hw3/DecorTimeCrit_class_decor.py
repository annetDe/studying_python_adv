from time import time, sleep


class DecorTimeCrit:
    def __init__(self, critical_time):
        self.crit_time = critical_time

    def check_time(self, func):
        '''функция для декорирования методов декорируемого класса'''
        def helper(*args, **kwargs):
            start = time()
            func(*args, ** kwargs)
            runtime = time() - start
            if runtime > self.crit_time:
                print(f'WARNING! {func.__name__} slow. Time = {runtime} sec.')
        return helper

    def __call__(self, cls):
        def helper(*args, **kwargs):
            for attr_str in dir(cls):  # для всех атрибутов декорируемого класса
                if attr_str.startswith('__'):  # если это магический метод
                    continue  # пропустить

                attr = getattr(cls, attr_str)  # получить атрибут
                if callable(attr):  # если это метод, а не поле
                    decor_attr = self.check_time(attr)  # задекорировать метод
                    setattr(cls, attr_str, decor_attr)  # заменить старый метод на декорированный
            return cls(*args, **kwargs)  # вернуть экземпляр класса
        return helper


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
