"""
Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином (для перегляду перейди за цим шляхом assets/task_7_probability_table.jpg)

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці.
"""
import random


def cube_dice():
    return random.randint(1, 6)


def checking_rand(cube_numbers):
    calculate = {}
    for _ in range(cube_numbers):
        cube1 = cube_dice()
        cube2 = cube_dice()
        total = cube1 + cube2
        if total in calculate:
            calculate[total] += 1
        else:
            calculate[total] = 1
    return calculate


def calculate_cases(calculate, cube_numbers):
    cases = {}
    for key, value in calculate.items():
        cases[key] = value / cube_numbers
    return cases


def summing_chances(cases):
    print("|  Sum  || Chances ||")
    print("-" * 25)
    for i in range(2, 13):
        print(f"|{i:^7}|| {cases.get(i, 0):.2%}   ||")


def main():
    cube_numbers = 333000
    calculate = checking_rand(cube_numbers)
    cases = calculate_cases(calculate, cube_numbers)
    summing_chances(cases)


if __name__ == "__main__":
    main()