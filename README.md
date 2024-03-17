| Sum |    Monte-Carlo def   |   Chances % | Combinations |
|-----|----------------------|-------------|--------------|
| 2   | 2.78%                | 2.78%       | (1/36)       |
| 3   | 5.55%                | 5.56%       | (2/36)       |
| 4   | 8.31%                | 8.33%       | (3/36)       |
| 5   | 11.08%               | 11.11%      | (4/36)       |
| 6   | 13.90%               | 13.89%      | (5/36)       |
| 7   | 16.64%               | 16.67%      | (6/36)       |
| 8   | 13.90%               | 13.89%      | (5/36)       |
| 9   | 11.13%               | 11.11%      | (4/36)       |
| 10  | 8.33%                | 8.33%       | (3/36)       |
| 11  | 5.56%                | 5.56%       | (2/36)       |
| 12  | 2.80%                | 2.78%       | (1/36)       |

З отриманих результатів можна зробити висновок, що метод Монте-Карло є досить ефективним і точним засобом для апроксимації ймовірностей у складних системах, таких як експеримент із кидком кубиків. Порівняння отриманих значень ймовірностей з теоретичними результатами показує, що вони майже ідентичні, що свідчить про високу достовірність методу Монте-Карло.

Ця висока точність дозволяє використовувати метод Монте-Карло в ситуаціях, де прямі аналітичні розрахунки можуть бути надто складними або обчислювально витратними. Враховуючи відмінність методу Монте-Карло від традиційних аналітичних методів, його застосування може бути особливо вигідним у випадках, коли немає можливості отримати аналітичні розв'язки або коли вимагається велика кількість обчислювальних ресурсів.

Отже, метод Монте-Карло може бути потужним інструментом для моделювання складних систем і вирішення різноманітних завдань, де точність та надійність дуже важливі.

| Sum | Analytical chances     | Monte Carlo chances     | Difference |
|-----|------------------------|-------------------------|------------|
| 2   | 2.78%                  | 2.78%                   | 0%         |
| 3   | 5.56%                  | 5.55%                   | 0.01%      |
| 4   | 8.33%                  | 8.31%                   | 0.02%      |
| 5   | 11.11%                 | 11.08%                  | 0.03%      |
| 6   | 13.89%                 | 13.90%                  | 0.01%      |
| 7   | 16.67%                 | 16.64%                  | 0.03%      |
| 8   | 13.89%                 | 13.90%                  | 0.01%      |
| 9   | 11.11%                 | 11.13%                  | 0.02%      |
| 10  | 8.33%                  | 8.33%                   | 0%         |
| 11  | 5.56%                  | 5.56%                   | 0%         |
| 12  | 2.78%                  | 2.80%                   | 0.02%      |

У цьому вигляді кожен рядок таблиці містить суму (Sum), аналітичну ймовірність (Analytical chances), ймовірність, отриману за допомогою методу Монте-Карло (Monte Carlo chances) та різницю між аналітичною та Монте-Карло ймовірностями (Difference). Таке порівняння дозволить нам зрозуміти, наскільки точно наш метод Монте-Карло апроксимує аналітичні результати.
