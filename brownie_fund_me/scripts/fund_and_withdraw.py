from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fundme = FundMe[-1]
    account = get_account()
    entranceFee = fundme.getEntranceFee()
    print(entranceFee)
    print(f"The current entry fee is {entranceFee}")
    print(f"Funding {account} with {entranceFee}")
    fundme.fund({"from": account, "value": entranceFee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
