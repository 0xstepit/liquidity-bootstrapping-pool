from matplotlib import pyplot as plt

from classes.LBP import LBP


class Simulator:

    @staticmethod
    def run(lbp: LBP, buyers):
        lbp.print_token_balance()
        for i in range(lbp.weights_update_steps):
            for buyer in buyers:
                buyer.buy(lbp)
            lbp.step()

        lbp.print_price_history()
        lbp.print_token_balance()
        lbp.plot_chart()
        plt.show()
