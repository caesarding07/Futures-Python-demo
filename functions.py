'''
Author: CaesarDing
Date: 2021-04-12 15:54:13
LastEditors: CaesarDing
LastEditTime: 2021-04-12 16:21:34
FilePath: \Futures-Python-demo\functions.py
Description: 
'''
import requests

def get_all_currencys(): #获取所有币种
    url = 'https://api.huobi.pro/v1/common/currencys'
    response = requests.request('GET', url , verify=False)
    if response.status_code == 200:
        print("ok")
        print(response.content)
        return response
    else:
        print('fail')
        return 0
def get_currrent_btc_u_price():
    url = 'https://www.huobi.co/-/x/pro/market/overview5?r=ny2seo'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price_usdt = data['data'][2]['close']
        return price_usdt
    else:
        return 0

def main():
    #get_currrent_btc_u_price()
    get_all_currencys()

main()


