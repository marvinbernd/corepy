sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]

for item in zip(sunday, monday):
    print(item)

for sun, mon in zip(sunday, monday):
    print("average =", (sun + mon) / 2)

tuesday = [14, 16, 17, 14, 12, 12, 15, 16, 20, 22, 24, 23]

for temps in zip(sunday, monday, tuesday):
    print(f"min={min(temps):4.1f}, max={max(temps):4.1f}, average={sum(temps) / len(temps):4.1f}")

from itertools import chain
temperatures = chain(sunday, monday, tuesday)
print(all(t > 0 for t in temperatures))

from lucas import lucas
from filtering_comprehensions import is_prime

for x in (p for p in lucas() if is_prime()):
    print(x)