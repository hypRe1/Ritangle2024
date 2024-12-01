"""
Ritangle Final Number Soup
"""

import itertools
import math
import time

from alive_progress import alive_it

from constants import *
from helpers import *

# all crossword combos found so far
# list of tuples of list and set
# set is already used numbers to help with unique constraint
# list of crossword squares (-1 means empty square)
crosswords: list[tuple[list[int], set[int]]] = []

print("WINTEGERS: THE REVENGE ARC 😈\nNumber Soup Solution\n\n")
start_time = time.perf_counter()


# 12 across and 15 across
# modifies 14,15,16,19,20,21
print("1. Computing 12ac and 15ac")

newcs = []
for _12ac, _15ac in alive_it(
    itertools.product({123, 199, 322, 521, 843}, {161, 385, 897}), 15
):
    newc = [-1] * 36
    newu = set()
    newc[14], newc[15], newc[16] = [int(x) for x in str(_12ac)]
    newu.add(_12ac)
    newc[19], newc[20], newc[21] = [int(x) for x in str(_15ac)]
    newu.add(_15ac)
    if validate(newc):
        newcs.append((newc, newu))

crosswords = newcs
print(f"Done 1 - {len(crosswords)} crosswords\n")

# modifies 11,12,13,22,23,24
newcs = []
print("2. Computing 10ac and 16ac")
for _10ac, _16ac in alive_it(
    itertools.combinations(goofyns, 2), math.comb(len(goofyns), 2)
):
    for c, u in crosswords:
        if _10ac in u or _16ac in u:
            continue
        newc = c.copy()
        newu = u.copy()
        newc[11], newc[12], newc[13] = [int(x) for x in str(_10ac)]
        newu.add(_10ac)
        newc[22], newc[23], newc[24] = [int(x) for x in str(_16ac)]
        newu.add(_16ac)
        if validate(newc):
            newcs.append((newc, newu))
crosswords = newcs.copy()

print(f"Done 2 - {len(crosswords)} crosswords\n")

# currently all possible 0..8 and 11..24 square combos have been found
# so we do the prime downs modifying 2,11,20,29 and 6,15,24,33
newcs = []
print("3. Computing 2dn and 6dn")
for _2dn in alive_it(primens):
    for c, u in crosswords:
        if _2dn in u:
            continue
        _2DNS = str(_2dn)

        if c[11] != int(_2DNS[1]) or c[20] != int(_2DNS[2]):
            continue

        for _6dn in primens:
            if _2dn == _6dn or _6dn in u:
                continue
            _6DNS = str(_6dn)
            if _2DNS[0] == _6DNS[0] or _2DNS[3] == _6DNS[3]:
                continue

            if c[15] != int(_6DNS[1]) or c[24] != int(_6DNS[2]):
                continue

            newc = c.copy()
            newu = u.copy()
            newc[2], newc[29] = int(_2DNS[0]), int(_2DNS[3])
            newu.add(_2dn)
            newc[6], newc[33] = int(_6DNS[0]), int(_6DNS[3])
            newu.add(_6dn)
            if validate(newc):
                newcs.append((newc, newu))
crosswords = newcs.copy()

print(f"Done 3 - {len(crosswords)} crosswords\n")


# modifies 27..35
print("4. Computing 19ac, 20ac, and 21ac")
newcs = []
for s, t, f in alive_it(
    itertools.product(squarens, triangns, fibns),
    total=len(squarens) * len(triangns) * len(fibns),
):
    if s == t or s == f or t == f:
        continue

    digits = set(list(str(s)) + list(str(t)) + list(str(f)))
    if len(digits) != 9:
        continue

    for _19ac, _20ac, _21ac in itertools.permutations((s, t, f)):
        for c, u in crosswords:
            if _19ac in u or _20ac in u or _21ac in u:
                continue

            # we already have 29 and 33
            if int(str(_19ac)[2]) != c[29] or int(str(_21ac)[0]) != c[33]:
                continue

            newc = c.copy()
            newu = u.copy()
            newc[27], newc[28], newc[29] = [int(x) for x in str(_19ac)]
            newu.add(_19ac)
            newc[30], newc[31], newc[32] = [int(x) for x in str(_20ac)]
            newu.add(_20ac)
            newc[33], newc[34], newc[35] = [int(x) for x in str(_21ac)]
            newu.add(_21ac)
            if validate(newc):
                newcs.append((newc, newu))
crosswords = newcs.copy()

print(f"Done 4 - {len(crosswords)} crosswords\n")

# Priority 3
# modifies 0,1,2,3,4,5,6,7,8
print("5. Computing 1ac, 3ac, and 6ac")
newcs = []
for h, l, c in alive_it(
    itertools.product(happyns, luckyns, cubens),
    total=len(happyns) * len(luckyns) * len(cubens),
):
    if h == l or h == c or l == c:
        continue

    digits = set(list(str(h)) + list(str(l)) + list(str(c)))
    if len(digits) != 9:
        continue

    for _1ac, _3ac, _6ac in itertools.permutations((h, l, c)):
        for c, u in crosswords:
            if _1ac in u or _3ac in u or _6ac in u:
                continue

            # we already have 2 and 6
            if int(str(_1ac)[2]) != c[2] or int(str(_6ac)[0]) != c[6]:
                continue

            newc = c.copy()
            newu = u.copy()
            newc[0], newc[1], newc[2] = [int(x) for x in str(_1ac)]
            newu.add(_1ac)
            newc[3], newc[4], newc[5] = [int(x) for x in str(_3ac)]
            newu.add(_3ac)
            newc[6], newc[7], newc[8] = [int(x) for x in str(_6ac)]
            newu.add(_6ac)
            if validate(newc):
                newcs.append((newc, newu))
crosswords = newcs.copy()

print(f"Done 5 - {len(crosswords)} crosswords\n")

# we now have all combos for 0,..,8,11,..,16,19,..,24,27,..35
# now we can start purging cos we need sum of cubes of digits of 4 down to be square
print("6. Computing 4dn and 5dn")
newcs = []
# 4, 13, 22, 31
for c, u in alive_it(crosswords):

    # 4 down requirement
    s = c[4] ** 3 + c[13] ** 3 + c[22] ** 3 + c[31] ** 3
    if s != math.isqrt(s) ** 2:
        continue

    # 5 down requirement
    # 11 down - harshad number = 5down
    # 11 down - 5 down = harshad number
    def check_harshad(a):
        """
        Check if number is a harshad number from geeksforgeeks
        """
        _sum = 0
        temp = a
        while temp > 0:
            _sum = _sum + temp % 10
            temp = temp // 10
        return a % _sum == 0

    _11dn = c[12] * 100 + c[21] * 10 + c[30]
    _5dn = c[5] * 100 + c[14] * 10 + c[23]
    h = _11dn - _5dn
    if h <= 0 or not check_harshad(h):
        continue
    newcs.append((c, u))
crosswords = newcs.copy()

print(f"Done 6 - {len(crosswords)} crosswords\n")

# 14 down - factor of 45 (sum of bottom row always 1+..+9 = 45)
# we can purge some more cases
print("7. Computing 14dn")
# must be 15 cos non-trivial function
newcs = []
for c, u in alive_it(crosswords):
    if c[27] != 5:
        continue

    if 15 not in u:
        newc = c.copy()
        newu = u.copy()
        newc[18] = 1
        if validate(newc):
            newu.add(18)
            newcs.append((newc, newu))
crosswords = newcs.copy()
print(f"Done 7 - {len(crosswords)} crosswords\n")


# 1 down - factor of 20 across
print("8. Computing 1dn")
newcs = []
for c, u in alive_it(crosswords):
    _20ac = c[30] * 100 + c[31] * 10 + c[32]
    for n in range(10, 100):
        if ("0" in str(n)) or (n in u) or (n == _20ac):
            continue

        if (_20ac % n == 0) and (n // 10 == c[0]):
            newc = c.copy()
            newu = u.copy()
            newc[9] = n - ((n // 10) * 10)
            if validate(newc):
                newu.add(n)
                newcs.append((newc, newu))

crosswords = newcs.copy()
print(f"Done 8 - {len(crosswords)} crosswords\n")

# 7 down - prime factor of 3 across
print("9. Computing 7dn")
newcs = []
for c, u in alive_it(crosswords):
    _3ac = c[3] * 100 + c[4] * 10 + c[5]
    for n in primens2:
        if (_3ac % n == 0) and (n not in u) and (n // 10 == c[8]) and (n != _3ac):
            newc = c.copy()
            newu = u.copy()
            newc[17] = n - ((n // 10) * 10)
            if validate(newc):
                newu.add(n)
                newcs.append((newc, newu))
crosswords = newcs.copy()
print(f"Done 9 - {len(crosswords)} crosswords\n")

# 17ac = 18dn - 13dn
print("10. Computing 8ac")
newcs = []
for c, u in alive_it(crosswords):
    for n in range(1, 10):
        _8ac = c[9] * 10 + n
        if _8ac in u:
            continue
        _1dn = c[0] * 10 + c[9]
        _9dn = n * 10 + c[19]

        if _8ac == _1dn - _9dn:
            newc = c.copy()
            newu = u.copy()
            newc[10] = n
            if validate(newc):
                newu.add(_8ac)
                newcs.append((newc, newu))
crosswords = newcs.copy()
print(f"Done 10 - {len(crosswords)} crosswords\n")

# 17ac = 18dn - 13dn
print("10. Computing 17ac")
newcs = []
for c, u in alive_it(crosswords):
    for n in range(10, 100):
        if ("0" in str(n)) or (n in u):
            continue

        _13dn = c[16] * 10 + n // 10
        _18dn = (n - ((n // 10) * 10)) * 10 + c[35]
        _17ac = n

        if _17ac == _18dn - _13dn:
            newc = c.copy()
            newu = u.copy()

            newc[25] = int(str(n)[0])
            newc[26] = int(str(n)[1])
            if validate(newc):
                newu.add(_17ac)
                newcs.append((newc, newu))
crosswords = newcs.copy()
print(f"Done 10 - {len(crosswords)} crosswords\n")

if len(crosswords) == 1:
    end_time = time.perf_counter()
    duration = end_time - start_time
    print(f"Successfully found solution in {round(duration, 3)} seconds ✅\n")
    c = crosswords[0][0]
    print(crossword_str(c))

    across_entries = []
    for a in across:
        entry = ""
        for sq in a:
            entry += str(c[sq])
        across_entries.append(int(entry))

    down_entries = []
    for d in down:
        entry = ""
        for sq in d:
            entry += str(c[sq])
        down_entries.append(int(entry))

    D = abs(sum(across_entries) - sum(down_entries))
    print(f"D = {D}")
    display_crossword(c)

# Save crosswords to file
with open("crosswords.txt", "w", encoding="ascii") as f:
    f.write("Wintegers: The Revenge Arc\nNumber Soup solution\n\n\n")
    for i, c in enumerate(crosswords, start=1):
        f.write(f"Crossword {i}\n" + crossword_str(c[0]) + "\n\n")
