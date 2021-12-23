# https://www.youtube.com/watch?v=M576WGiDBdQ @ 4:53:54


from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    upgraded_value = simple_storage.retrieve()
    print(upgraded_value)


def main():
    deploy_simple_storage()


# Notes
# print(account)
# account = accounts.add(config["wallets"]["from_key"])
# print(account)
