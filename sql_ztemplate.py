import sqlite3
con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row
c = con.cursor()
########################################################################################################################
########################################################################################################################
def list(table_name):
    res='*'
    ok = c.execute('SELECT {cnn} FROM {tn} '.\
            format(cnn=res, tn=table_name))

    x = 1
    for veri in ok.fetchall():
        date=veri['date']
        date=date[:-7]
        print(x,veri['id'],veri['no'],date,veri['adi'],veri['soyadi'])
        x = x + 1
list("ogrenciler")

########################################################################################################################


########################################################################################################################
########################################################################################################################
con.commit()
con.close()
########################################################################################################################
