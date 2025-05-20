# function 4
# map
from typing import List

wage: List[float] = [1000, 2000, 3000, 4000, 8000]

print(wage)


def salary_increase(wage: float) -> float:
    match wage:
        case w if w <= 1000:
            return w * 2.8
        case w if w <= 2000:
            return w * 2.5
        case w if w <= 3000:
            return w * 1.8
        case w if w <= 4000:
            return w * 1.5
        case w if w >= 4000:
            return w * 1.2
        case _:
            return w


new_wage = list(map(salary_increase, wage))

print(new_wage)
