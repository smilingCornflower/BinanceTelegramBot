# BinanceTelegramBot
Welcome to the Binance Data Parser Telegram Bot!
This bot is designed to help you analyze and monitor cryptocurrency data directly from Binance. Here's what it can do:
## Features:
- *CSV File Generation:* Automatically creates CSV files containing OHLCV 
- (Open, High, Low, Close, Volume) data for your selected cryptocurrencies and each line contains information about the time


- *Alerts:* Receive real-time alerts when specific cryptocurrencies meet certain conditions you define.

## Setup:
- Clone this repository.
```python
git clone https://github.com/smilingCornflower/BinanceTelegramBot/
```

- Install dependencies form requirements.txt
```python
pip install -r requirements.txt
```

- Obtain your own bot token from **@BotFather** in telegram


- Create secret.py in the root of a project and add these data
```python
your_id = 'your_id'

# API KEY and SECRET KEY are the keys to your binance account.
# You can leave these fields empty, then you will be anonymous and you will still be able to make requests to the binance api.
# Keys are needed for monetary transactions with the account
# just leave it empty

API_KEY = ''
SECRET_KEY = ''


bot_token = 'your telegram bot token'
```
- in constants.py change user_id to your own telegram id, for example. You can get your id from this bot **@userinfobot**.  
Also you can select interesting currency 
```python
user_id = secret.your_id
currency = 'BTCUSDT'
```

- Finally you can run python bot.py to start the bot.


## Commands:

Following commands you should write to your bot, not in terminal.
___ 
Sends you an excel file with detailed information about the selected currency

```python
/get_csv_day
/get_csv_month
/get_csv_year
```

## How to setup alerts?
Alerts are mostly individual and everyone puts their own logic that they want.
In the file strategies.py there is an example of two alerts.


**strategy_1** is a function that outputs a report based on a formula (the formula is from a book of investment).   
**start_strategy_1** It works in a separate thread, 
```python
start_strategy_1_thread = threading.Thread(target=start_strategy_1, args=[currency])
start_strategy_1_thread.start()
```
this is necessary so that the bot can process other actions in parallel. 
It's waiting for the time to be exactly HH:59:59 and at this moment it calls the strategy_1 function 
and receives the final line from it, then sends this message to user_id
```python
bot.send_message(chat_id=user_id, text=output_text)
```
You can also add your own logic so that the bot, 
for example, analyzes every 10 minutes and if the price drops by 0.5%, then send a notification
