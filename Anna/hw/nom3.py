from math import *


def okrug(x):
    if x * 100 - int(x * 100) == 0.5:
        x += 0.01
    return round(x * 100) / 100


A1 = [int(input("A1.X\n")), int(input("A1.Y\n"))]
A2 = [int(input("A2.X\n")), int(input("A2.Y\n"))]
A3 = [int(input("A3.X\n")), int(input("A3.Y\n"))]
A4 = [int(input("A4.X\n")), int(input("A4.Y\n"))]
A1A2 = sqrt((A2[1] - A1[1]) ** 2 + (A2[0] - A1[0]) ** 2)
A2A4 = sqrt((A4[1] - A2[1]) ** 2 + (A4[0] - A2[0]) ** 2)
A1A4 = sqrt((A4[1] - A1[1]) ** 2 + (A4[0] - A1[0]) ** 2)
A3A4 = sqrt((A4[1] - A3[1]) ** 2 + (A4[0] - A3[0]) ** 2)
A3A2 = sqrt((A2[1] - A3[1]) ** 2 + (A2[0] - A3[0]) ** 2)
A1A2 = abs(A1A2)
A2A4 = abs(A2A4)
A1A4 = abs(A1A4)
A3A4 = abs(A3A4)
A3A2 = abs(A3A2)
angleA2 = acos((A1A4 ** 2 - A1A2 ** 2 - A2A4 ** 2) / (-2 * A1A2 * A2A4))
angleA4 = acos((A3A2 ** 2 - A3A4 ** 2 - A2A4 ** 2) / (-2 * A3A4 * A2A4))
angleA2 = okrug(angleA2)
angleA4 = okrug(angleA4)
if angleA2 + angleA4 == 3.14:
    print('YES')
else:
    print('NO')
