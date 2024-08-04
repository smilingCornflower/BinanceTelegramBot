from constants import bot, users_id, developer_id, ALERT_COMPONENTS
from services import get_candles
from datetime import datetime
import time
import statistics


def strategy_1(volumes_48, only_text=True):
    volumes_20 = volumes_48[-20:]
    volumes_24 = volumes_48[-24:]
    current_volume = volumes_48[-1]

    std_dev_20_volume = statistics.stdev(volumes_20)
    mean_24_volume = statistics.mean(volumes_24)
    formula = 2 * std_dev_20_volume + mean_24_volume
    result: bool = formula < current_volume

    if only_text:
        output_text = (f"<b>NOT_1</b>[3.1%] result: <b>{result}</b>\n"
                       f"std_dev_20_volume: <b>{round(std_dev_20_volume, 5)}</b>\n"
                       f"mean_24_volume: <b>{round(mean_24_volume, 5)}</b>\n"
                       f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                       f"2 * std_dev_20 + mean_24: <b>{round(formula, 5)}</b>\n"
                       )
        return output_text
    return result, formula, std_dev_20_volume, mean_24_volume


def strategy_2(volumes_48, only_text=True):
    volumes_40 = volumes_48[-40:]
    current_volume = volumes_48[-1]
    std_dev_40_volume = statistics.stdev(volumes_40)
    mean_40_volume = statistics.mean(volumes_40)

    formula = (std_dev_40_volume + mean_40_volume) / current_volume
    result: bool = formula > 3.75
    if only_text:
        output_text = (f"<b>NOT_2</b>[3.7%] result: <b>{result}</b>\n"
                       f"std_dev_40_volume: <b>{round(std_dev_40_volume, 5)}</b>\n"
                       f"mean_40_volume: <b>{round(mean_40_volume, 5)}</b>\n"
                       f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                       f"(std_dev_40 + mean_40) / volume: <b>{round(formula, 5)}</b>\n"
                       )
        return output_text
    return result, formula, std_dev_40_volume, mean_40_volume


def strategy_3(volumes_48, only_text=True):
    volumes_20 = volumes_48[-20:]
    volumes_24 = volumes_48[-24:]
    current_volume = volumes_48[-1]

    std_dev_20_volume = statistics.stdev(volumes_20)
    mean_24_volume = statistics.mean(volumes_24)
    formula = 2.35 * std_dev_20_volume + mean_24_volume
    result: bool = formula < current_volume

    if only_text:
        output_text = (f"<b>IO_3</b>[1.65%] result: <b>{result}</b>\n"
                       f"std_dev_20_volume: <b>{round(std_dev_20_volume, 5)}</b>\n"
                       f"mean_24_volume: <b>{round(mean_24_volume, 5)}</b>\n"
                       f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                       f"2.35 * std_dev_20 + mean_24: <b>{round(formula, 5)}</b>\n"
                       )
        return output_text

    return result, formula, std_dev_20_volume, mean_24_volume


def strategy_4(volumes_48, only_text=True):
    volumes_40 = volumes_48[-40:]
    current_volume = volumes_48[-1]

    std_dev_40_volume = statistics.stdev(volumes_40)
    mean_40_volume = statistics.mean(volumes_40)
    formula = (std_dev_40_volume + mean_40_volume) / current_volume
    result = formula > 3.6

    if only_text:
        output_text = (f"<b>IO_4</b>[4.4%] result: <b>{result}</b>\n"
                       f"std_dev_40_volume: <b>{round(std_dev_40_volume, 5)}</b>\n"
                       f"mean_40_volume: <b>{round(mean_40_volume, 5)}</b>\n"
                       f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                       f"(std_dev_40 + mean_40) / volume: <b>{round(formula, 5)}</b>\n"
                       )
        return output_text
    return result, formula, std_dev_40_volume, mean_40_volume


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
                   f"vol[-1]: <b>{vol_1:.5f}</b> \n"
                   f"vol[-2]: <b>{vol_2:.5f}</b> \n"
                   f"vol[-3]: <b>{vol_3:.5f}</b> \n"
                   f"vol[-4]: <b>{vol_4:.5f}</b> \n"
                   f"vol[-1] > 2 * vol[-2]: <b>{check_1}</b> \n"
                   f"vol[-2] > vol[-3]: <b>{check_2}</b> \n"
                   f"vol[-1] + vol[-2] > vol[-3] + vol[-4]: <b>{check_3}</b> \n"
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
                   f"open[-1]: <b>{open_1:.8f}</b> \n "
                   f"open[-2]: <b>{open_2:.8f}</b> \n "
                   f"open[-3]: <b>{open_3:.8f}</b> \n "
                   f"open[-1] == open[-2]: {check_1} \n"
                   f"open[-2] > open[-3]: {check_2} \n"
                   )

    if only_text:
        return output_text
    else:
        return result


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
                   f"vol[-1]: <b>{vol_1:.5f}</b> \n"
                   f"vol[-2]: <b>{vol_2:.5f}</b> \n"
                   f"vol[-3]: <b>{vol_3:.5f}</b> \n"
                   f"vol[-4]: <b>{vol_4:.5f}</b> \n"
                   f"high[-1]: <b>{high_1:.5f}</b> \n"
                   f"high[-2]: <b>{high_2:.5f}</b> \n"
                   f"open[-2]: <b>{open_2:.5f}</b> \n"
                   f"close[-1]: <b>{close_1:.5f}</b> \n"
                   f"close[-2]: <b>{close_2:.5f}</b> \n"
                   f"mean_40_volume: <b>{mean_40_volume:.5f}</b> \n"
                   f"std_dev_40_volume: <b>{std_dev_40_volume:.5f}</b> \n"
                   f"vol[-1] + vol[-2]: > vol[-3] + vol[-4]: <b>{check_1}</> \n"
                   f"high[-2] > high[-1]: <b>{check_2}</> \n"
                   f"open[-2] > close[-2]: <b>{check_3}</> \n"
                   f"close[-2] > close[-1]: <b>{check_4}</> \n"
                   f"vol[-1] > (mean_40 + std_40): <b>{check_5}</> \n"
                   )

    if only_text:
        return output_text
    else:
        return result


def strategies(necessary_strategy: str):
    btc = 'BTCUSDT'
    pepe = 'PEPEUSDT'

    btc_candles_48 = get_candles(currency=btc, start_time_mode='two_days')
    pepe_candles_24 = get_candles(currency=pepe, start_time_mode='day')

    request_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    btc_volumes_48 = [candle['volume'] for candle in btc_candles_48]
    pepe_open_24 = [candle['open'] for candle in pepe_candles_24]

    match necessary_strategy:
        case 'all':
            output_text_1 = strategy_1(btc_volumes_48)
            output_text_2 = strategy_2(btc_volumes_48)
            output_text_3 = strategy_3(btc_volumes_48)
            output_text_4 = strategy_4(btc_volumes_48)
            output_text_5 = strategy_5(btc_volumes_48)
            output_text_6 = strategy_6(pepe_open_24)
            output_text_7 = strategy_7(btc_candles_48)
            output = (f"Time: <b>{request_time}</b>\n\n"
                      f"{output_text_1}\n"
                      f"{output_text_2}\n"
                      f"{output_text_3}\n"
                      f"{output_text_4}\n"
                      f"{output_text_5} \n"
                      f"{output_text_6} \n"
                      f"{output_text_7} \n"
                      )
        case '1234':
            output_text_1 = strategy_1(btc_volumes_48)
            output_text_2 = strategy_2(btc_volumes_48)
            output_text_3 = strategy_3(btc_volumes_48)
            output_text_4 = strategy_4(btc_volumes_48)
            output = (f"Time: <b>{request_time}</b>\n\n"
                      f"{output_text_1}\n"
                      f"{output_text_2}\n"
                      f"{output_text_3}\n"
                      f"{output_text_4}\n"
                      )
        case '567':
            output_text_5 = strategy_5(btc_volumes_48)
            output_text_6 = strategy_6(pepe_open_24)
            output_text_7 = strategy_7(btc_candles_48)
            output = (f"Time: <b>{request_time}</b>\n\n"
                      f"{output_text_5} \n"
                      f"{output_text_6} \n"
                      f"{output_text_7} \n"
                      )
        case 'strategy_1':
            output = strategy_1(btc_volumes_48)
        case 'strategy_2':
            output = strategy_2(btc_volumes_48)
        case 'strategy_3':
            output = strategy_3(btc_volumes_48)
        case 'strategy_4':
            output = strategy_4(btc_volumes_48)
        case 'strategy_5':
            output = strategy_5(btc_volumes_48)
        case 'strategy_6':
            output = strategy_6(pepe_open_24)
        case 'strategy_7':
            output = strategy_7(btc_candles_48)
        case _:
            raise ValueError("No such strategy")

    return output


def start_strategies() -> None:
    while True:
        while datetime.now().minute != 39:
            time.sleep(60)
        while datetime.now().second < 45:
            time.sleep(1)

        alert_message = strategies(necessary_strategy=ALERT_COMPONENTS)
        for user in users_id:
            bot.send_message(chat_id=user, text=alert_message, parse_mode='HTML')

        time.sleep(15)
