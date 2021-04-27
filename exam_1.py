# On the first day, the athlete ran X kilometers, and then every day he increased the mileage by 10% from the
# previous one values (to solve the problem, it is allowed to use numbers with a comma, which in Python are written
# with a dot).For this number X, determine the number of the day for which the athlete's mileage will be at least Y
# kilometers.
import random


def runing(run, road):
    day = 1
    while road > run * day:
        day += 1
        run += run / 10
    return day


print(runing(10, 60))


# Given three sides of a triangle a, b, c. Determine the type of triangle with given sides. Print one of four words:
# simple for a simple triangle, isosceles for an isosceles triangle, 2 side equal for 2 side equal triangle,
# or impossible if a triangle with such sides does not exist (we assume that a degenerate triangle is also impossible).

def type_of_tringle(a, b, c):
    if a != b and a != c and b != c:
        print("Triangle is simple")
    elif a == b == c:
        print("Triangle is isoscele")
    elif (a == b and a == c and b != c) or (a == b and b == c and a != c) or (a == c and b == c and a != b):
        print("Two side equal triangle")
    else:
        print("impossible triangle")


type_of_tringle(3, 4, 5)


# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является
# високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем,
# год являетсявисокосным, если его номер кратен 4, но не кратен 100, или же если он кратен 400

def is_leap_year(year):
    is_leap = False
    if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0):
        is_leap = True
    if is_leap:
        return 'YES'
    else:
        return 'NO'


print(is_leap_year(1600))


# chingachung

def pleyer():
    str = ('paper', 'stone', 'scissors')
    hand = random.choice(str)
    return hand


def chingachung():
    i = input('Input paper, stone or scissors ')
    you = pleyer()
    if i == you:
        print('I', i, 'You', you, 'No one won')
    elif i == 'paper' and you == 'stone' \
            or i == 'stone' and you == 'scissors' \
            or i == 'scissors' and you == 'paper':
        print('I', i, 'won You', you)
    elif i == 'paper' and you == 'scissors'\
            or i == 'stone' and you == 'paper'\
            or i == 'scissors' and you == 'stone':
        print('You', you, 'won me', i)
    else:
        print("Mistake word. Please input paper, stone or scissors")


chingachung()
