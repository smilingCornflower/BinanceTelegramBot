from constants import client
from datetime import datetime
import csv


START_DAY_READABLE = '1 day ago UTC'
START_MONTH_READABLE = '1 month ago UTC'
START_TWO_DAYS_READABLE = '2 days ago UTC'
START_YEAR_READABLE = '1 year ago UTC'
HOUR = client.KLINE_INTERVAL_1HOUR
MIN30 = client.KLINE_INTERVAL_30MINUTE


def get_candles(currency: str, start_time_mode: str, interval_mode='hour') -> list[dict]:
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
        case _:
            raise ValueError(f'Incorrect value for start_time_mode: {start_time_mode}')

    match interval_mode:
        case 'hour':
            interval = HOUR
        case 'min30':
            interval = MIN30
        case _:
            raise ValueError(f'Incorrect value for interval_mode: {interval_mode}')


    # interval=HOUR, because it's necessary for business
    klines = client.get_historical_klines(
        symbol=currency,
        interval=interval,
        start_str=start_time
    )
    for kline in klines:
        kline_data = {
            # ohlcv - open, high, low, close, volume
            # don't touch this !
            'datetime': datetime.fromtimestamp(kline[0] / 1000).strftime('%d.%m.%Y %H:%M'),
            'open': float(kline[1]),
            'close': float(kline[4]),
            'low': float(kline[3]),
            'high': float(kline[2]),
            'volume': float(kline[5])
        }
        output.append(kline_data)
    return output


def create_csv(currency: str, start_time_mode: str, filename: str, interval_mode='hour'):
    with open(filename, 'w', encoding='utf-8', newline='') as data_file:
        writer = csv.writer(data_file, delimiter=';')
        writer.writerow(['Time', 'Open Price', 'Close Price', 'Low Price', 'High Price', 'Volume'])

        candles = get_candles(currency=currency, start_time_mode=start_time_mode, interval_mode=interval_mode)

        for candle in candles:
            writer.writerow(candle.values())

    return filename
