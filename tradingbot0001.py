from dotenv import load_dotenv
from lumibot.brokers import Alpaca
from lumibot.traders import Trader
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader

import os
load_dotenv()
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
base_url = os.getenv("BASE_URL")