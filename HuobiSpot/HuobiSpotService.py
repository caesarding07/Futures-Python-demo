'''
Author: CaesarDing
Date: 2021-04-12 17:35:46
LastEditors: CaesarDing
LastEditTime: 2021-04-12 20:49:44
FilePath: \Futures-Python-demo\HuobiSpot\HuobiSpotService.py
Description: 
'''

from HuobiSpotUtil import http_get_request, api_key_get

class HuobiSpot:
    def __init__(self, url, access_key, secret_key):
        self.__url = url
        self.__access_key = access_key
        self.__secret_key = secret_key

    '''
    ======================
    Market data API
    ======================
    '''
    # 获取k线数据

    def get_history_kline(self):
        params = {
            'symbol': 'btcusdt',
            'period': '1min'
        }
        url = self.__url + '/market/history/kline'
        return http_get_request(url, params)

    # 获取账户信息
    def get_account_info(self):
        """
        Returns:
            id: account_id
        """
        params = {}
        request_path = '/v1/account/accounts'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取账户余额
    def get_account_balance(self, uid):
        """[summary]

        Returns:
            [type]: [description]
        """
        params = {}
        request_path = '/v1/account/accounts/'+uid+'/balance'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)

    # 获取账户流水
    def get_account_history(self, uid):
        params = {'account-id': uid}
        request_path = '/v1/account/history'
        return api_key_get(self.__url, request_path, params, self.__access_key, self.__secret_key)
