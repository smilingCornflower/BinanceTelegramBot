from constants import bot, currency, NOTUSDT, IOUSDT
from strategies import start_strategies
import threading
from handlers import *
import time

start_strategies_thread = threading.Thread(target=start_strategies)
start_strategies_thread.start()

while True:
    try:
        bot.infinity_polling(timeout=50, long_polling_timeout=50)
    except Exception as e:
        print(f"Error occurred: {e}")
        time.sleep(5)




