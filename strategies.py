from constants import bot, user_id
from services import create_csv

from datetime import datetime
import time
import statistics
import csv


def strategy_1(currency: str, only_output_text=False):
    # std_dev_20_volume = standard deviation for 20 hours
    # mean_24_volume = mean volume for 24 hours
    # Strategy logic is for business purpose
    # if 2 * std_dev_20_vol + mean_24_vol < current volume --> Alert

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

        result: bool = 2 * std_dev_20_volume + mean_24_volume < current_volume

        output_text = f"strategy_1 result: <b>{result}</b>\n" \
                      f"std_dev_20_volume: <b>{round(std_dev_20_volume, 5)}</b>\n" \
                      f"mean_24_volume: <b>{round(mean_24_volume, 5)}</b>\n" \
                      f"current_volume: <b>{round(current_volume, 5)}</b>\n" \

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
        # headers = [Time, Open, High, Close, Volume]
        for i in range(9):
            next(csv_reader)

        volumes_data_40 = []

        for row in csv_reader:
            volumes_data_40.append(float(row[5]))

        std_dev_40_volume = statistics.stdev(volumes_data_40)
        mean_40_volume = statistics.mean(volumes_data_40)
        current_volume = volumes_data_40[-1]

        result: bool = (std_dev_40_volume + mean_40_volume) / current_volume > 3.75

        output_text = f"strategy_2 result: <b>{result}</b>\n" \
                      f"std_dev_40_volume: <b>{round(std_dev_40_volume, 5)}</b>\n" \
                      f"mean_40_volume: <b>{round(mean_40_volume, 5)}</b>\n" \
                      f"current_volume: <b>{round(current_volume, 5)}</b>\n" \

        if only_output_text:
            print(volumes_data_40)

            return output_text

        return result, std_dev_40_volume, mean_40_volume, current_volume, output_text


def start_strategy_1(currency: str) -> None:
    while True:
        while datetime.now().minute != 59:
            time.sleep(60)
        while datetime.now().second < 58:
            time.sleep(1)

        output_text = strategy_1(currency=currency, only_output_text=True)

        bot.send_message(chat_id=user_id, text=output_text)


def start_strategy_2(currency: str) -> None:
    while True:
        while datetime.now().minute != 59:
            time.sleep(60)
        while datetime.now().second < 58:
            time.sleep(1)

        output_text = strategy_2(currency=currency, only_output_text=True)

        bot.send_message(chat_id=user_id, text=output_text)
