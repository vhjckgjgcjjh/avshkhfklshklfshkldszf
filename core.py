import random
import time
from aptos_sdk.account import Account
from pyrogram import Client

from pancakeswap import (swap_APT_to_zUSDC_via_pancakeswap, swap_zUSDC_to_APT_via_pancakeswap,
                         swap_APT_to_ceUSDT_via_pancakeswap, swap_ceUSDT_to_APT_via_pancakeswap,
                         swap_APT_to_ceUSDC_via_pancakeswap, swap_ceUSDC_to_APT_via_pancakeswap,
                         swap_APT_to_zUSDT_via_pancakeswap, swap_zUSDT_to_APT_via_pancakeswap)

from sushiswap import (swap_APT_to_zUSDC_via_sushiswap, swap_zUSDC_to_APT_via_sushiswap,
                       swap_APT_to_zUSDT_via_sushiswap, swap_zUSDT_to_APT_via_sushiswap)

from thala import (swap_APT_to_MOD, stake_MOD)

from tortuga import (stake_apt_via_tortuga, unstake_apt_via_tortuga)

from liquidswap import (swap_APT_to_zUSDC_via_liquidswap, swap_zUSDC_to_APT_via_liquidswap,
                        swap_APT_to_zUSDT_via_liquidswap, swap_zUSDT_to_APT_via_liquidswap)

from aptin import (stake_apt_via_aptin, borrow_apt_via_aptin,
                   repay_apt_via_aptin, withdraw_apt_via_aptin)

from abel import (swap_APT_to_zUSDC_via_abel, swap_zUSDC_to_APT_via_abel,
                  swap_APT_to_zUSDT_via_abel, swap_zUSDT_to_APT_via_abel)

from amnis import (stake_APT_via_amnis, swap_APT_via_liquidswap,
                   stake2_APT_via_amnis, swap2_APT_via_liquidswap)

from merkle import (open_merkle_order)

from ditto import (stake_apt_via_ditto, unstake_apt_via_ditto)

from baptswap import (swap_APT_to_zUSDC_via_baptswap, swap_zUSDC_to_APT_via_baptswap)

from argo import (stake_apt_via_argo, unstake_apt_via_argo)

from aptoswap import (swap_APT_to_wUSDC_via_aptoswap, swap_wUSDC_to_APT_via_aptoswap,
                      swap_APT_to_wUSDT_via_aptoswap, swap_wUSDT_to_APT_via_aptoswap,
                      pool_APT_and_wUSDC_via_aptoswap, unpool_APT_and_wUSDC_via_aptoswap,
                      pool_APT_and_wUSDT_via_aptoswap, unpool_APT_and_wUSDT_via_aptoswap)

from hippo import (swap_APT_to_zUSDC_via_hippo, swap_zUSDC_to_APT_via_hippo,
                   swap_APT_to_zUSDT_via_hippo, swap_zUSDT_to_APT_via_hippo)

from umi import (swap_APT_to_zUSDC_via_umi, swap_zUSDC_to_APT_via_umi)

from gator import (deposit_APT_to_gator, swap_APT_to_USDC_via_gator,
                   swap_USDC_to_APT_via_gator, withdraw_APT_to_gator)

from swapgpt import (deposit_APT_to_swapgpt, swap_APT_to_USDC_via_swapgpt,
                     swap_USDC_to_APT_via_swapgpt, withdraw_APT_to_swapgpt)

from kanalabs import (deposit_APT_to_kanalabs, swap_APT_to_USDC_via_kanalabs,
                      swap_USDC_to_APT_via_kanalabs, withdraw_APT_to_kanalabs)

from ariesmarket import (deposit_APT_to_ariesmarkets, swap_APT_to_USDC_via_ariesmarkets,
                          swap_USDC_to_APT_via_ariesmarkets, withdraw_APT_to_ariesmarkets)



from utils import get_coin_value, get_account_balance, check_registration
from constant import API_ID, path, API_HASH, bot_token, zUSDC_coin, amnisAPT_coin, aptswap_pool_coin2, wUSDT_coin, aptswap_pool_coin, zUSDT_coin, wUSDC_coin, ditto_stakeAPT_coin,  STAKE_amnisAPT_coin, tsAPT_coin, vAPT_coin, MOD_coin, ceUSDT_coin, ceUSDC_coin, MIN_SLEEP, MAX_SLEEP
from logger import setup_gay_logger
from transactions import Rest_Client

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH,
             bot_token=bot_token)

Z8 = 10**8
Z6 = 10**6

def process_key(key):
    account = Account.load_key(key)
    address = account.address()
    print(address)
    logger = setup_gay_logger(f"{address}")
    logger.info("Getting initial wallet balance...")
    initial_balance_APT = get_account_balance(Rest_Client, account)
    fix = initial_balance_APT / Z8
    logger.info(f"Starting wallet balance is {fix} APT")

    #початок скріпту
    half_APT = int(initial_balance_APT * 0.5)
    quarter_APT = int(initial_balance_APT * 0.25)
    for _ in range(random.randint(3, 7)):
        # 16-19, свапалки на еконії
        dex = random.randint(16, 19)
        if dex == 1:
            pancake = random.randint(1, 4)
            if pancake == 1:
                #свап на панкейку_zUSDC
                swap_APT_to_zUSDC_via_pancakeswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDC coin value...")
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                swap_zUSDC_to_APT_via_pancakeswap(account, zUSDC_value)
                time.sleep(random.randint(3, 20))
            if pancake == 2:
                #свап на панкейку_ceUSDT
                swap_APT_to_ceUSDT_via_pancakeswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting ceUSDT coin value...")
                ceUSDT_value = int(get_coin_value(address, ceUSDT_coin))
                swap_ceUSDT_to_APT_via_pancakeswap(account, ceUSDT_value)
                time.sleep(random.randint(3, 20))
            if pancake == 3:
                #свап на панкейку_ceUSDC
                swap_APT_to_ceUSDC_via_pancakeswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting ceUSDC coin value...")
                ceUSDC_value = int(get_coin_value(address, ceUSDC_coin))
                swap_ceUSDC_to_APT_via_pancakeswap(account, ceUSDC_value)
                time.sleep(random.randint(3, 20))
            if pancake == 4:
                #свап на панкейку_zUSDT
                swap_APT_to_zUSDT_via_pancakeswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDT coin value...")
                zUSDT_value = int(get_coin_value(address, zUSDT_coin))
                swap_zUSDT_to_APT_via_pancakeswap(account, zUSDT_value)
                time.sleep(random.randint(3, 20))
        if dex == 2:
            sushi = random.randint(1, 2)
            if sushi == 1:
                # свап на сушах_zUSDC
                swap_APT_to_zUSDC_via_sushiswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDC coin value...")
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                swap_zUSDC_to_APT_via_sushiswap(account, zUSDC_value)
                time.sleep(random.randint(3, 20))
            if sushi == 2:
                # свап на сушах_zUSDC
                swap_APT_to_zUSDT_via_sushiswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDT coin value...")
                zUSDT_value = int(get_coin_value(address, zUSDT_coin))
                swap_zUSDT_to_APT_via_sushiswap(account, zUSDT_value)
                time.sleep(random.randint(3, 20))
        if dex ==3:
            swap_APT_to_MOD(account, random.randint(21000, 31000))
            time.sleep(random.randint(5, 10))
            stake_MOD(account, random.randint(8000, 21000))
            time.sleep(random.randint(3, 20))
        if dex == 4:
            stake_apt_via_tortuga(account, quarter_APT)
            logger.info("Getting tsAPT coin value...")
            time.sleep(random.randint(5, 10))
            tsAPT_value = int(get_coin_value(address, tsAPT_coin))
            unstake_apt_via_tortuga(account, tsAPT_value)
            time.sleep(random.randint(3, 20))
        if dex == 5:
            time.sleep(random.randint(3, 20))
            liquid = random.randint(1, 2)
            if liquid == 1:
                swap_APT_to_zUSDC_via_liquidswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDC coin value...")
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                swap_zUSDC_to_APT_via_liquidswap(account, zUSDC_value)
                time.sleep(random.randint(3, 20))
            if liquid == 2:
                swap_APT_to_zUSDT_via_liquidswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDT coin value...")
                zUSDT_value = int(get_coin_value(address, zUSDT_coin))
                swap_zUSDT_to_APT_via_liquidswap(account, zUSDT_value)
                time.sleep(random.randint(3, 20))
        if dex == 6:
            stake_apt_via_aptin(account)
            time.sleep(random.randint(5, 10))
            borrow_apt_via_aptin(account)
            time.sleep(random.randint(5, 10))
            repay_apt_via_aptin(account)
            time.sleep(random.randint(5, 10))
            logger.info("Getting vAPT coin value...")
            vAPT_value = int(get_coin_value(address, vAPT_coin))
            withdraw_apt_via_aptin(account, vAPT_value, address)
            time.sleep(random.randint(3, 20))
        if dex == 7:
            abel = random.randint(1, 2)
            if abel == 1:
                swap_APT_to_zUSDC_via_abel(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDC coin value...")
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                swap_zUSDC_to_APT_via_abel(account, zUSDC_value)
                time.sleep(random.randint(3, 20))
            if abel == 2:
                swap_APT_to_zUSDT_via_abel(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                logger.info("Getting zUSDT coin value...")
                zUSDT_value = int(get_coin_value(address, zUSDT_coin))
                swap_zUSDT_to_APT_via_abel(account, zUSDT_value)
                time.sleep(random.randint(3, 20))
        if dex == 8:
            amnis = random.randint(1, 2)
            if amnis == 1:
                stake_APT_via_amnis(account, address)
                time.sleep(random.randint(5, 10))
                logger.info("Getting amnisAPT_coin coin value...")
                amnisAPT_value = int(get_coin_value(address, amnisAPT_coin))
                swap_APT_via_liquidswap(account, amnisAPT_value)
                time.sleep(random.randint(3, 20))
            if amnis == 2:
                stake2_APT_via_amnis(account, address)
                time.sleep(random.randint(5, 10))
                logger.info("Getting STAKE_amnisAPT_coin value...")
                STAKE_amnisAPT_value = int(get_coin_value(address, STAKE_amnisAPT_coin))
                swap2_APT_via_liquidswap(account, STAKE_amnisAPT_value)
                time.sleep(random.randint(3, 20))
        if dex == 9:
            if fix > 0.3:
                apt_to_USDC = random.randint(1, 4)
                if apt_to_USDC == 1:
                    swap_APT_to_zUSDC_via_pancakeswap(account, random.randint(27954976, 29954976))
                    time.sleep(random.randint(5, 10))
                if apt_to_USDC == 2:
                    swap_APT_to_zUSDC_via_sushiswap(account, random.randint(27954976, 29954976))
                    time.sleep(random.randint(5, 10))
                if apt_to_USDC == 3:
                    swap_APT_to_zUSDC_via_liquidswap(account, random.randint(27954976, 29954976))
                    time.sleep(random.randint(5, 10))
                if apt_to_USDC == 4:
                    swap_APT_to_zUSDC_via_abel(account, random.randint(27954976, 29954976))
                    time.sleep(random.randint(5, 10))
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                open_merkle_order(account, zUSDC_value)
                time.sleep(random.randint(5, 10))
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                USDC_to_APT = random.randint(1, 4)
                if USDC_to_APT == 1:
                    swap_zUSDC_to_APT_via_pancakeswap(account, zUSDC_value)
                    time.sleep(random.randint(3, 20))
                if USDC_to_APT == 2:
                    swap_zUSDC_to_APT_via_sushiswap(account, zUSDC_value)
                    time.sleep(random.randint(3, 20))
                if USDC_to_APT == 3:
                    swap_zUSDC_to_APT_via_liquidswap(account, zUSDC_value)
                    time.sleep(random.randint(3, 20))
                if USDC_to_APT == 4:
                    swap_zUSDC_to_APT_via_abel(account, zUSDC_value)
                    time.sleep(random.randint(3, 20))

        if dex == 10:
            stake_apt_via_ditto(account)
            time.sleep(random.randint(5, 10))
            ditto_stakeAPT_value = int(get_coin_value(address, ditto_stakeAPT_coin))
            unstake_apt_via_ditto(account, ditto_stakeAPT_value)
            time.sleep(random.randint(3, 20))
        if dex == 11:
            swap_APT_to_zUSDC_via_baptswap(account, quarter_APT)
            time.sleep(random.randint(5, 10))
            logger.info("Getting zUSDC coin value...")
            zUSDC_value = int(get_coin_value(address, zUSDC_coin))
            swap_zUSDC_to_APT_via_baptswap(account, zUSDC_value)
            time.sleep(random.randint(3, 20))
        if dex == 12:
            stake_apt_via_argo(account, quarter_APT)
            time.sleep(random.randint(5, 10))
            unstake_apt_via_argo(account, quarter_APT)
            time.sleep(random.randint(3, 20))
        if dex == 13:
            aptoswap = random.randint(1, 2)
            if aptoswap == 1:
                time.sleep(random.randint(5, 10))
                swap_APT_to_wUSDC_via_aptoswap(account, quarter_APT)
                pool = random.randint(1, 2)
                if pool == 1:
                    pool_APT_and_wUSDC_via_aptoswap(account, quarter_APT)
                    time.sleep(random.randint(5, 10))
                    logger.info("Getting aptswap_pool coin value...")
                    aptswap_pool_value = int(get_coin_value(address, aptswap_pool_coin))
                    unpool_APT_and_wUSDC_via_aptoswap(account, aptswap_pool_value)
                time.sleep(random.randint(5, 10))
                logger.info("Getting wUSDC coin value...")
                wUSDC_value = int(get_coin_value(address, wUSDC_coin))
                swap_wUSDC_to_APT_via_aptoswap(account, wUSDC_value)
                time.sleep(random.randint(3, 20))
            if aptoswap == 2:
                swap_APT_to_wUSDT_via_aptoswap(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                unpool = random.randint(1, 2)
                if unpool == 1:
                    pool_APT_and_wUSDT_via_aptoswap(account, quarter_APT)
                    time.sleep(random.randint(5, 10))
                    logger.info("Getting aptswap_pool coin value...")
                    aptswap_pool_value = int(get_coin_value(address, aptswap_pool_coin2))
                    unpool_APT_and_wUSDT_via_aptoswap(account, aptswap_pool_value)
                    time.sleep(random.randint(3, 20))
                time.sleep(random.randint(5, 10))
                logger.info("Getting wUSDT coin value...")
                wUSDT_value = int(get_coin_value(address, wUSDT_coin))
                swap_wUSDT_to_APT_via_aptoswap(account, wUSDT_value)
                time.sleep(random.randint(3, 20))
        if dex == 14:
            hippo = random.randint(1, 2)
            if hippo == 1:
                swap_APT_to_zUSDC_via_hippo(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                zUSDC_value = int(get_coin_value(address, zUSDC_coin))
                swap_zUSDC_to_APT_via_hippo(account, zUSDC_value)
                time.sleep(random.randint(3, 20))
            if hippo == 2:
                swap_APT_to_zUSDT_via_hippo(account, quarter_APT)
                time.sleep(random.randint(5, 10))
                zUSDT_value = int(get_coin_value(address, zUSDT_coin))
                swap_zUSDT_to_APT_via_hippo(account, zUSDT_value)
                time.sleep(random.randint(3, 20))
        if dex == 15:
            swap_APT_to_zUSDC_via_umi(account, quarter_APT)
            time.sleep(random.randint(5, 10))
            zUSDC_value = int(get_coin_value(address, zUSDC_coin))
            swap_zUSDC_to_APT_via_umi(account, zUSDC_value)
            time.sleep(random.randint(3, 20))
        if dex == 16:
            sum_depo = random.randint(54000000, 57000000)
            deposit_APT_to_gator(account, sum_depo)
            time.sleep(random.randint(5, 10))
            swap_APT_to_USDC_via_gator(account)
            time.sleep(random.randint(5, 10))
            swap_USDC_to_APT_via_gator(account)
            time.sleep(random.randint(5, 10))
            withdraw_APT_to_gator(account, sum_depo-200000)
            time.sleep(random.randint(3, 20))
        if dex == 17:
            #trade
            sum_depo = random.randint(54000000, 57000000)
            deposit_APT_to_swapgpt(account, sum_depo)
            time.sleep(random.randint(5, 10))
            swap_APT_to_USDC_via_swapgpt(account)
            time.sleep(random.randint(5, 10))
            swap_USDC_to_APT_via_swapgpt(account)
            time.sleep(random.randint(5, 10))
            withdraw_APT_to_swapgpt(account, sum_depo - 200000)
            time.sleep(random.randint(3, 20))
        if dex == 18:
            # trade
            sum_depo = random.randint(54000000, 57000000)
            deposit_APT_to_kanalabs(account, sum_depo)
            time.sleep(random.randint(5, 10))
            swap_APT_to_USDC_via_kanalabs(account)
            time.sleep(random.randint(5, 10))
            swap_USDC_to_APT_via_kanalabs(account)
            time.sleep(random.randint(5, 10))
            withdraw_APT_to_kanalabs(account, sum_depo - 200000)
            time.sleep(random.randint(3, 20))
        if dex == 19:
            # trade
            sum_depo = random.randint(54000000, 57000000)
            deposit_APT_to_ariesmarkets(account, sum_depo)
            time.sleep(random.randint(5, 10))
            swap_APT_to_USDC_via_ariesmarkets(account)
            time.sleep(random.randint(5, 10))
            swap_USDC_to_APT_via_ariesmarkets(account)
            time.sleep(random.randint(5, 10))
            withdraw_APT_to_ariesmarkets(account, sum_depo - 200000)
            time.sleep(random.randint(3, 20))




    logger.info("Process completed successfully.")
    app.start()
    app.send_message("vladvasiliev", f"Process completed successfully")
    app.stop()
    return 0

while True:
    try:
        with open(path, 'r') as file:
            pkeys = file.readlines()

        for pkey in pkeys:
            pkeys2 = [pkey.strip() for pkey in pkeys]
            random_key = random.choice(pkeys2)
            result = process_key(random_key)

            time.sleep(random.randint(MIN_SLEEP, MAX_SLEEP))

    except Exception as e:
        app.start()
        app.send_message("vladvasiliev", f"у нас тут ошибочка, друг:\n\n {e}")
        app.stop()