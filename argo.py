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

def stake_apt_via_argo(account, APT_amount: int):
    logger = setup_gay_logger('stake_apt')

    payload = {
      "function": "0x98298d34bcf896c663e069c464754e0cfd36b50e21eedd8db0e4189168057cb7::console_v1::deposit_with_price",
      "type_arguments": [
        "0xa0a017f8d8a695731dcdb8bf27e2da141da68785b347aaa5b87c5e0fa4332222::namespace::Namespace0",
        "0x1::aptos_coin::AptosCoin"
      ],
      "arguments": [
        str(APT_amount),
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)

def unstake_apt_via_argo(account, APT_amount: int):
    logger = setup_gay_logger('unstake_apt')

    payload = {
      "function": "0x98298d34bcf896c663e069c464754e0cfd36b50e21eedd8db0e4189168057cb7::console_v1::withdraw_with_price",
      "type_arguments": [
        "0xa0a017f8d8a695731dcdb8bf27e2da141da68785b347aaa5b87c5e0fa4332222::namespace::Namespace0",
        "0x1::aptos_coin::AptosCoin"
      ],
      "arguments": [
        str(APT_amount),
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)
