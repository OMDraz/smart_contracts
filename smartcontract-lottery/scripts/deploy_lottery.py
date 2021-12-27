from scripts.helpful_scripts import get_account, get_contract
from brownie import Lottery, network, config


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(
        get_contract("eth_usd_price_feed").address,
        get_contract("vrf_coordinator").address,
        get_contract("link_token").address,
        config["networks"][network.show_active()]["fee"],
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed Lottery!")


def start_lottery():
    # Step 1: Get the account
    account = get_account()
    # Step 2: Get the contract
    lottery = Lottery[-1]
    # Step 3: Call the function in the contract you want
    starting_tx = lottery.startLottery({"from": account})
    starting_tx.wait(1)
    # Step 4: Print that it's  starting
    print("The lottery has begun!")

def enter_lottery():
    # Step 1: Get the account
    account = get_account()
    
    # Step 2: Get the lottery
    lottery = Lottery[-1]
    
    # Step 3: Get the value for entering
    value = lottery.getEntranceFee + 100000000
    
    # Step 4: Deploy the function
    enter_tx = lottery.enter({'from': account}, value: value))
    
    # Step 5: Wait a second 
    enter_tx(1)
    
    # Step 6: Print for completion
    print('You have entered the lottery!')

def main():
    deploy_lottery()
    start_lottery()
    enter_lottery() 