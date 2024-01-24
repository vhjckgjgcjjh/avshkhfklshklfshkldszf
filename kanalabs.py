from aptos_sdk.client import RestClient
from constant import MAX_SLIPPAGE_PERCENT
from logger import setup_gay_logger
from utils import get_apt_price, append_digit_to_integer
import random

sum_swap = str(random.randint(500, 530))

SLIPPAGE = (100 - MAX_SLIPPAGE_PERCENT) / 100
Z8 = 10 ** 8
Z6 = 10 ** 6
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



def deposit_APT_to_kanalabs(account, APT_amount: int):
    logger = setup_gay_logger('deposit_APT_to_kanalabs')

    payload = {
  "function": "0x9538c839fe490ccfaf32ad9f7491b5e84e610ff6edc110ff883f06ebde82463d::wrapper::deposit_and_register_base",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC"
  ],
  "arguments": [
    str(APT_amount),
    "7"
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_APT_to_USDC_via_kanalabs(account):
    logger = setup_gay_logger('swap_APT_to_USDC_via_kanalabs')

    payload = {
  "function": "0x9538c839fe490ccfaf32ad9f7491b5e84e610ff6edc110ff883f06ebde82463d::wrapper::place_market_order_user_entry_without_deposit",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC"
  ],
  "arguments": [
    sum_swap,
    "7",
    "0xd718181a753f5b759518d9b896018dd7eb3d77d80bf90ba77fffaf678f781929",
    True,
    3
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)


def swap_USDC_to_APT_via_kanalabs(account):
    logger = setup_gay_logger('swap_USDC_to_APT_via_kanalabs')


    payload = {
  "function": "0x9538c839fe490ccfaf32ad9f7491b5e84e610ff6edc110ff883f06ebde82463d::wrapper::place_market_order_user_entry_without_deposit",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC"
  ],
  "arguments": [
    sum_swap,
    "7",
    "0xd718181a753f5b759518d9b896018dd7eb3d77d80bf90ba77fffaf678f781929",
    False,
    3
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def withdraw_APT_to_kanalabs(account, APT_amount: int):
    logger = setup_gay_logger('withdraw_APT_to_kanalabs')


    payload = {
  "function": "0xc0deb00c405f84c85dc13442e305df75d1288100cdd82675695f6148c7ece51c::user::withdraw_to_coinstore",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin"
  ],
  "arguments": [
    "7",
     str(APT_amount),
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

