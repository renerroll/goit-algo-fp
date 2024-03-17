"""
Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.
"""


# Helpers for greedy algorithm method
def calculate_ratio(item):
    return item[1]["calories"] / item[1]["cost"]


def greedy_algorithm(items, maxbudget):
    sorted_items = sorted(items.items(), key=calculate_ratio, reverse=True)
    selected_items = {}
    survive_budget = maxbudget

    for item_name, item_data in sorted_items:
        if item_data["cost"] <= survive_budget:
            selected_items[item_name] = 1
            survive_budget -= item_data["cost"]
    return selected_items, survive_budget


# Helpers for dynamic programmnig method
def get_ccal(items, cost):
    for key in items:
        if items[key]["cost"] == cost:
            return items[key]["calories"]


def dynamic_programming(items, maxbudget):
    cost = [int(items[key]["cost"]) for key in items]
    sorted_items = sorted(cost)
    n = len(sorted_items)

    K = [[0 for w in range(maxbudget + 1)] for i in range(n + 1)]
    K_res = {}

    for i in range(n + 1):
        for w in range(maxbudget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                K_res[(i, w)] = {}
            elif cost[i - 1] <= w:
                if (
                    get_ccal(items, cost[i - 1]) + K[i - 1][w - cost[i - 1]]
                    < K[i - 1][w]
                ):
                    K[i][w] = K[i - 1][w]
                    K_res[(i, w)] = K_res[(i - 1, w)]
                else:
                    K[i][w] = get_ccal(items, cost[i - 1]) + K[i - 1][w - cost[i - 1]]
                    K_res[(i, w)] = K_res[(i - 1, w - cost[i - 1])] | {
                        cost[i - 1]: True
                    }

            else:
                K[i][w] = K[i - 1][w]
                K_res[(i, w)] = K_res[(i - 1, w)]

    survive_budget = maxbudget
    selected_items = {}
    for cost in K_res[(n, maxbudget)]:
        item_name = next(key for key in items if items[key]["cost"] == cost)
        selected_items[item_name] = 1
        survive_budget -= cost

    return selected_items, survive_budget


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    maxbudget = 112  

    greedy_res, survive_budget = greedy_algorithm(items, maxbudget)
    print(f"Greedy algorithm set: {greedy_res}")
    print(f"Remaining maxbudget: {survive_budget}")

    dp_res, survive_budget = dynamic_programming(items, maxbudget)
    print(f"Dynamic programming set: {dp_res}")
    print(f"Remaining maxbudget: {survive_budget}")