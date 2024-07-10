from constants import client
from datetime import datetime
import csv


START_DAY_READABLE = '1 day ago UTC'
START_MONTH_READABLE = '1 month ago UTC'
START_TWO_DAYS_READABLE = '2 days ago UTC'
START_YEAR_READABLE = '1 year ago UTC'
HOUR = client.KLINE_INTERVAL_1HOUR

def get_candles(currency: str, start_time_mode: str):
    output = []

    match start_time_mode:
        case 'day':
            start_time = START_DAY_READABLE
        case 'two_days':
            start_time = START_TWO_DAYS_READABLE
        case 'month':
            start_time = START_MONTH_READABLE
        case 'year':
            start_time = START_YEAR_READABLE

    # interval=HOUR, because it's necessary for business
    klines = client.get_historical_klines(
        symbol=currency,
        interval=HOUR,
        start_str=start_time
    )
    for kline in klines:
        kline_data = {
            'datetime': datetime.fromtimestamp(kline[0] / 1000).strftime('%d.%m.%Y %H:%M'),
            'open': float(kline[1]),
            'high': float(kline[2]),
            'low': float(kline[3]),
            'close': float(kline[4]),
            'volume': float(kline[5])
        }
        output.append(kline_data)
    return output


def create_csv(currency: str, start_time_mode: str, filename: str):
    with open(filename, 'w', encoding='utf-8', newline='') as data_file:
        writer = csv.writer(data_file, delimiter=';')
        writer.writerow(['Time', 'Open Price', 'Close Price', 'Low Price', 'High Price', 'Volume'])

        candles = get_candles(currency=currency, start_time_mode=start_time_mode)

        for candle in candles:
            writer.writerow(candle.values())

    return filename