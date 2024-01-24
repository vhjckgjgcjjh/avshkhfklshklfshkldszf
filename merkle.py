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

def open_merkle_order(account, amount_zUSDC: int):
    # Fake tx, no actual position will be open

    logger = setup_gay_logger('open_merkle_order')

    leverage = 130
    position_size = leverage * amount_zUSDC
    if position_size <= 300000000:
        return None

    apt = int(get_apt_price() * Z8)
    margin_requirement = 1 / leverage
    liquidation_price = int(apt * (1 - margin_requirement))
    stop_loss_price = int(apt * (1 - 0.10 / leverage))
    take_profit_price = int(apt * (1 + 0.20 / leverage))

    payload = {
        "function": "0x5ae6789dd2fec1a9ec9cccfb3acaf12e93d432f0a3a42c92fe1a9d490b7bbc06::managed_trading::place_order_with_referrer",
        "type_arguments": [
            "0x5ae6789dd2fec1a9ec9cccfb3acaf12e93d432f0a3a42c92fe1a9d490b7bbc06::pair_types::APT_USD",
            "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC"
        ],
        "arguments": [
            str(position_size),
            str(amount_zUSDC),
            str(append_digit_to_integer(liquidation_price, 10)),
            True,
            True,
            True,
            str(append_digit_to_integer(stop_loss_price, 59)),
            str(append_digit_to_integer(take_profit_price, 60)),
            False,
            "0x0"
        ],
        "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)