from time import time, sleep


def DecorTimeCrit(critical_time):
    '''функция  принимает аргумент и возвращает декоратор'''

    def check_time(func, critical_time):
        '''функция для декорирования методов декорируемого класса'''

        def helper(*args, **kwargs):
            start = time()
            res = func(*args, **kwargs)  # выполнить декорируемый метод
            runtime = time() - start
            if runtime > critical_time:
                print(f'WARNING! {func.__name__} slow. Time = {runtime} sec.')
            return res

        return helper

    def decorator(cls):
        def helper(*args, **kwargs):
            for attr_str in dir(cls):  # для всех атрибутов декорируемого класса
                if attr_str.startswith('__'):  # если это магический метод
                    continue  # пропустить

                attr = getattr(cls, attr_str)  # получить атрибут
                if callable(attr):  # если это метод, а не поле
                    decor_attr = check_time(attr, critical_time)  # задекорировать метод
                    setattr(cls, attr_str, decor_attr)  # заменить старый метод на декорированный
            return cls(*args, **kwargs)  # вернуть экземпляр класса
        return helper
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
