# References: https://github.com/donallmc/lbp_sim

import json

from classes.Buyers import BuyersFactory
from classes.LBP import LBP
from classes.Simulator import Simulator

lbp_config_file: str = 'configs/lbp.json'
lbp_type = 'weights_5_95'
buyer_config_file: str = 'configs/mix.json'

lbp_config: json = json.load(open(lbp_config_file,))
buyer_config: json = json.load(open(buyer_config_file,))

factory: BuyersFactory = BuyersFactory()
buyers: list = factory.build_buyers(buyer_config)

lbp: LBP = LBP(**lbp_config[lbp_type])

lbp.plot_weights()
simulator: Simulator = Simulator()
simulator.run(lbp, buyers)
