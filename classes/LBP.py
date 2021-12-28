import logging
import sys
import json
import matplotlib.pyplot as plt

black = '#202122'
lightblue = '#00E7B9'
purple = '#881AF5'


class LBP:
    def __init__(
            self,
            init_balance_token: float,
            init_balance_usd: float,
            init_weight_token: float,
            final_weight_token: float,
            weights_update_steps: int,
    ):
        self.balance_usd = init_balance_usd
        self.balance_token = init_balance_token
        self.weight_token = init_weight_token
        self.weight_usd = 1 - init_weight_token
        self.weights_update_steps = weights_update_steps
        self.delta_weight = (init_weight_token - final_weight_token) / self.weights_update_steps
        self.iteration = 0
        self.price_history = [self.spot_price()]

    def step(self):
        """Update weights of the tokens and compute + append the new token price."""
        self.iteration += 1
        self.update_weights()
        self.price_history.append(self.spot_price())

    def update_weights(self):
        """Update weights associated to usd and the token. The assumption here is that the token will always start
        with an higher weight. This is the situation of an initial bootstrapping."""
        self.weight_usd += self.delta_weight
        self.weight_token -= self.delta_weight

    def spot_price(self):
        """Compute token price based on weights and pool balances"""
        return round((self.balance_usd / self.weight_usd) / (self.balance_token / self.weight_token), 4)

    def buy_tokens(self, usd: float):
        """Buy an amount of token with a certain amount of usd."""
        if self.balance_token > 0:
            price = self.spot_price()
            tokens = usd / price
            if tokens >= self.balance_token:
                tokens = self.balance_token
                usd = tokens * price
            self.balance_usd += usd
            self.balance_token -= tokens

    def print_price_history(self):
        print("\n\n--- PRICE HISTORY ---")
        for i in range(len(self.price_history)):
            print("Iteration #" + str(i) + ":\t$" + str(self.price_history[i]))

    def print_token_balance(self):
        """Print the number of token available in the pool."""
        print("Remaining available tokens: " + '{:,}'.format(round(self.balance_token, 2)))

    def plot_chart(self):
        """Print the price history of the bootstrapped token"""
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(range(0, len(self.price_history)), self.price_history, linewidth=2, c=purple)
        ax.set_title("LBP TOKEN PRICE", fontweight="bold")
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Price")
        ax.set_xlim([0, self.weights_update_steps])

    def plot_weights(self):
        weights_token = [self.weight_token - self.delta_weight * i for i in range(self.weights_update_steps)]
        weights_usd = [self.weight_usd + self.delta_weight * i for i in range(self.weights_update_steps)]
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(range(0, self.weights_update_steps), weights_token, linewidth=2, c=lightblue, label="Token")
        ax.plot(range(0, self.weights_update_steps), weights_usd, linewidth=2, c=purple, label="USD")
        ax.set_title("LBP WEIGHTS", fontweight="bold")
        ax.set_xlabel("Iterations")
        ax.set_ylabel("Weights")
        ax.legend()
        ax.set_xlim([0, self.weights_update_steps])
        ax.set_ylim([0, 1])
        ax.margins(x=0, y=0)

