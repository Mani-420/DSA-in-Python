# Get all factors of n
import math
n = 12
factors = set()
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        factors.add(i)
        factors.add(n // i)


# O(n!) Factorial Time ----------------------------------------
# Traveling Salesman Problem
# Extremly Slow. Even with less data takes extremly large time.

# Permutations
# Travelling Salesman Problem