"""Пример простых функций."""


def example_function():
    """Выводит пример сообщения."""
    print('Это пример функции')


def greet(name):
    """Выводит приветствие для переданного имени."""
    message = 'Привет, ' + name + '!'
    print(message)


if __name__ == '__main__':
    example_function()
    greet('Мир')
