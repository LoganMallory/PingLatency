#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 20:36:25 2018

@author: Logan Mallory
"""
import subprocess
from datetime import datetime
import pandas as pd
from time import sleep
import random

def pingAddress(url = 'www.google.com'):
    host = url

    ping = subprocess.Popen(
            ["ping", "-c", "32", host], #use "-n" if not on a Mac
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
            )
    beginTime = str(datetime.now())    #get current time
    out, error = ping.communicate()    #get ping latency data
    endTime = str(datetime.now())      #get current time again

    return(out,beginTime,endTime)

def getLatency(data, location):
    pings = pd.DataFrame()              #initialize empty dataframe
    vero = str(data[0])                 #get ping latency data as a string    
    pingList = vero.split('\\n')        #split the string
    pingList = pingList[1:33]           #shorten the list to only relevant data
    for i, line in enumerate(pingList):
        pingList[i] = line.split('=') + [data[1]] + [data[2]] + [location]  
        #split string to get latency time, then add begining and end times and location
        
    for part in pingList:
        pings = pings.append([part])    #append the lists in pingList to the pings dataframe as rows
    return(pings)
    
   
def runPingTest(pingTimes, location):
    pingData = pingAddress()                    #get raw ping data
    single = getLatency(pingData, location)     #get dataframe of the ping latency data with time and location
    pingTimes = pd.concat([pingTimes, single])  #add the 'single' dataframe (row-wise) to the larger pingTimes dataframe
    return(pingTimes)



def getPingData(pingDF, location):
    while True:                                       #YOU MUST EXIT THIS LOOP MANUALLY
        pingDF = runPingTest(pingDF, location)        #get a dataframe of all ping data so far
        pingDF.to_csv('PingDataFrame.csv')            #export this file to the computer, overwriting the previous export
        sleeptime = random.randrange(1,600)             
        print('Sleeping for', sleeptime, 'seconds.....')#sleep for some random time between 1 and 600 seconds (10min)
        sleep(sleeptime)                                #you can exit the program while it is sleeping and it will not harm the data


def main():
    test = pingAddress()                                #initialize some raw ping data
    initPingDF = getLatency(test, 'Lobby of Hotel')     #initialize a ping latency dataframe
    getPingData(initPingDF, 'Lobby of Hotel')           #run more ping tests and export as csv's after every test

main()

