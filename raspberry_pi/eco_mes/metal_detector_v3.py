#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:42:43 2020

@author: pi
"""

import time
import datetime
import RPi.GPIO as GPIO
import pandas as pd

GPIOpin = -1

# Initial Pin
def initialInductive(pin):
    global GPIOpin
    GPIOpin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOpin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    print("Finished Initiation")
    print(GPIOpin)
    
    
# Detect Metal
def detectMetal(ini_time, times, state_, tp_list, ct_list):
    if (GPIOpin != -1):
        state = GPIO.input(GPIOpin)
        if state != state_ and state == 1:
            times+=1
            print("Metal Detected {} times.".format(times))
            ini_time_ = datetime.datetime.now()
            ct = ini_time_ - ini_time
            tp_list.append(ini_time_)
            ct_list.append(ct.total_seconds())
            print("CT: {} s.".format(ct.total_seconds())) 
            ini_time = ini_time_
        state_ = state
            
    else:
        print("Please initial input pin")
    return ini_time, times, state_,tp_list, ct_list

def save_csv(times, tp_list, ct_list):
    if times % 10 == 0 and times != 0:
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
    
    while True:
        ini_time, times, state_,tp_list, ct_list = detectMetal(ini_time,times,state_,tp_list, ct_list)
        tp_list, ct_list, times = save_csv(times, tp_list, ct_list)
        time.sleep(0.01)