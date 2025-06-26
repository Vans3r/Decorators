import os
from functools import wraps
from datetime import datetime

def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        name = old_function.__name__
        with open('main.log', 'a', encoding='utf-8') as m:
            m.write(f'Название: {name}\nАргументы: {args,kwargs}\nДата: {datetime.now()}\nРезультат: {result}')
        return result
    return new_function

def flat_generator(lists):
    outer_index = 0
    inner_index = 0
    while outer_index < len(lists):
        current_list = lists[outer_index]
        if inner_index < len(current_list):
            item = current_list[inner_index]
            inner_index += 1
            yield item
        else:
            outer_index += 1
            inner_index = 0

list_of_lists = ['помидор, яблоко, банан',['капуста']]
logger(flat_generator(list_of_lists))