from binance.client import Client
import secret
import telebot


client = Client(secret.API_KEY, secret.SECRET_KEY)
bot = telebot.TeleBot(secret.bot_token)

user_id = secret.daniyar_id
developer_id = secret.nauryzbek_id

NOTUSDT = 'NOTUSDT'
IOUSDT = 'IOUSDT'

STRATEGY_CURRENT = 'BTCUSDT'

currency = 'NOTUSDT'



