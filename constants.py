from binance.client import Client
import secret
import telebot


client = Client(secret.API_KEY, secret.SECRET_KEY)
bot = telebot.TeleBot(secret.bot_token)

user_id = secret.nauryzbek_id
currency = 'BTCUSDT'


