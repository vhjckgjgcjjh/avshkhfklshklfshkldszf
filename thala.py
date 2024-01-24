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



def swap_APT_to_MOD(account, APT_amount: int):
    logger = setup_gay_logger('swap_zUSDC_to_MOD')

    apt_price = get_apt_price()
    normalization = APT_amount / Z8
    MOD_ideal = apt_price * normalization
    MOD_slip = MOD_ideal * SLIPPAGE
    MOD_slip_int = int(MOD_slip * Z6)

    payload = {
          "function": "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::weighted_pool_scripts::swap_exact_in",
          "type_arguments": [
            "0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01::mod_coin::MOD",
            "0x1::aptos_coin::AptosCoin",
            "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::base_pool::Null",
            "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::base_pool::Null",
            "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::weighted_pool::Weight_45",
            "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::weighted_pool::Weight_55",
            "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::base_pool::Null",
            "0x48271d39d0b05bd6efca2278f22277d6fcc375504f9839fd73f74ace240861af::base_pool::Null",
            "0x1::aptos_coin::AptosCoin",
            "0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01::mod_coin::MOD"
          ],
          "arguments": [
            str(APT_amount),
            str(MOD_slip_int)
          ],
          "type": "entry_function_payload"
        }

    submit_and_log_transaction(account, payload, logger)


def stake_MOD(account, amount_MOD: int):
    logger = setup_gay_logger('deposit_MOD')

    payload = {
        "type": "entry_function_payload",
        "function": "0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01::stability_pool_scripts::deposit_mod",
        "type_arguments": [
            "0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01::stability_pool::Crypto"
        ],
        "arguments": [
            str(amount_MOD)
        ],
    }

    submit_and_log_transaction(account, payload, logger)

