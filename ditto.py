from aptos_sdk.client import RestClient
from constant import MAX_SLIPPAGE_PERCENT
from logger import setup_gay_logger
from utils import get_apt_price, append_digit_to_integer
import random

SLIPPAGE = (100 - MAX_SLIPPAGE_PERCENT) / 100
Z8 = 10 ** 8
Z6 = 10 ** 6
Z4 = 10 ** 4
Rest_Client = RestClient("https://fullnode.mainnet.aptoslabs.com/v1")

def submit_and_log_transaction(account, payload, logger):
    try:
        txn = Rest_Client.submit_transaction(account, payload)
        Rest_Client.wait_for_transaction(txn)
        logger.info(f'Success: https://explorer.aptoslabs.com/txn/{txn}?network=mainnet')
    except AssertionError as e:
        logger.error(f"AssertionError caught: {e}")
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {e}")

def stake_apt_via_ditto(account):
    logger = setup_gay_logger('stake_apt')

    payload = {
  "function": "0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5::ditto_staking::stake_aptos",
  "type_arguments": [],
  "arguments": [
    str(random.randint(1100000, 1600000))
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def unstake_apt_via_ditto(account, APT_amount: int):
    logger = setup_gay_logger('unstake_apt')

    payload = {
  "function": "0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5::ditto_staking::instant_unstake",
  "type_arguments": [],
  "arguments": [
    str(APT_amount)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)
