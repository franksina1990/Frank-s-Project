#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 01:30:32 2020

@author: pi
"""

import pymssql

conn = pymssql.connect(server = '192.168.3.4:1433',#'DESKTOP-TDRDBT0\SQLEXPRESS',
                       database='ct_test',
                       user = 'test',
                       password = '123123123',
                       charset='utf8')
cursor = conn.cursor()

if cursor:
    print(1)
    
#conn = pymssql.connect(host='DESKTOP-TDRDBT0\SQLEXPRESS',
 #                      user = 'test',
  #                     password = '123123123',
   #                    charset='utf8')

#cursor=conn.cursor() #get cursor
print('connect to db success')

cursor.execute('SELECT * FROM test1')
rows = cursor.fetchall()
print(rows)


cursor.executemany('INSERT INTO test1 VALUES (%d,%s,%d)',[(2,35,"JS")])


cursor.execute('SELECT * FROM test1')
rows = cursor.fetchall()
print(rows)
 
'''
cursor.execute("""
CREATE TABLE test3(
    tid INT NOT NULL,
    age int,
    school VARCHAR(150),
    PRIMARY KEY(tid))
""")
conn.commit()

print('success')'''

