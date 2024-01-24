path = "/Users/maksimvasiliev/PycharmProjects/script_aptos/new script/pkey.txt" #шлях до файлу з ключами

with open(path, 'r') as file:
    # Считываем все строки из файла в список
    lines = file.readlines()
    number_of_lines = len(lines)

MAX_SLIPPAGE_PERCENT = 1
ALL_SLEEP = 2592000
CONST_SLEEP = 9
#затримка автоматично вираховується в залежності від кількості гаманців які вказані в pkey.txt, але можна прописати і власноруч
MIN_SLEEP = ((ALL_SLEEP/number_of_lines)/CONST_SLEEP)/2
MAX_SLEEP = ((ALL_SLEEP/number_of_lines)/CONST_SLEEP)*2

zUSDC_coin = "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC"
zUSDT_coin = "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDT"
MOD_coin = "0x6f986d146e4a90b828d8c12c14b6f4e003fdff11a8eecceceb63744363eaac01::mod_coin::MOD"
ceUSDT_coin = "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdtCoin"
ceUSDC_coin = "0x8d87a65ba30e09357fa2edea2c80dbac296e5dec2b18287113500b902942929d::celer_coin_manager::UsdcCoin"
tsAPT_coin = "0x84d7aeef42d38a5ffc3ccef853e1b82e4958659d16a7de736a29c55fbbeb0114::staked_aptos_coin::StakedAptosCoin"
vAPT_coin = "0x3c1d4a86594d681ff7e5d5a233965daeabdc6a15fe5672ceeda5260038857183::vcoins::V<0x1::aptos_coin::AptosCoin>"
amnisAPT_coin = "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a::amapt_token::AmnisApt"
STAKE_amnisAPT_coin = "0x111ae3e5bc816a5e63c2da97d0aa3886519e0cd5e4b046659fa35796bd11542a::stapt_token::StakedApt"
ditto_stakeAPT_coin = "0xd11107bdf0d6d7040c6c0bfbdecb6545191fdf13e8d8d259952f53e1713f61b5::staked_coin::StakedAptos"
wUSDC_coin = "0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T"
wUSDT_coin = "0xa2eda21a58856fda86451436513b867c97eecb4ba099da5775520e0f7492e852::coin::T"
aptswap_pool_coin = "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::LSP<0x1::aptos_coin::AptosCoin, 0x5e156f1207d0ebfa19a9eeff00d62a282278fb8719f4fab3a586a0a2c0fffbea::coin::T>"
aptswap_pool_coin2 = "0xa5d3ac4d429052674ed38adc62d010e52d7c24ca159194d17ddc196ddb7e480b::pool::LSP<0x1::aptos_coin::AptosCoin, 0xa2eda21a58856fda86451436513b867c97eecb4ba099da5775520e0f7492e852::coin::T>"

#API_ID і API_HASH можна взяти з https://my.telegram.org/auth, bot_token - токен який видає @BotFather
API_ID = 1111111
API_HASH = "1111111"
bot_token = "1111111111111"