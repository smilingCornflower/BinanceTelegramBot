from services import get_candles
from datetime import datetime
import statistics


def strategy_5(btc_volumes_48: list[float], only_text=True):
    vol_1: float = btc_volumes_48[-1]
    vol_2: float = btc_volumes_48[-2]
    vol_3: float = btc_volumes_48[-3]
    vol_4: float = btc_volumes_48[-4]

    check_1: bool = vol_1 > 2 * vol_2
    check_2: bool = vol_2 > vol_3
    check_3: bool = vol_1 + vol_2 > vol_3 + vol_4

    result: bool = (check_1 + check_2 + check_3) == 3

    output_text = (f"<b>PEPE_5</b> S[2.05%] SL[3%] 5H \n"
                   f"result: <b>{result}</b>\n"
                   f"vol[-1]: <b>{round(vol_1, 5)}</b> \n"
                   f"vol[-2]: <b>{round(vol_2, 5)}</b> \n"
                   f"vol[-3]: <b>{round(vol_3, 5)}</b> \n"
                   f"vol[-4]: <b>{round(vol_4, 5)}</b> \n"
                   f"vol[-1] > 2 * vol[-2]: {check_1}"
                   f"vol[-2] > vol[-3]: {check_2}"
                   f"vol[-1] + vol[-2] > vol[-3] + vol[-4]: {check_3}"
                   )

    if only_text:
        return output_text
    else:
        return result


def strategy_6(pepe_open_24: list[float], only_text=True):
    open_1: float = round(pepe_open_24[-1], 8)
    open_2: float = round(pepe_open_24[-2], 8)
    open_3: float = round(pepe_open_24[-3], 8)

    check_1: bool = (open_1 == open_2)
    check_2: bool = open_2 > open_3

    result: bool = (check_1 + check_2 == 2)

    output_text = (f"<b>PEPE_6</b> B[1.75%] SL[3%] 7H \n"
                   f"result: <b>{result}</b> \n"
                   f"open[-1]: <b>{open_1}</b> \n "
                   f"open[-2]: <b>{open_2}</b> \n "
                   f"open[-3]: <b>{open_3}</b> \n "
                   f"open[-1] == open[-2]: {check_1} \n"
                   f"open[-2] > open[-3]: {check_2} \n"
                   )

    if only_text:
        return output_text
    else:
        return result


# 1) (volume[-1] + volume[-2]) > (volume[-3] + volume[-4])
# 2) high[-1] < high[-2]
# 3) open[-2] > close[-2]
# 4) close[-2] > close[-1]
# 5) volume[-1] > (40mean_vol + 40std_vol)
#
# > NOT_7: S[1.85%] SL[3.5%] 5H
# result: True

def strategy_7(btc_candles_48: list[dict], only_text=True):
    vol_1: float = btc_candles_48[-1]['volume']
    vol_2: float = btc_candles_48[-2]['volume']
    vol_3: float = btc_candles_48[-3]['volume']
    vol_4: float = btc_candles_48[-4]['volume']
    high_1: float = btc_candles_48[-1]['high']
    high_2: float = btc_candles_48[-2]['high']
    open_2: float = btc_candles_48[-2]['open']
    close_1: float = btc_candles_48[-1]['close']
    close_2: float = btc_candles_48[-2]['close']

    volumes_40: list[float] = [candle['volume'] for candle in btc_candles_48[-40:]]

    std_dev_40_volume: float = statistics.stdev(volumes_40)
    mean_40_volume: float = statistics.mean(volumes_40)

    check_1: bool = (vol_1 + vol_2) > (vol_3 + vol_4)
    check_2: bool = high_1 < high_2
    check_3: bool = open_2 > close_2
    check_4: bool = close_2 > close_1
    check_5: bool = vol_1 > (std_dev_40_volume + mean_40_volume)

    result: bool = sum([check_1, check_2, check_3, check_4, check_5]) == 5

    output_text = (f"<b> NOT_7</b> S[1.85%] SL[3.5%] 5H \n"
                   f"result: <b>{result}</b> \n"
                   f"vol[-1]: <b>{round(vol_1, 8)}</b> \n"
                   f"vol[-2]: <b>{round(vol_2, 8)}</b> \n"
                   f"vol[-3]: <b>{round(vol_3, 8)}</b> \n"
                   f"vol[-4]: <b>{round(vol_4, 8)}</b> \n"
                   f"high[-1]: <b>{round(high_1, 8)}</b> \n"
                   f"high[-2]: <b>{round(high_2, 8)}</b> \n"
                   f"open[-2]: <b>{round(open_2, 8)}</b> \n"
                   f"close[-1]: <b>{round(close_1, 8)}</b> \n"
                   f"close[-2]: <b>{round(close_2, 8)}</b> \n"
                   f"mean_40_volume: <b>{round(mean_40_volume, 8)}</b> \n"
                   f"std_dev_40_volume: <b>{round(std_dev_40_volume, 8)}</b> \n"
                   f"vol[-1] + vol[-2] > vol[-3] + vol[-4]: {check_1} \n"
                   f"high[-1] < high[-2]: {check_2} \n"
                   f"open[-2] > close[-2]: {check_3} \n"
                   f"close[-2] > close[-1]: {check_4} \n"
                   f"vol[-1] > (mean_40 + std_40): {check_5} \n"
                   )
    if only_text:
        return output_text
    else:
        return result


def new_strategies(necessary_strategy: str = 'all'):
    btc = 'BTCUSDT'
    pepe = 'PEPEUSDT'

    btc_candles_48 = get_candles(currency=btc, start_time_mode='two_days')
    pepe_candles_24 = get_candles(currency=pepe, start_time_mode='day')

    request_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    btc_volumes_48 = [candle['volume'] for candle in btc_candles_48]
    pepe_open_24 = [candle['open'] for candle in pepe_candles_24]

    match necessary_strategy:
        case '567':
            output_text_5 = strategy_5(btc_volumes_48)
            output_text_6 = strategy_6(pepe_open_24)
            output_text_7 = strategy_7(btc_candles_48)
            output_text = (f"Time: <b>{request_time}</b>\n\n"
                           f"{output_text_5} \n"
                           f"{output_text_6} \n"
                           f"{output_text_7} \n"
                           )
        case 'strategy_5':
            output = strategy_5(btc_volumes_48)
        case 'strategy_6':
            output = strategy_6(pepe_open_24)
