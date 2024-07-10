from constants import bot, currency
from strategies import start_strategy_1, start_strategy_2
import threading
from handlers import *


start_strategy_1_thread = threading.Thread(target=start_strategy_1, args=[currency])
start_strategy_1_thread.start()

start_strategy_2_thread = threading.Thread(target=start_strategy_2, args=[currency])
start_strategy_2_thread.start()

bot.infinity_polling()

