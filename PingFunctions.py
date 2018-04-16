#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:36:25 2018

@author: LoganMallory2
"""
import subprocess
from datetime import datetime
import pandas as pd
from time import sleep
import random

def pingAddress(url = 'www.denison.edu'):
    host = url

    ping = subprocess.Popen(
            ["ping", "-c", "32", host],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
            )
    beginTime = str(datetime.now())
    out, error = ping.communicate()
    endTime = str(datetime.now())

    return(out,beginTime,endTime)

def getLatency(data, location):
    pings = pd.DataFrame()
    vero = str(data[0])
    pingList = vero.split('\\n')
    pingList = pingList[1:33]
    for i, line in enumerate(pingList):
        pingList[i] = line.split('=') + [data[1]] + [data[2]] + [location]
        
    for part in pingList:
        pings = pings.append([part])
    return(pings)
    
   
def runPingTest(pingTimes, location):
    pingData = pingAddress()
    single = getLatency(pingData, location)
    pingTimes = pd.concat([pingTimes, single])
    return(pingTimes)

test = pingAddress()
pingDF = getLatency(test, 'Beaver 35')  


while True:
    pingDF = runPingTest(pingDF, 'Burton Morgan 405')
    pingDF.to_csv('PingDataFramePY.csv')
    sleeptime = random.randrange(1,600)
    print('Sleeping for', sleeptime, 'seconds.....')
    sleep(sleeptime)
    #for k in range(1,sleeptime):
        #print(k)
        #sleep(1)






