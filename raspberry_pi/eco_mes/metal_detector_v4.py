#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:42:43 2020

@author: hz
"""

import time
import datetime
import RPi.GPIO as GPIO
import pandas as pd
import pymssql

GPIOpin = -1


def connect_sqlserver():
    conn = pymssql.connect(server = '192.168.3.4:1433',#'DESKTOP-TDRDBT0\SQLEXPRESS',
                       database='ct_test',
                       user = 'test',
                       password = '123123123',
                       charset='utf8')
    cursor = conn.cursor()
    print('connect to db success')
    return cursor, conn
    

# Initial Pin
def initialInductive(pin):
    global GPIOpin
    GPIOpin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    print("Finished Initiation")
    print(GPIOpin)
    
# Detect Metal
def detectMetal(ini_time, times, state_, tp_list, ct_list, cursor,conn):
    if (GPIOpin != -1):
        state = GPIO.input(GPIOpin)
        if state != state_ and state == 1:
            times+=1
            print("Metal Detected {} times.".format(times))
            ini_time_ = datetime.datetime.now()
            ct = ini_time_ - ini_time
            tp_list.append(ini_time_)
            ct_list.append(ct.total_seconds())
            cursor.executemany('INSERT INTO test4 VALUES (%s,%s)',[(str(ini_time_),ct.total_seconds())])
            conn.commit()
            print("CT: {} s.".format(ct.total_seconds())) 
            ini_time = ini_time_
        state_ = state
            
    else:
        print("Please initial input pin")
    return ini_time, times, state_,tp_list, ct_list


def save_csv(times, tp_list, ct_list, limit = 100):
    if times % limit == 0 and times != 0:
        pd_dict = {"time_stamp": tp_list,
                   "CT": ct_list}
        df = pd.DataFrame.from_dict(pd_dict)
        df.to_csv("/home/pi/Desktop/metal_detector/csv/ct_record_{}.csv".format(datetime.datetime.now()))
        print("ct_record_{} saved.".format(datetime.datetime.now()))
        #print(times)
        tp_list, ct_list = [], []
        times = 0
    return tp_list, ct_list, times

#Run        
if __name__ == '__main__':
    pin = 17
    initialInductive(pin)
    
    ini_time = datetime.datetime.now()
    times = 0
    state_ = 0
    tp_list = []
    ct_list = []
    cursor, conn = connect_sqlserver()
    
    while True:
        ini_time, times, state_,tp_list, ct_list = detectMetal(ini_time,times,state_,tp_list, ct_list, cursor, conn)
        #tp_list, ct_list, times = save_csv(times, tp_list, ct_list)
        time.sleep(0.005)