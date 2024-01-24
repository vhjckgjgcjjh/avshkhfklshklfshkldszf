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



def swap_APT_to_zUSDC_via_hippo(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDC_via_hippo')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDC_ideal = apt_price * normalization
    zUSDC_slip = zUSDC_ideal * SLIPPAGE
    zUSDC_slip_int = int(zUSDC_slip * Z6)

    payload = {
  "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0x7fd500c11216f0fe3095d0c4b8aa4d64a4e2e04f83758462f2b127255643615::thl_coin::THL",
    "0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01::mod_coin::MOD",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::curves::Uncorrelated",
    "u8",
    "u8"
  ],
  "arguments": [
    3,
    3,
    "2",
    False,
    14,
    "18027592649162752",
    False,
    14,
    "18049582881570816",
    True,
    str(APT_amount),
    str(zUSDC_slip_int)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_zUSDC_to_APT_via_hippo(account, zUSDC_amount: int):
    logger = setup_gay_logger('swap_zUSDC_to_APT_via_hippo')

    apt_price = get_apt_price()
    normalization = zUSDC_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
  "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
  "type_arguments": [
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0x1::string::String",
    "0x1::string::String",
    "0x1::aptos_coin::AptosCoin",
    "u8",
    "0x1::string::String",
    "0x1::string::String"
  ],
  "arguments": [
    1,
    11,
    "0",
    False,
    0,
    "0",
    False,
    0,
    "0",
    False,
    str(zUSDC_amount),
    str(APT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)

def swap_APT_to_zUSDT_via_hippo(account, APT_amount: int):
    logger = setup_gay_logger('swap_APT_to_zUSDT_via_hippo')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    zUSDT_ideal = apt_price * normalization
    zUSDT_slip = zUSDT_ideal * SLIPPAGE
    zUSDT_slip_int = int(zUSDT_slip * Z6)

    payload = {
  "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::swap",
  "type_arguments": [
    "0x1::aptos_coin::AptosCoin",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::WETH",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
    "u8",
    "0x190d44266241744264b964a37b8f09863167a12d3e70cda39376cfb4e3561e12::curves::Uncorrelated",
    "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::curves::Stable"
  ],
  "arguments": [
    3,
    11,
    "0",
    True,
    3,
    "0",
    False,
    3,
    "3",
    True,
    str(APT_amount),
        str(zUSDT_slip_int)
  ],
  "type": "entry_function_payload"
}
    submit_and_log_transaction(account, payload, logger)

def swap_zUSDT_to_APT_via_hippo(account, zUSDT_amount: int):
    logger = setup_gay_logger('swap_zUSDT_to_APT_via_hippo')

    apt_price = get_apt_price()
    normalization = zUSDT_amount / Z6
    APT_ideal = normalization / apt_price
    APT_slip = APT_ideal * SLIPPAGE
    APT_slip_int = int(APT_slip * Z8)

    payload = {
  "function": "0x890812a6bbe27dd59188ade3bbdbe40a544e6e104319b7ebc6617d3eb947ac07::aggregator::split_swap",
  "type_arguments": [
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT",
    "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5::staked_coin::StakedAptos",
    "0x1::aptos_coin::AptosCoin",
    "u8",
    "0x1::string::String",
    "0x1::string::String",
    "u8",
    "0x1::string::String",
    "0x1::string::String",
    "u8",
    "0x163df34fccbf003ce219d3f1d9e70d140b60622cb9dd47599c25fb2f797ba6e::curves::Stable",
    "0x1::string::String"
  ],
  "arguments": [
    "0x0c",
    [
      "0"
    ],
    [
      False
    ],
    [
      "60000"
    ],
    "0x0b",
    [
      "0"
    ],
    [
      False
    ],
    [
      "60000"
    ],
    "0x0b03",
    [
      "0",
      "3"
    ],
    [
      False,
      False
    ],
    [
      "16800",
      "43200"
    ],
    str(zUSDT_amount),
      str(APT_slip_int)
  ],
  "type": "entry_function_payload"
}

    submit_and_log_transaction(account, payload, logger)



