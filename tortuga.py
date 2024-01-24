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

def stake_apt_via_tortuga(account, APT_amount: int):
    logger = setup_gay_logger('stake_apt')

    payload = {
  "function": "0x8f396e4246b2ba87b51c0739ef5ea4f26515a98375308c31ac2ec1e42142a57f::stake_router::stake",
  "type_arguments": [],
  "arguments": [
    str(random.randint(1100000, 1600000))

  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def unstake_apt_via_tortuga(account, APT_amount: int):
    logger = setup_gay_logger('unstake_apt')

    payload = {
      "function": "0xbd35135844473187163ca197ca93b2ab014370587bb0ed3befff9e902d6bb541::amm::swap_exact_coin_for_coin_with_signer",
      "type_arguments": [
        "0x84d7aeef42d38a5ffc3ccef853e1b82e4958659d16a7de736a29c55fbbeb0114::staked_aptos_coin::StakedAptosCoin",
        "0x1::aptos_coin::AptosCoin"
      ],
      "arguments": [
        str(APT_amount),
        "0"
      ],
      "type": "entry_function_payload"
    }
    submit_and_log_transaction(account, payload, logger)
