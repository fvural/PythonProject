import sqlite3
con=sqlite3.connect('database.db')
con.row_factory=sqlite3.Row
vt=con.cursor()