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



def swap_APT_to_zUSDC_via_pancakeswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDC_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDC_ideal = apt_price * normalization
    zUSDC_slip = zUSDC_ideal * SLIPPAGE
    zUSDC_slip_int = int(zUSDC_slip * Z6)

    payload = {
      "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
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

def swap_zUSDC_to_APT_via_pancakeswap(account, zUSDC_amount: int):
    logger = setup_gay_logger('swap_zUSDC_to_APT_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = zUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
        "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
        "type_arguments": [
            "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
            "0x1::aptos_coin::AptosCoin"
        ],
        "arguments": [
            str(zUSDC_amount),
            str(APT_slip_int)
        ],
        "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)



def swap_APT_to_ceUSDT_via_pancakeswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_ceUSDT_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    ceUSDT_ideal = apt_price * normalization
    ceUSDT_slip = ceUSDT_ideal * SLIPPAGE
    ceUSDT_slip_int = int(ceUSDT_slip * Z6)

    payload = {
      "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
      "type_arguments": [
        "0x1::aptos_coin::AptosCoin",
        "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdtCoin"
      ],
      "arguments": [
        str(APT_amount),
        str(ceUSDT_slip_int)
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)

def swap_ceUSDT_to_APT_via_pancakeswap(account, ceUSDT_amount: int):
    logger = setup_gay_logger('swap_ceUSDT_to_APT_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = ceUSDT_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
          "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
          "type_arguments": [
            "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdtCoin",
            "0x1::aptos_coin::AptosCoin"
          ],
          "arguments": [
            str(ceUSDT_amount),
            str(APT_slip_int)
          ],
          "type": "entry_function_payload"
        }

    submit_and_log_transaction(account, payload, logger)



def swap_APT_to_ceUSDC_via_pancakeswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_ceUSDC_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    ceUSDC_ideal = apt_price * normalization
    ceUSDC_slip = ceUSDC_ideal * SLIPPAGE
    ceUSDC_slip_int = int(ceUSDC_slip * Z6)

    payload = {
      "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
      "type_arguments": [
        "0x1::aptos_coin::AptosCoin",
        "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdcCoin"
      ],
      "arguments": [
        str(APT_amount),
        str(ceUSDC_slip_int)
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)

def swap_ceUSDC_to_APT_via_pancakeswap(account, ceUSDC_amount: int):
    logger = setup_gay_logger('swap_ceUSDC_to_APT_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = ceUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
      "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
      "type_arguments": [
        "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdcCoin",
        "0x1::aptos_coin::AptosCoin"
      ],
      "arguments": [
        str(ceUSDC_amount),
        str(APT_slip_int)
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)



def swap_APT_to_zUSDT_via_pancakeswap(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDT_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDT_ideal = apt_price * normalization
    zUSDT_slip = zUSDT_ideal * SLIPPAGE
    zUSDT_slip_int = int(zUSDT_slip * Z6)

    payload = {
      "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
      "type_arguments": [
        "0x1::aptos_coin::AptosCoin",
        "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT"
      ],
      "arguments": [
        str(APT_amount),
        str(zUSDT_slip_int)
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)

def swap_zUSDT_to_APT_via_pancakeswap(account, zUSDT_amount: int):
    logger = setup_gay_logger('swap_zUSDT_to_APT_via_pancakeswap')

    apt_price = get_apt_price()
    normalization = zUSDT_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
      "function": "0xc7efb4076dbe143cbcd98cfaaa929ecfc8f299203dfff63b95ccb6bfe19850fa::router::swap_exact_input",
      "type_arguments": [
        "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
        "0x1::aptos_coin::AptosCoin"
      ],
      "arguments": [
        str(zUSDT_amount),
        str(APT_slip_int)
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)