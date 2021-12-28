from decimal import Decimal
from utils import *
from typing import List


class WeightedMath:

    @staticmethod
    def calculate_invariant(weight_1: Decimal, balance_1: Decimal, weight_2: Decimal, balance_2: Decimal):

        invariant = mul_down(pow_down(balance_1, weight_1), pow_down(balance_2, weight_2))
        return invariant

    @staticmethod
    def calc_out_given_in(
            balance_in: Decimal,
            weight_in: Decimal,
            balance_out: Decimal,
            weight_out: Decimal,
            amount_in: Decimal
    ) -> Decimal:

        denominator = balance_in + amount_in
        base = div_up(balance_in, denominator)
        exponent = div_down(weight_in, weight_out)
        power = pow_up(base, exponent)
        right_term = Decimal(1) - power

        return mul_down(balance_out, right_term)

