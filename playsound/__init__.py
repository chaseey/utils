#coding=utf-8
__author__ = 'kidd'


# for client
import redis


SERVER_IP = '192.168.1.222'
DB_NUM = 0
CHANNEL_NAME = 'news'

r = redis.Redis(host=SERVER_IP, db=DB_NUM)

class Client(object):
    def __init__(self):
        self.r = redis.Redis(host=SERVER_IP, db=DB_NUM)
        self.rps = r.pubsub()
        self.rps.subscribe(CHANNEL_NAME)

    def run(self):
        for d in self.rps.listen():
            if d['type'] == 'message':
                self.process_data(d['data'])

    def process_data(self, data):
        print data
        pass



class Server(object):
    def __init__(self):
        self.r = redis.Redis(host=SERVER_IP, db=DB_NUM)
        self.channel = CHANNEL_NAME

    def publish(self, msg):
        self.r.publish(self.channel, msg)


client = Client()
client.run()




