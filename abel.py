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



def swap_APT_to_zUSDC_via_abel(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDC_via_abel')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDC_ideal = apt_price * normalization
    print(zUSDC_ideal, "zUSDC_ideal")
    zUSDC_slip = zUSDC_ideal * SLIPPAGE
    print(zUSDC_slip, "zUSDC_slip")
    zUSDC_slip_int = int(zUSDC_slip * Z6)
    print(zUSDC_slip_int, "zUSDC_slip_int")


    payload = {
  "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
    "0x1::string::String",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "u8",
    "u8",
    "0x1::string::String"
  ],
  "arguments": [
    2,
    11,
    "0",
    True,
    12,
    "0",
    False,
    0,
    "0",
    False,
    str(APT_amount),
    "0"
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_zUSDC_to_APT_via_abel(account, zUSDC_amount: int):
    logger = setup_gay_logger('swap_zUSDC_to_APT_via_abel')

    apt_price = get_apt_price()
    normalization = zUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
  "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
  "type_arguments": [
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T",
    "0x1::string::String",
    "0x1::aptos_coin::AptosCoin",
    "u8",
    "u8",
    "0x1::string::String"
  ],
  "arguments": [
    2,
    12,
    "0",
    False,
    12,
    "2",
    False,
    0,
    "0",
    False,
    str(zUSDC_amount),
    "0"
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def swap_APT_to_zUSDT_via_abel(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDT_via_abel')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDT_ideal = apt_price * normalization
    zUSDT_slip = zUSDT_ideal * SLIPPAGE
    zUSDT_slip_int = int(zUSDT_slip * Z6)

    payload = {
      "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
      "type_arguments": [
        "0x1::aptos_coin::AptosCoin",
        "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdcCoin",
        "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
        "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
        "u8",
        "u8",
        "u8"
      ],
      "arguments": [
        3,
        11,
        "0",
        True,
        12,
        "0",
        True,
        12,
        "0",
        True,
        str(APT_amount),
        "0"
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)

def swap_zUSDT_to_APT_via_abel(account, zUSDT_amount: int):
    logger = setup_gay_logger('swap_zUSDT_to_APT_via_abel')

    apt_price = get_apt_price()
    normalization = zUSDT_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
      "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
      "type_arguments": [
        "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
        "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
        "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T",
        "0x1::aptos_coin::AptosCoin",
        "u8",
        "u8",
        "u8"
      ],
      "arguments": [
        3,
        12,
        "0",
        False,
        12,
        "0",
        False,
        12,
        "2",
        False,
        str(zUSDT_amount),
        "0"
      ],
      "type": "entry_function_payload"
    }

    submit_and_log_transaction(account, payload, logger)



