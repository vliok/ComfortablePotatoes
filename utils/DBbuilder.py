import sqlite3

db=sqlite3.connect('../data/Comfy.db')
c=db.cursor()

def makeDB():
    q="CREATE TABLE users( \'first\' text, \'last\' text, \'username\' text, \'password\' text, \'points\' integer, \'players\' integer, \'group\' integer )"
    c.execute(q)

makeDB()
db.commit()
db.close()

