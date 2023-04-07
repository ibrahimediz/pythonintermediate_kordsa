# import sqlite3 as sql
# sql.connect(database)
# from sqlite3 import connect
# connect(database)
import sqlite3 as sql
import pathlib as pt
db = sql.connect(pt.Path(__file__).parent / "chinook.db")
cur = db.cursor()
cur.execute("""
SELECT * FROM artists LIMIT 5
""")
for item in cur.fetchall():
    print(item)

isim = "Neşet Ertaş"
sayi = 0
for i in isim:
    sayi+=ord(i)
print(sayi)