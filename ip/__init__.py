#coding=utf-8


def ip2num(ipString):
    if ipString is None:
        raise Exception("Invalid IP")
    try:
       octets = [octet.strip() for octet in ipString.split('.')]
    except Exception,e:
        raise e

    num = (int(octets[0])<<24) + (int(octets[1])<<16) + (int(octets[2])<<8) + int(octets[3])
    return num


def num2ip(numericIp):
    if numericIp is None or type(numericIp) not in  (int, long):
        raise Exception("Invalid numeric IP. Must be an integer")
    return str(numericIp >> 24) + '.' + str((numericIp >> 16) & 255) + '.' +\
           str((numericIp >> 8) & 255) + '.' + str(numericIp & 255)



