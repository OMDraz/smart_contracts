from brownie import Lottery, accounts, config, network
from web3 import Web3


def test_get_entrance_fee():
    # Get the account
    account = accounts[0]
    # create the contract
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_usd_price_feed"],
        {"from": account},
    )
    # deploy the function and check if it is within bounds
    # assert lottery.getEntranceFee() > Web3.toWei(0.01, "ether")
    # assert lottery.getEntranceFee() < Web3.toWei(0.015, "ether")
