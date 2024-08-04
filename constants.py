from binance.client import Client
import secret
import telebot

client = Client(secret.API_KEY, secret.SECRET_KEY)
bot = telebot.TeleBot(secret.bot_token)

daniyar_id = secret.daniyar_id
developer_id = secret.nauryzbek_id
unknown_user_id = secret.unkown_user_id

users_id = [
    developer_id
    # daniyar_id,
    # unknown_user_id,
]

NOTUSDT = 'NOTUSDT'
IOUSDT = 'IOUSDT'
PEPEUSDT = 'PEPEUSDT'
BTCUSDT = 'BTCUSDT'

ALERT_COMPONENTS = 'all'
# all
# 1234
# 567


currency = 'BTCUSDT'
