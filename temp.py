from math import sqrt


def CalculateSquareRoot(number: float) -> float:
    """Вычисляет квадратный корень"""
    return sqrt(number)


def calc(your_number: float) -> str:
    if your_number <= 0:
        return 'Отрицательное число'
    root = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа. Это будет: '
          f'{root}')


message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)
calc(25.5)
