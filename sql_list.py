import sqlite3
con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row
c = con.cursor()
########################################################################################################################
########################################################################################################################
def list(table_name):
    column_2 = 'adi'
    column_3 = 'soyadi'

    ok=c.execute('SELECT * FROM {tn} '.\
            format(coi1=column_2, coi2=column_3, tn=table_name, cn=column_2))

    x = 1
    for veri in ok.fetchall():
        print(x,veri['no'],veri['adi'],veri['soyadi'],veri['date'])
        x = x + 1
########################################################################################################################


########################################################################################################################
########################################################################################################################
