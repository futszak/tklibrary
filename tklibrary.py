#!/usr/local/bin/python3.9
# -*- coding:utf-8 -*-
# Name: TK Library
# Discription: Communication Python Library by Tomasz Kruk
#
# Author:  Tomasz Kruk   futszak@gmail.com
# version 0.1

import socket
import configparser

configini = configparser.ConfigParser()
configini.read('config.ini')

try:
    UDP_PORT=configini['logsend']['port']
except:
    UDP_PORT=514


def logsend(x):
    if not configini['logsend']['address']:
        return()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(x.encode(), (configini['logsend']['address'], UDP_PORT))
