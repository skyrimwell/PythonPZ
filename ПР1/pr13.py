# from decimal import Decimal
import math


def f11(x, y):
    return(y-math.exp(y) + 43 + (x**4 - math.log(y)) / (abs(y) - x**3 + 64) + math.sqrt(
        ((y**6 - 22 * y**4) / (29 * x**3 + math.tan(y)))))


def f12(x):
    if x < -27:
        return x - math.exp(x) + 43
    elif (x < -1) and (x >= -27):
        return x**5 - x**2
    elif (x >= -1) and (x < 9):
        return x**8 - 51 * x**3
    elif (x >= 9):
        return 51 * x**5 + math.fabs(x)


def f13(n,m):
    cyc1 = cyc2  = 0
    for i in range(1,n+1):
        cyc1 += i-math.exp(i)+43
    for i in range(1,n+1):
        for j in range(1,m+1):
            cyc2 += abs(j) - j**4
    return 18 * cyc1 - cyc2

def f14(n):
    if n == 0:
        return 9
    else:
        return abs(f14(n-1))+math.tan(f14(n-1))


# print(f"f11(54,63)={Decimal(f11(54,63)):.2E}")
# print(f"f11(-51,3)={Decimal(f11(-51,3)):.2E}")
# print("\n")
# print(f"f12(-35)={Decimal(f12(-35)):.2E}")
# print(f"f12(-20)={Decimal(f12(-20)):.2E}")
# print("\n")
# print(f"f13(47,44)={Decimal(f13(47,44)):.2E}")
# print(f"f13(61,27)={Decimal(f13(61,27)):.2E}")
# print("\n")
# print(f"f14(3)={Decimal(f14(3)):.2E}")
# print(f"f14(16)={Decimal(f14(16)):.2E}")