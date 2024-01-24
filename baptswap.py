from aptos_sdk.client import RestClient
from constant import MAX_SLIPPAGE_PERCENT
from logger import setup_gay_logger
from utils import get_apt_price, append_digit_to_integer

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

def swap_APT_to_zUSDC_via_baptswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDC_via_baptswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDC_ideal = apt_price * normalization
    zUSDC_slip = zUSDC_ideal * SLIPPAGE
    zUSDC_slip_int = int(zUSDC_slip * Z6)

    payload = {
  "function": "0x6ee5ff12d9af89de4cb9f127bc4c484d26acda56c03536b5e3792eac94da0a36::router_v2::swap_exact_input",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC"
  ],
  "arguments": [
    str(APT_amount),
    str(zUSDC_slip_int)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_zUSDC_to_APT_via_baptswap(account, zUSDC_amount: int):
    logger = setup_gay_logger('swap_zUSDC_to_APT_via_baptswap')

    apt_price = get_apt_price()
    normalization = zUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_ideal * Z8)
    rounded_number = (APT_slip_int // 1000000) * 1000000
    print(rounded_number, "rounded_number")

    payload = {
  "function": "0x6ee5ff12d9af89de4cb9f127bc4c484d26acda56c03536b5e3792eac94da0a36::router_v2::swap_exact_input",
  "type_arguments": [
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0x1::aptos_coin::AptosCoin"
  ],
  "arguments": [
    str(zUSDC_amount),
    str(rounded_number)
  ],
  "type": "entry_function_payload"
}


    submit_and_log_transaction(account, payload, logger)



