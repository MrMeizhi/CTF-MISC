#!/usr/bin/env python
#-*- coding:utf-8 -*-

import scapy.all as scapy
import scapy_http.http
import urllib
import re
import base64
def main():
    packet = scapy.rdpcap('1.pcap')
    n = 0
    for p in packet:
        n = n + 1
        a = p.show(dump=True)
        if '###[ HTTP Request ]###' in a:
            getLoad = re.compile("load      = \'(.*)\'").findall(a)
            if getLoad != []:
                load = getLoad[0]
                load = urllib.unquote(load)
                getParameter = re.compile('z0=(.*)&z1=(.*)&z2=(.*)').findall(load)
                if getParameter != []:
                    print n
                    b = list(getParameter[0])
                    print base64.b64decode(b[0])
                    print base64.b64decode(b[1])
                    print base64.b64decode(b[2])
                    print '='*78
            
            
    print n
if __name__ == '__main__':
    main()
