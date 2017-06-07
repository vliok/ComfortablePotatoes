import sqlite3
from statsScraper import getPrevSeasonHeaders



def makeDB():
    db=sqlite3.connect('../data/users.db')
    c=db.cursor()
    q="CREATE TABLE users( \'userID\' integer, \'username\' text, \'password\' text, \'points\' integer, \'players\' text, \'group\' integer )"
    c.execute(q)
    db.commit()
    db.close()


#makeDB()

def prevSeasonCommand():
    q = "CREATE TABLE prevSeason("
    headers = getPrevSeasonHeaders()
    q += "\'PID\' integer, \'name\' text, \'img\' text," 
    for x in headers:
        q += "\'" + x + "\' text,"
    return q.rstrip(',')+  ")"

def makeDB2():
    db=sqlite3.connect('../data/athletes.db')
    c=db.cursor()
    c.execute(prevSeasonCommand())
    db.commit()
    db.close()

#makeDB2()

def makeDB3():
    db=sqlite3.connect('../data/stats.db')
    c=db.cursor()
    q="CREATE TABLE days(\'Athlete\' text, \'Day\' integer, \'MP\' text, \'FG\' text, \'FGA\' text, \'FG%\' text, \'3P\' text, \'3PA\' text, \'3P%\' text, \'FT\' text, \'FTA\' text, \'FT%\' text, \'ORB\' text, \'DRB\' text, \'TRB\' text, \'AST\' text, \'STL\' text, \'BLK\' text, \'TOV\' text, \'PF\' text, \'PTS\' text)"
    c.execute(q)
    db.commit()
    db.close()

makeDB3()
