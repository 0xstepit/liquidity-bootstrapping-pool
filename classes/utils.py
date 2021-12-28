from decimal import *


def mul_up(a: Decimal, b: Decimal) -> Decimal:
    getcontext().prec = 28
    getcontext().rounding = ROUND_UP
    return a * b


def mul_down(a: Decimal, b: Decimal) -> Decimal:
    getcontext().prec = 28
    getcontext().rounding = ROUND_DOWN
    return a * b


def pow_up(a: Decimal, b: Decimal) -> Decimal:
    getcontext().prec = 28
    getcontext().rounding = ROUND_UP
    return a ** b


def pow_down(a: Decimal, b: Decimal) -> Decimal:
    getcontext().prec = 28
    getcontext().rounding = ROUND_DOWN
    return a ** b


def div_up(a: Decimal, b: Decimal) -> Decimal:
    if a * b == 0:

        return Decimal(0)
    else:
        getcontext().prec = 28
        getcontext().rounding = ROUND_UP
        return a / b


def div_down(a: Decimal, b: Decimal) -> Decimal:
    getcontext().prec = 28
    getcontext().rounding = ROUND_DOWN
    result = a / b
    return result
