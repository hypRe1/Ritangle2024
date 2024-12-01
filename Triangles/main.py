import itertools

from helpers import display_crossword, valid_triangle, is_triangular, crossword_str, validate_crossword
from constants import pythagtrips
from math import gcd, isqrt

crosswords: list[tuple[list[int],set[int]]] = []

print("WINTEGERS: THE REVENGE ARC 😈\nTriangles Solution\n\n")

# 1ac,2ac,4ac
newcs = crosswords.copy()
odd_composites = [n for n in range(11, 100, 2) if any(n % d == 0 for d in range(3, isqrt(n) + 1))]
for i in range(len(odd_composites)):
    for j in range(i + 1, len(odd_composites)):
        for k in range(j + 1, len(odd_composites)):
            a, b, c = odd_composites[i], odd_composites[j], odd_composites[k]
            
            # Check pairwise co-primality
            if gcd(a, b) != 1 or gcd(a, c) != 1 or gcd(b, c) != 1:
                continue

            # Check triangle inequality
            if not valid_triangle(a,b,c):
                continue

            # Check if the perimeter is triangular
            P = a + b + c
            if not is_triangular(P):
                continue
            
            for _1ac, _2ac, _4ac in itertools.permutations((a,b,c)):
                newc = [-1] * 24
                newu = set()
                newc[0] = int(str(_1ac)[0])
                newc[1] = int(str(_1ac)[1])
                newu.add(_1ac)

                newc[2] = int(str(_2ac)[0])
                newc[3] = int(str(_2ac)[1])
                newu.add(_2ac)

                newc[4] = int(str(_4ac)[0])
                newc[5] = int(str(_4ac)[1])
                newu.add(_4ac)

                if validate_crossword(newc):
                    newcs.append((newc.copy(), newu.copy()))
crosswords = newcs.copy()


# 11ac,10dn,12dn
newcs = []
for a,b,c in pythagtrips:
    if not (10<=a<100 and 10<=b<100 and 10<=c<100):
        continue

    for newc, newu in crosswords:
        if (a in newu) or (b in newu) or (c in newu):
            continue

        for _11ac, _10dn, _12dn in itertools.permutations((a,b,c)):
            newc[14] = int(str(_11ac)[0])
            newc[15] = int(str(_11ac)[1])
            newu.add(_11ac)

            newc[12] = int(str(_10dn)[0])
            newc[18] = int(str(_10dn)[1])
            newu.add(_10dn)

            newc[17] = int(str(_12dn)[0])
            newc[23] = int(str(_12dn)[1])
            newu.add(_12dn)

            if validate_crossword(newc):
                newcs.append((newc.copy(), newu.copy()))
crosswords = newcs.copy()

# 13ac,7dn,1dn
newcs = []
for a,b,c in pythagtrips:
    if not (10<=a<100 and 100<=b<1000 and 100<=c<1000):
        continue

    for newc, newu in crosswords:
        if (a in newu) or (b in newu) or (c in newu):
            continue

        for _13ac, _7dn, _1dn in itertools.permutations((a,b,c)):
            if (len(str(_13ac)) != 3) or (len(str(_7dn)) != 3) or (len(str(_1dn)) != 2):
                continue

            # we already have 0 and 18
            if (int(str(_13ac)[0]) != newc[18]) or (int(str(_1dn)[0]) != newc[0]):
                continue

            # we have overlap at 19
            if str(_13ac)[1] != str(_7dn)[2]:
                continue

            newc[19] = int(str(_13ac)[1])
            newc[20] = int(str(_13ac)[2])
            newu.add(_13ac)

            newc[7] = int(str(_7dn)[0])
            newc[13] = int(str(_7dn)[1])
            newu.add(_7dn)

            newc[6] = int(str(_1dn)[1])
            newu.add(_1dn)

            if validate_crossword(newc):
                newcs.append((newc.copy(), newu.copy()))
crosswords = newcs.copy()

# 14ac,9dn,5dn
newcs = []
for a,b,c in pythagtrips:
    if not (10<=a<100 and 100<=b<1000 and 100<=c<1000):
        continue

    for newc, newu in crosswords:
        if (a in newu) or (b in newu) or (c in newu):
            continue

        for _14ac, _9dn, _5dn in itertools.permutations((a,b,c)):
            if (len(str(_14ac)) != 3) or (len(str(_9dn)) != 3) or (len(str(_5dn)) != 2):
                continue

            # we already have 5 and 23
            if (int(str(_14ac)[2]) != newc[23]) or (int(str(_5dn)[0]) != newc[5]):
                continue

            # we have overlap at 22
            if str(_14ac)[1] != str(_9dn)[2]:
                continue

            newc[21] = int(str(_14ac)[0])
            newc[22] = int(str(_14ac)[1])
            newu.add(_14ac)

            newc[10] = int(str(_9dn)[0])
            newc[16] = int(str(_9dn)[1])
            newu.add(_9dn)

            newc[11] = int(str(_5dn)[1])
            newu.add(_5dn)

            if validate_crossword(newc):
                newcs.append((newc.copy(), newu.copy()))
crosswords = newcs.copy()

# 6ac,8ac
newcs = []
for n in range(0, 100):
    a = n//10
    b = n-a*10
    if b==0:
        continue

    for newc, newu in crosswords:
        _2dn = newc[2]*100 + a*10 + newc[14]
        _3dn = newc[3]*100 + b*10 + newc[15]

        _sum =_2dn + _3dn
        if _sum == isqrt(_sum)**2:
            newc[8] = a
            newc[9] = b
            if validate_crossword(newc):
                newcs.append((newc.copy(), newu.copy()))
crosswords = newcs.copy()

newcs = []
for c, u in crosswords:
    valid = True
    answers = set()
    answer_sqs = [[0,1],[2,3],[4,5],[6,7,8],[9,10,11],[14,15],[18,19,20],[21,22,23],[0,6],[2,8,14],[3,9,15],[5,11],[7,13,19],[10,16,22],[12,18],[17,23]]
    for sqs in answer_sqs:
        answer = ""
        for sq in sqs:
            answer += str(c[sq])
        answer = int(answer)
        if answer in answers:
            valid = False
            break
        answers.add(answer)
    if not valid:
        continue


    P = (c[0]+c[2]+c[4])*10 + c[1]+c[3]+c[5]
    found = False
    for x in answers:
        if found:
            break
        for y in answers:
            if x-y == P:
                newcs.append((c.copy(), u.copy()))
                found = True
                break
crosswords = newcs.copy()

# Save crosswords to file
with open("crosswords.txt", "w", encoding="ascii") as f:
    f.write("Wintegers: The Revenge Arc\nTriangles solution\n\n\n")
    for i, c in enumerate(crosswords, start=1):
        f.write(f"Crossword {i}\n" + crossword_str(c[0]) + "\n\n")
print(f"Saved {len(crosswords)} crossword(s) to crosswords.txt\n\n")

# Compute D

C = crosswords[0][0]
across_sqs = [[0,1],[2,3],[4,5],[6,7,8],[9,10,11],[14,15],[18,19,20],[21,22,23]]
down_sqs = [[0,6],[2,8,14],[3,9,15],[5,11],[7,13,19],[10,16,22],[12,18],[17,23]]

across = []
for sqs in across_sqs:
    answer = ""
    for sq in sqs:
        answer += str(C[sq])
    answer = int(answer)
    across.append(answer)

down = []
for sqs in down_sqs:
    answer = ""
    for sq in sqs:
        answer += str(C[sq])
    answer = int(answer)
    down.append(answer)

D = abs(sum(across)-sum(down))
print(f"D = {D}")

display_crossword(C)
