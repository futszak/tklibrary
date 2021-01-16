#!/usr/local/bin/python3.9
# -*- coding:utf-8 -*-
# Name: TK Library
# Discription: Communication Python Library by Tomasz Kruk
#
# Author:  Tomasz Kruk   futszak@gmail.com
# version 0.3

import socket
import configparser
import mysql.connector

configini = configparser.ConfigParser()
configini.read('config.ini')

try:
    UDP_PORT=configini['logsend']['port']
except:
    UDP_PORT=514

def logsend(x):
    """Sending UDP datagram to remote machine

    Args:
        logsend ([string]): Datagram string
    """
    if not configini['logsend']['address']:
        return()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(x.encode(), (configini['logsend']['address'], UDP_PORT))

def msqlconn():
    """Creating MySQL handle
    """
    mydb = mysql.connector.connect(
        host=configini['database']['host'],
        user=configini['database']['user'],
        passwd=configini['database']['password'],
        database=configini['database']['database']
    )
    return(mydb)

def mysqlquery(mysqlquery):
    """Geting data from mysql database

    Args:
        mysqlquery ([string]): Executing mysql query
    """
    mydb = msqlconn()
    mycursor = mydb.cursor()
    mycursor.execute(mysqlquery)
    myresult = mycursor.fetchall()
    return(myresult)

def mysqlupdate(mysqlquery):
    """Making change in mysql database

    Args:
        mysqlquery ([string]): [Mysql command with arguments]
    """
    mydb = msqlconn()
    mycursor = mydb.cursor()
    try:
        mycursor.execute(mysqlquery)
    except:
        return(False)
    mydb.commit()
    return(mycursor.rowcount, "record(s) affected")
