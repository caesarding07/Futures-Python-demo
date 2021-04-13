'''
Author: CaesarDing
Date: 2021-04-13 13:18:08
LastEditors: CaesarDing
LastEditTime: 2021-04-13 14:03:39
FilePath: \Futures-Python-demo\HuobiSpot\websocket_demo.py
Description: 
'''
# %%
from websocket import create_connection
import gzip  # 压缩和解压缩文件 WebSocket 行情接口返回的所有数据都进行了 GZIP 压缩，需要 client 在收到数据之后解压。
import time

# print(__name__) 魔法函数 在当前页面运行就是__main__ ,其他页面显示包名
if __name__ == '__main__':
    # print(__name__)
    while(1):
        try:
            print('尝试')
            ws = create_connection("wss://api.huobi.pro/ws")
        except Exception as e:
            print('An exception occurred:' % e)
            time.sleep(5)

    print('hh')
    # 订阅KLine 数据
    tradeStr_kline = """
    {"sub": "market.BTC_CQ.kline.1min",  "id": "id1"}
    """

    # 请求 KLine 数据
    tradeStr_klinereq = """
    {"req": "market.BTC_CQ.kline.1min", "id": "id4"}
    """

    ws.send(tradeStr_kline)
    trade_id = ''
    while(1):
        print(__name__)
        compressData = ws.recv()
        result = gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            # 心跳消息
            # 当用户的Websocket客户端连接到火币Websocket服务器后，服务器会定期（当前设为5秒）向其发送ping消息并包含一整数值。
            # 当用户的Websocket客户端接收到此心跳消息后，应返回pong消息并包含同一整数值。
            ts = result[8:21]
            pong = '{"pong":'+ts+'}'
            ws.send(pong)
            ws.send(tradeStr_klinereq)
        else:
            try:
                if trade_id == result['data']['id']:
                    print('重复的id')
                    break
                else:
                    trade_id = result['data']['id']
            except Exception as e:
                print('An exception occurred' % e)

            print(result)

# %%
