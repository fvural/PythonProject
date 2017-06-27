def cls():
    import os
    os.system('cls')
    return
print("selam")
cls()
print("selam")
cls()
print("selam")
cls()
print("selam")
cls()
print("selam")

import pymysql
'''

bag = pymysql.connect(host='192.168.1.35:3388',
                       user='root',
                       passwd='159753',
                       db='kutuphane',
                       charset='utf8')
'''
import oursql

db_connection = oursql.connect(host='127.0.0.1',user='root',passwd='159753',db='kutuphane')
cur=db_connection.cursor()
cur.execute("SELECT * FROM `test`")
for row in cur.fetchall():
    print row[0]