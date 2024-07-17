from constants import bot, user_id, developer_id, NOTUSDT, IOUSDT, STRATEGY_CURRENT
from services import create_csv
from datetime import datetime
import time
import statistics
import csv


def strategy_1(currency: str, only_output_text=False):
    '''
    std_dev_20_volume = standard deviation for 20 hours
    mean_24_volume = mean volume for 24 hours
    Strategy logic is for business purpose
    if 2 * std_dev_20_vol + mean_24_vol < current volume --> Alert
    '''
    csv_name = 'csv/strategy_1.csv'
    create_csv(currency=currency, start_time_mode='day', filename=csv_name)

    with open(csv_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader)  # skip headers = [Time, Open, High, Close, Volume]
        std_dev_data = []
        mean_data = []

        for row in csv_reader:
            volume_value = float(row[5])
            std_dev_data.append(volume_value)
            mean_data.append(volume_value)

        std_dev_data = std_dev_data[4:]

        std_dev_20_volume = statistics.stdev(std_dev_data)
        mean_24_volume = statistics.mean(mean_data)
        current_volume = volume_value
        formula = 2 * std_dev_20_volume + mean_24_volume
        result: bool = formula < current_volume

        output_text = (f"<b>NOT_1</b>[3.1%] result: <b>{result}</b>\n"
                       f"std_dev_20_volume: <b>{round(std_dev_20_volume, 5)}</b>\n"
                       f"mean_24_volume: <b>{round(mean_24_volume, 5)}</b>\n"
                       f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                       f"2 * std_dev_20 + mean_24: <b>{round(formula, 5)}</b>\n"
                       )
        if only_output_text:
            return output_text

        return result, std_dev_20_volume, mean_24_volume, current_volume, output_text


def strategy_2(currency: str, only_output_text=False):
    # std_dev_40_volume = standard deviation for 40 hours
    # mean_40_volume = mean volume for 40 hours
    # Strategy logic is for business purpose
    # (std_dev_20_volume + mean_24_volume) / current volume > 3.75 --> Alert

    csv_name = 'csv/strategy_2.csv'
    create_csv(currency=currency, start_time_mode='two_days', filename=csv_name)

    with open(csv_name, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        # skip headers and first 8 rows, since we need only 40 rows from 48 rows
        # headers = [Time, Open, Close, Low, High, Volume]
        for i in range(9):
            next(csv_reader)

        volumes_data_40 = []

        for row in csv_reader:
            volumes_data_40.append(float(row[5]))

        std_dev_40_volume = statistics.stdev(volumes_data_40)
        mean_40_volume = statistics.mean(volumes_data_40)
        current_volume = volumes_data_40[-1]

        formula = (std_dev_40_volume + mean_40_volume) / current_volume
        result: bool = formula > 3.75

        output_text = (f"<b>NOT_2</b>[3.7%] result: <b>{result}</b>\n"
                       f"std_dev_40_volume: <b>{round(std_dev_40_volume, 5)}</b>\n"
                       f"mean_40_volume: <b>{round(mean_40_volume, 5)}</b>\n"
                       f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                       f"(std_dev_40 + mean_40) / volume: <b>{round(formula, 5)}</b>\n"
                       )
        if only_output_text:
            return output_text

        return result, std_dev_40_volume, mean_40_volume, current_volume, output_text


def strategy_3(currency: str, only_output_text=False):
    # Expands strategy_1
    _, std_dev_20_volume, mean_24_volume, current_volume, _ = strategy_1(currency=currency)
    formula = 2.35 * std_dev_20_volume + mean_24_volume
    result: bool = formula < current_volume

    output_text = (f"<b>IO_3</b>[1.65%] result: <b>{result}</b>\n"
                   f"std_dev_20_volume: <b>{round(std_dev_20_volume, 5)}</b>\n"
                   f"mean_24_volume: <b>{round(mean_24_volume, 5)}</b>\n"
                   f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                   f"2.35 * std_dev_20 + mean_24: <b>{round(formula, 5)}</b>\n"
                   )
    if only_output_text:
        return output_text
    return result, std_dev_20_volume, mean_24_volume, current_volume, output_text


def strategy_4(currency: str, only_output_text=False):
    # Expands strategy_2
    _, std_dev_40_volume, mean_40_volume, current_volume, _ = strategy_2(currency=currency)
    formula = (std_dev_40_volume + mean_40_volume) / current_volume
    result = formula > 3.6

    output_text = (f"<b>IO_4</b>[4.4%] result: <b>{result}</b>\n"
                   f"std_dev_40_volume: <b>{round(std_dev_40_volume, 5)}</b>\n"
                   f"mean_40_volume: <b>{round(mean_40_volume, 5)}</b>\n"
                   f"current_volume: <b>{round(current_volume, 5)}</b>\n"
                   f"(std_dev_40 + mean_40) / volume: <b>{round(formula, 5)}</b>\n"
                   )
    if only_output_text:
        return output_text

    return result, std_dev_40_volume, mean_40_volume, current_volume, output_text


def start_strategies() -> None:
    while True:
        while datetime.now().minute != 20:
            time.sleep(60)
        while datetime.now().second < 45:
            time.sleep(1)

        output_text_1 = strategy_1(currency=STRATEGY_CURRENT, only_output_text=True)

        output_text_2 = strategy_2(currency=STRATEGY_CURRENT, only_output_text=True)

        output_text_3 = strategy_3(currency=STRATEGY_CURRENT, only_output_text=True)

        output_text_4 = strategy_4(currency=STRATEGY_CURRENT, only_output_text=True)

        time_now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        output = (f"Time: <b>{time_now}</b>\n\n"
                  f"{output_text_1}\n"
                  f"{output_text_2}\n"
                  f"{output_text_3}\n"
                  f"{output_text_4}\n"
                  )

        bot.send_message(chat_id=developer_id, text=output, parse_mode='HTML')
        bot.send_message(chat_id=user_id, text=output, parse_mode='HTML')

        time.sleep(15)
