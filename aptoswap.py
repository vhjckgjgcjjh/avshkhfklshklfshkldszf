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



def swap_APT_to_wUSDC_via_aptoswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_wUSDC_via_aptoswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    wUSDC_ideal = apt_price * normalization
    wUSDC_slip = wUSDC_ideal * SLIPPAGE
    wUSDC_slip_int = int(wUSDC_slip * Z6)

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::swap_x_to_y",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T"
  ],
  "arguments": [
    str(APT_amount),
    str(wUSDC_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def pool_APT_and_wUSDC_via_aptoswap(account, APT_amount: int):
    logger = setup_gay_logger('pool_APT_and_wUSDC_via_aptoswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    wUSDC_ideal = apt_price * normalization
    wUSDC_slip = wUSDC_ideal * SLIPPAGE
    wUSDC_slip_int = int(wUSDC_slip * Z6)

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::add_liquidity",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T"
  ],
  "arguments": [
    str(APT_amount),
    str(wUSDC_slip_int)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def unpool_APT_and_wUSDC_via_aptoswap(account, APT_amount: int):
    logger = setup_gay_logger('unpool_APT_and_wUSDC_via_aptoswap')

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::remove_liquidity",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T"
  ],
  "arguments": [
    str(APT_amount),
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_wUSDC_to_APT_via_aptoswap(account, wUSDC_amount: int):
    logger = setup_gay_logger('swap_wUSDC_to_APT_via_aptoswap')

    apt_price = get_apt_price()
    normalization = wUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::swap_y_to_x",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T"
  ],
  "arguments": [
    str(wUSDC_amount),
        str(APT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def swap_APT_to_wUSDT_via_aptoswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_wUSDT_via_aptoswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    wUSDT_ideal = apt_price * normalization
    wUSDT_slip = wUSDT_ideal * SLIPPAGE
    wUSDT_slip_int = int(wUSDT_slip * Z6)

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::swap_x_to_y",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xa2eda21a58856fda86451436513b867c97eecb4ba099da5775520e0f7492e852::coin::T"
  ],
  "arguments": [
    str(APT_amount),
    str(wUSDT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def pool_APT_and_wUSDT_via_aptoswap(account, APT_amount: int):
    logger = setup_gay_logger('pool_APT_and_wUSDT_via_aptoswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    wUSDT_ideal = apt_price * normalization
    wUSDT_slip = wUSDT_ideal * SLIPPAGE
    wUSDT_slip_int = int(wUSDT_slip * Z6)

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::add_liquidity",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xa2eda21a58856fda86451436513b867c97eecb4ba099da5775520e0f7492e852::coin::T"
  ],
  "arguments": [
    str(APT_amount),
    str(wUSDT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def unpool_APT_and_wUSDT_via_aptoswap(account, APT_amount: int):
    logger = setup_gay_logger('unpool_APT_and_wUSDT_via_aptoswap')

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::remove_liquidity",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xa2eda21a58856fda86451436513b867c97eecb4ba099da5775520e0f7492e852::coin::T"
  ],
  "arguments": [
    str(APT_amount),
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def swap_wUSDT_to_APT_via_aptoswap(account, wUSDT_amount: int):
    logger = setup_gay_logger('swap_wUSDT_to_APT_via_aptoswap')

    apt_price = get_apt_price()
    normalization = wUSDT_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
  "function": "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::swap_y_to_x",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xa2eda21a58856fda86451436513b867c97eecb4ba099da5775520e0f7492e852::coin::T"
  ],
  "arguments": [
    str(wUSDT_amount),
    str(APT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)



