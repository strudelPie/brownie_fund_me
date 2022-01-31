from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    # entrance_fee = 25000000000000000
    print(f"The entrance_fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    # fund_me.withdraw({"from": account})
    fund_me.withdraw({"from": account, "gas_limit": 6721975, "allow_revert": True})


def main():
    fund()
    withdraw()
