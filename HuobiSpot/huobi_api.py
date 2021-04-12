'''
Author: CaesarDing
Date: 2021-04-12 16:31:15
LastEditors: CaesarDing
LastEditTime: 2021-04-12 21:07:22
FilePath: \Futures-Python-demo\HuobiSpot\huobi_api.py
Description: 
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:48:13 2018

@author: zhaobo
"""


# %%  market data api ===============

from HuobiSpotService import HuobiSpot
from pprint import pprint  # 分行打印，适合结构化数据

#from talib import RSI

# input huobi spot url
URL = 'http://api.huobi.pro'

# input your access_key and secret_key below:
ACCESS_KEY = 'f3b4b94e-xa2b53ggfc-ae9c10c0-05d85'
SECRET_KEY = 'a3eef828-d9a746b7-384d13f6-41e30'
Spot = HuobiSpot(URL, ACCESS_KEY, SECRET_KEY)
UID = '6767065'
""" 
print(U' 获取用户账户信息 ')
pprint(Spot.get_account_info()) """
""" print(U' 获取用户账户余额')
pprint(Spot.get_account_balance(UID)) """
""" print(U' 获取用户账户流水')
pprint(Spot.get_account_history(UID)) """
print(' 获取k线数据')
pprint(Spot.get_history_kline())

# %%
