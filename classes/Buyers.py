from classes.LBP import LBP


class Buyers:
    pass


class LimitOrders(Buyers):

    def __init__(self, target: float, budget: float):
        """Trader that buy an amount of token when its price is lower thank or equal to to target.

        Args:
            target: maximum price allowed to buy.
            budget: budget for the buy.
        """
        self.target = target
        self.budget = budget
        self.bought = False

    def buy(self, lbp: LBP):
        """Buy token with amount if price is less than target price and if not a previous buy exists."""
        if not self.bought and self.target >= lbp.spot_price():
            lbp.buy_tokens(usd=self.budget)
            self.bought = True


class FrontRunners(Buyers):

    def __init__(self, budget: float):
        self.budget = budget
        self.bought = False

    def buy(self, lbp):
        if not self.bought:
            lbp.buy_tokens(usd=self.budget)
            self.bought = True


class BuyersFactory:

    @staticmethod
    def build_buyers(buyers_config_list: list) -> list:
        """

        Args:
            buyers_config_list: a list of child of the parent class Buyers

        Returns:

        """
        buyers = []  # this is a queue of buyers' orders
        # If config is an empty list, buyers will be an empty list. In this case the price will be driven by te weights.
        for buyer in buyers_config_list:
            buyer_type = buyer["type"]
            if not buyer_type:
                RuntimeError("No buyer type specified in config")
            elif buyer_type == "FrontRunners":
                buyers.append(FrontRunners(buyer["budget"] * buyer["count"]))
            elif buyer_type == "LimitOrders":
                for _ in range(buyer["count"]):
                    buyers.append(LimitOrders(buyer["target"], buyer["budget"]))

        return buyers
