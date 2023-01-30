def outer_function():
    message = 'hi'

    def inner_function():
        print(message)

    return inner_function()


outer_function()


# closures
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_fun = outer_function('hi')
bye_fun = outer_function('Bye')
hi_fun()
bye_fun()


# decorator
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper function executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print(f'display info ran with argument {name} {age}')


display()
display_info('mikhail', 34)


# classes as decorators
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method  executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('display function ran')


@decorator_class
def display_info(name, age):
    print(f'display info ran with argument {name} {age}')


display()
display_info('mike', 24)


