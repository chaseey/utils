#coding=utf-8
__author__ = 'kidd'

'''监控行情'''

import requests
import time
from pyquery import PyQuery as pq
import winsound
import win32api
from agents import USER_AGENTS
import random
import os
import datetime
import threading

MUSIC_PATH = r'C:\Windows\Media\Landscape\Windows Exclamation.wav'

WATCH_STOCKS = ['LLG', 'LLS']

URL = 'http://www.92621888.com/m/gen_quote/getdata_9262_utf8_3-tt.php?show=&_='


def alert_message(title,msg):
    threads = []
    threads.append(
        threading.Thread(target=winsound.PlaySound, args=(MUSIC_PATH, winsound.SND_FILENAME))
    )
    # winsound.PlaySound(MUSIC_PATH, winsound.SND_FILENAME)
    # win32api.MessageBox(0, msg, title)
    threads.append(
        threading.Thread(target=win32api.MessageBox, args=(0, msg, title))
    )
    for t in threads:
        t.start()




def get_url():
    return URL + str(time.time())

def _process_price(priceStr):
    '''
    :param priceStr: string like  1244.0/4.5  左卖 右买
    :return: a list like (int 1244.5, int 1244.0)  转为 左买， 右卖
    '''
    sell, buyPart = [i for i in priceStr.split('/')]
    sn = len(buyPart)
    buy = sell[0:-sn] + buyPart
    return (float(buy), float(sell))


def get_price():
    url = get_url()
    header = {'User-Agent' : random.choice(USER_AGENTS)}
    r = requests.get(url, headers=header)
    html = pq(r.content)
    prices = {}
    for tr in html('table tr[bgcolor]'):
        for stock in WATCH_STOCKS:
            if stock in html(tr)('td[rowspan]:first').text():
                priceStr = html(tr)('td[rowspan]:last').text()  # 1244.0/4.5  左卖 右买
                prices[stock] = _process_price(priceStr)
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), prices
    return prices


def compare(stock, type, price):
    '''
    type : in ['buy', 'sell']
    '''
    stock = stock.upper()
    type = type.upper()
    price = float(price)
    print 'start watching {}'.format(stock)
    while True:
        prices = get_price()
        if stock not in prices:
            alert_message(u'出错了', u'找不到报价:{}'.format(stock))
            return False
        buy, sell = prices[stock]

        if type in ['B', 'BUY']:
            if buy >= price:
                msg = u'时间:{}\n行情报价:{}/{}\n监控买入:{}'.format(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),buy, sell,price)
                alert_message(u'报价命中', msg)
                return True
        elif type in ['S', 'SELL']:
            if sell <= price:
                msg = u'时间:{}\n行情报价:{}/{}\n监控卖出:{}\n'.format(
                    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),buy, sell, price)
                alert_message(u'报价命中', msg)
                return True
        else:
            print(u'ERROR: type 出错')
            return False
        time.sleep(3)





if __name__ == '__main__':
    from optparse import OptionParser
    p = OptionParser(usage=u'行情监控')
    p.add_option('-s', '--stock', help=u'监控代码: LLS, LLG',dest='stock')
    p.add_option('-t', '--type', help=u'监控行情方向: buy, sell, test(测试)', dest='type')
    p.add_option('-p', '--price', help=u'监控的报价', dest='price')

    options, args = p.parse_args()

    stock = options.stock
    type = options.type
    price = options.price

    if type== 'test':
        alert_message(u'', 'testing')
        exit()

    try:
        result = compare(stock, type, price)
    except Exception as e:
        print e
        p.print_help()
        exit()
    if not result:
        p.print_help()





