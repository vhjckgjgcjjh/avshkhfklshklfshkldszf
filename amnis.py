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

def stake_APT_via_amnis(account, address):
    logger = setup_gay_logger('stake_APT_via_amnis')

    payload = {
  "function": "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a::router::deposit_entry",
  "type_arguments": [],
  "arguments": [
    str(random.randint(20000000, 21000000)),
    str(address)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_APT_via_liquidswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_via_liquidswap')

    payload = {
      "function": "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::scripts::swap",
      "type_arguments": [
        "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a::amapt_token::AmnisApt",
        "0x1::aptos_coin::AptosCoin",
        "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::curves::Stable"
      ],
      "arguments": [
        str(APT_amount),
        str(random.randint(19322223, 19522223)),
      ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def stake2_APT_via_amnis(account, address):
    logger = setup_gay_logger('stake2_APT_via_amnis')

    payload = {
  "function": "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a::router::deposit_and_stake_entry",
  "type_arguments": [],
  "arguments": [
    str(random.randint(20000000, 21000000)),
    str(address)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap2_APT_via_liquidswap(account, APT_amount: int):
    logger = setup_gay_logger('swap2_APT_via_liquidswap')

    payload = {
  "function": "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::scripts::swap",
  "type_arguments": [
    "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a::stapt_token::StakedApt",
    "0x1::aptos_coin::AptosCoin",
    "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::curves::Stable"
  ],
  "arguments": [
    str(APT_amount),
    str(random.randint(19322223, 19522223)),
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)