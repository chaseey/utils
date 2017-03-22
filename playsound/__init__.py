#coding=utf-8
__author__ = 'kidd'


# for client
import redis
import threading
import os

#

SERVER_IP = '192.168.1.222'
DB_NUM = 0
CHANNEL_NAME = 'new*'
SOUND_FILE = r'F:\notify.wav'



class PlaySound(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sound = None
        if os.name == 'nt':
            import winsound
            self.sound = winsound

    def run(self):
        if self.sound:
            self.sound.PlaySound(SOUND_FILE, self.sound.SND_FILENAME)
        # processs msg



class Client(object):
    def __init__(self):
        self.r = redis.Redis(host=SERVER_IP, db=DB_NUM, socket_connect_timeout=3)
        self.rps = self.r.pubsub()
        self.rps.subscribe(CHANNEL_NAME)

    def run(self, func=None):
        for d in self.rps.listen():
            if d['type'] == 'message':
                p = PlaySound()
                p.start()
                p.join()
                print 'receive message:', d['data']
                if func:
                    func(d['data'])


class Server(object):
    def __init__(self):
        self.r = redis.Redis(host=SERVER_IP, db=DB_NUM, socket_connect_timeout=3)
        self.channel = CHANNEL_NAME

    def publish(self, msg):
        self.r.publish(self.channel, msg)



if __name__ == '__main__':
    c = Client()
    def func(msg):
        print 'msg:', msg

    c.run(func)
