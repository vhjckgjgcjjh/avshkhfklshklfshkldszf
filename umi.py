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

def swap_APT_to_zUSDC_via_umi(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDC_via_umi')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDC_ideal = apt_price * normalization
    zUSDC_slip = zUSDC_ideal * SLIPPAGE
    zUSDC_slip_int = int(zUSDC_slip * Z6)

    payload = {
  "function": "0xbeaa9e5ef5bee0781476a4adf293aae7dc3a28e9bd79fda89fca7211fb94c80::aggregator::three_step_route",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::WETH",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12::curves::Uncorrelated",
    "u8",
    "u8"
  ],
  "arguments": [
    3,
    "0",
    False,
    10,
    "0",
    False,
    11,
    "0",
    False,
    str(APT_amount),
    str(zUSDC_slip_int)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_zUSDC_to_APT_via_umi(account, zUSDC_amount: int):
    logger = setup_gay_logger('swap_zUSDC_to_APT_via_umi')

    apt_price = get_apt_price()
    normalization = zUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
  "function": "0xbeaa9e5ef5bee0781476a4adf293aae7dc3a28e9bd79fda89fca7211fb94c80::aggregator::three_split_route",
  "type_arguments": [
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0x1::aptos_coin::AptosCoin",
    "u8",
    "u8",
    "u8"
  ],
  "arguments": [
    8,
    "0",
    False,
    "400",
    10,
    "0",
    False,
    "550",
    7,
    "0",
    False,
    str(zUSDC_amount),
    str(APT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)
