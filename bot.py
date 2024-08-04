from constants import bot, currency, NOTUSDT, IOUSDT
from strategies import start_strategies
import threading
from handlers import *
import time

start_strategies_thread = threading.Thread(target=start_strategies)
start_strategies_thread.start()

bot.infinity_polling()
