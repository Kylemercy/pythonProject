# practical use of decorator
def my_timer(org_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = org_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{org_func.__name__} ran in {t2} seconds')
        return result

    return wrapper

import time


@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display info ran with argument {name} {age}')


display_info('nank',34)