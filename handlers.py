from constants import bot, currency, developer_id, NOTUSDT, IOUSDT, STRATEGY_CURRENT
from strategies import strategy_1, strategy_2, strategy_3, strategy_4
from services import create_csv
import os


def get_csv_pattern(message, start_time_mode: str, currency=currency, interval_mode='hour'):
    csv_filename = f"csv/{currency}_{start_time_mode}.csv"
    create_csv(currency, start_time_mode, filename=csv_filename, interval_mode=interval_mode)
    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        bot.send_document(message.chat.id, csv_file)

# currency handlers ----------------------------------------------------------
@bot.message_handler(commands=['get_currency'])
def get_currency(message):
    bot.send_message(message.chat.id, text=f"Current currency is <b>{currency}</b>", parse_mode='HTML')

@bot.message_handler(commands=['get_csv_day_hour'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day')

@bot.message_handler(commands=['get_csv_month_hour'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month')

@bot.message_handler(commands=['get_csv_year_hour'])
def get_csv_year(message):
    get_csv_pattern(message, start_time_mode='year')

@bot.message_handler(commands=['get_csv_day_min30'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day', interval_mode='min30')

@bot.message_handler(commands=['get_csv_month_min30'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month', interval_mode='min30')

@bot.message_handler(commands=['get_csv_year_min30'])
def get_csv_year(message):
    get_csv_pattern(message, start_time_mode='year', interval_mode='min30')

@bot.message_handler(commands=['get_strategy_1'])
def get_strategy_1(message):
    output_text = strategy_1(currency=STRATEGY_CURRENT, only_output_text=True)
    bot.send_message(message.chat.id, text=output_text, parse_mode='HTML')

@bot.message_handler(commands=['get_strategy_2'])
def get_strategy_2(message):
    output_text = strategy_2(currency=STRATEGY_CURRENT, only_output_text=True)
    bot.send_message(message.chat.id, text=output_text, parse_mode='HTML')

@bot.message_handler(commands=['get_strategy_3'])
def get_strategy_2(message):
    output_text = strategy_3(currency=STRATEGY_CURRENT, only_output_text=True)
    bot.send_message(message.chat.id, text=output_text, parse_mode='HTML')

@bot.message_handler(commands=['get_strategy_4'])
def get_strategy_2(message):
    output_text = strategy_4(currency=STRATEGY_CURRENT, only_output_text=True)
    bot.send_message(message.chat.id, text=output_text, parse_mode='HTML')

# NOTUSDT handlers -----------------------------------------------------------
@bot.message_handler(commands=['notusdt_csv_day_hour'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day', currency=NOTUSDT)

@bot.message_handler(commands=['notusdt_csv_month_hour'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month', currency=NOTUSDT)

@bot.message_handler(commands=['notusdt_csv_day_min30'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day', currency=NOTUSDT, interval_mode='min30')

@bot.message_handler(commands=['notusdt_csv_month_min30'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month', currency=NOTUSDT, interval_mode='min30')

# IOUSDT handlers ------------------------------------------------------------
@bot.message_handler(commands=['iousdt_csv_day_hour'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day', currency=IOUSDT)


@bot.message_handler(commands=['iousdt_csv_month_hour'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month', currency=IOUSDT)


@bot.message_handler(commands=['iousdt_csv_day_min30'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day', currency=IOUSDT, interval_mode='min30')


@bot.message_handler(commands=['iousdt_csv_month_min30'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month', currency=IOUSDT, interval_mode='min30')
