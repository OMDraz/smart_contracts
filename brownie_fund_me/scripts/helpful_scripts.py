from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3


LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-locale"]
DECIMALS = 8
STARTING_PRICE = 20000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The development network is {network.show_active()}")
    print("Deploying to mock...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print(f"Deployed to address {MockV3Aggregator[-1].address}")
