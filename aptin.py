from aptos_sdk.client import RestClient
from constant import MAX_SLIPPAGE_PERCENT
from logger import setup_gay_logger
from utils import get_apt_price, append_digit_to_integer

import random

SLIPPAGE = (100 - MAX_SLIPPAGE_PERCENT) / 100
Z8 = 10 ** 8
Z6 = 10 ** 6
Rest_Client = RestClient("https://fullnode.mainnet.aptoslabs.com/v1")

function = random.randint(210000, 310000)

function_stay = function


def submit_and_log_transaction(account, payload, logger):
    try:
        txn = Rest_Client.submit_transaction(account, payload)
        Rest_Client.wait_for_transaction(txn)
        logger.info(f'Success: https://explorer.aptoslabs.com/txn/{txn}?network=mainnet')
    except AssertionError as e:
        logger.error(f"AssertionError caught: {e}")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}")


def stake_apt_via_aptin(account):
    logger = setup_gay_logger('stake_apt_via_aptin')

    payload = {
      "function": "0x3c1d4a86594d681ff7e5d5a233965daeabdc6a15fe5672ceeda5260038857183::lend::supply",
      "type_arguments": [
        "0x1::aptos_coin::AptosCoin"
      ],
      "arguments": [
        str(random.randint(11000000, 16000000)),
        True
      ],
      "type": "entry_function_payload"
    }


    submit_and_log_transaction(account, payload, logger)

def borrow_apt_via_aptin(account):
    logger = setup_gay_logger('borrow_apt_via_aptin')

    payload = {
  "function": "0x3c1d4a86594d681ff7e5d5a233965daeabdc6a15fe5672ceeda5260038857183::lend::borrow",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin"
  ],
  "arguments": [
    str(function)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def repay_apt_via_aptin(account):
    logger = setup_gay_logger('repay_apt_via_aptin')

    payload = {
  "function": "0x3c1d4a86594d681ff7e5d5a233965daeabdc6a15fe5672ceeda5260038857183::lend::repay",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin"
  ],
  "arguments": [
    str(function_stay)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def withdraw_apt_via_aptin(account, vAPT_amount: int, address):
    logger = setup_gay_logger('withdraw_apt_via_aptin')

    payload = {
  "function": "0x3c1d4a86594d681ff7e5d5a233965daeabdc6a15fe5672ceeda5260038857183::lend::withdraw",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin"
  ],
  "arguments": [
    str(vAPT_amount),
    str(address)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)