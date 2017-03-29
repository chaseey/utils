# coding:utf-8
__author__ = 'kidd'


import requests
import json
import time
import os

'''
    update stock price for manloong.com
'''

STOCK_DIC = {
    'HSI': {
        'url': 'http://www.aastocks.com/tc/resources/datafeed/getstockindex.ashx?type=1',
        'interval': 60*3,
        'rule': 1,
    },
    'DJI': {
        'url': 'http://www.aastocks.com/tc/resources/datafeed/getstockindex.ashx?type=3',
        'interval': 60,
        'rule': 1,
    },
    'EBML': {
        'url': 'http://www.aastocks.com/tc/resources/datafeed/getusstockhistory.ashx?',
        'interval': 60*5,
        'rule': 2,
    }
}


'''Cache data obj'''
class CacheData(object):
    def __init__(self):
        self.file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'get_stock_cache.txt'
        )

    def get(self):
        try:
            with open(self.file_path, 'r') as f:
                string = f.read()
                return json.loads(string)
        except:
            return {}


    def save(self, jsonData):
        with open(self.file_path, 'w') as f:
            f.write(json.dumps(jsonData, indent=2))


'''Stock Class'''
class Stock(object):
    def __init__(self, name, url, interval=60, rule=1):
        self.name = name
        self.url = '{}&timestamp={}'.format(url, time.time())
        self.interval = interval
        self.rule = rule

    def get_data(self):
        s = requests.session()
        if self.rule == 1:
            data = json.loads(s.get(self.url).text)
            for i in data:
                if i['symbol'] == self.name:
                    i['lastUpdateByML'] = time.time()
                    return i

        elif self.rule == 2:    # from EBML
            s.cookies['USStock'] = 'BrowserHistory=EBML'
            data = json.loads(s.get(self.url).text)
            for i in data:
                if i['symwoex'] == self.name:
                    i['lastUpdateByML'] = time.time()
                    return i


def run_get_stock():
    cache = CacheData()
    cache_data = cache.get()
    updated = False

    for name, dic in STOCK_DIC.items():
        stock_obj = Stock(name, dic['url'], dic['interval'], dic['rule'])
        if name in cache_data:
            interval = time.time() - cache_data[name]['lastUpdateByML']
            if interval < stock_obj.interval:
                continue
        cache_data[name] = stock_obj.get_data()
        updated = True

    if updated:
        cache.save(cache_data)


if __name__ == '__main__':
    run_get_stock()
