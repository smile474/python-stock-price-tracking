import yfinance as yf
import time
from datetime import datetime
from discord import send_message
from config import load_config
import sys

if __name__ == '__main__':
    config = load_config()
    if len(config['webhook_url']) == 0:
        print("webhook_url not found")
        sys.exit(1)
    while 1:
        dat = yf.Ticker("MSFT")
        current_time = datetime.now().strftime("%H:%M:%S")
        current_price = float(dat.info.get("currentPrice"))
        print(f'{current_time} current_price = {current_price}')
        if current_price >= float(535.07):
            send_message(current_price, config['webhook_url'])
            time.sleep(60) # send next message after 1 minutes (prevent rate limit exceed)
        time.sleep(1) #refresh stock price data every 1 seconds