from constants import bot, currency
from strategies import strategy_1, strategy_2
from services import create_csv
import os


def get_csv_pattern(message, start_time_mode: str):
    csv_filename = f"csv/{currency}_{start_time_mode}.csv"
    create_csv(currency, start_time_mode, filename=csv_filename)
    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        bot.send_document(message.chat.id, csv_file)
    os.remove(csv_filename)


@bot.message_handler(commands=['get_csv_day'])
def get_csv_day(message):
    get_csv_pattern(message, start_time_mode='day')

@bot.message_handler(commands=['get_csv_month'])
def get_csv_month(message):
    get_csv_pattern(message, start_time_mode='month')

@bot.message_handler(commands=['get_csv_year'])
def get_csv_year(message):
    get_csv_pattern(message, start_time_mode='year')

@bot.message_handler(commands=['get_strategy_1'])
def get_strategy_1(message):
    output_text = strategy_1(currency=currency, only_output_text=True)
    bot.send_message(message.chat.id, text=output_text, parse_mode='HTML')

@bot.message_handler(commands=['get_strategy_2'])
def get_strategy_2(message):
    output_text = strategy_2(currency=currency, only_output_text=True)
    bot.send_message(message.chat.id, text=output_text, parse_mode='HTML')
