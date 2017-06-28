# tablo ismi ile birlikte sütun isimleride verilsin bir şekilde
# verilen tablo ismi database de yoksa hata mesajı versin...
# asc-dsc opsiyonu

import sqlite3
con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row
c = con.cursor()

c.execute("Delete from test where adi='3965'")
########################################################################################################################
########################################################################################################################

con.commit()
con.close()