from abc import ABC, abstractmethod

class Figures(ABC):
    def vibor(self):
        print(f'Вы выбрали фигуру {self.__class__.__name__}')

    @abstractmethod
    def P(self):
        raise Exception


class Triangle(Figures):
    def __init__(self, storony):
        self.storony = storony
    def P(self):
        print(int(st1) + int(st2) + int(st3))

class Cycle(Figures):
    def __init__(self, radius):
        self.radius = radius
    def P(self):
        print(int(r) * 2 * 3.14)

class Square(Figures):
    def __init__(self, storony):
        self.storony = storony
    def P(self):
        print((int(st1) * 4))

class Rectangle(Figures):
    def __init__(self, storony):
        self.storony = storony

    def P(self):
        print((int(st1) + int(st2)) * 2)

print('Какая ваша фигура?\n1.Треугольник\n2.Круг\n3.Квадрат\n4.Прямоугольник')
choice = int(input())

if choice == 1:
    t = Triangle(choice)
    st1 = input(f'Введите 1 сторону треугольника.\n')
    st2 = input(f'Введите 2 сторону треугольника.\n')
    st3 = input(f'Введите 3 сторону треугольника.\n')
    vopr = input((f'Хотите узнать периметр вашей фигуры?\ny/n?\n'))
    if vopr == 'y':
        t.P()

elif choice == 2:
    c = Cycle(choice)
    r = input(f'Введите радиус круга.\n')
    vopr = input((f'Хотите узнать периметр вашей фигуры?\ny/n?\n'))
    if vopr == 'y':
        c.P()

elif choice == 3:
    s = Square(choice)
    st1 = input(f'Введите сторону квадрата.\n')
    vopr = input((f'Хотите узнать периметр вашей фигуры?\ny/n?\n'))
    if vopr == 'y':
        s.P()

elif choice == 4:
    r = Rectangle(choice)
    st1 = input(f'Введите 1 сторону прямоугольника.\n')
    st2 = input(f'Введите 2 сторону прямоугольника.\n')
    vopr = input((f'Хотите узнать периметр вашей фигуры?\ny/n?\n'))
    if vopr == 'y':
        r.P()

