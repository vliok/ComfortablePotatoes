import sqlite3

def storeStats(day, stats):
    db=sqlite3.connect("../data/stats.db")
    c=db.cursor()
    for athleteStats in stats:
        q="INSERT INTO days VALUES( \'"+athleteStats[0]+"\', "+str(day)+", \'"+athleteStats[1][athleteStats[0]]["MP"]+"\', \'"+athleteStats[1][athleteStats[0]]["FG"]+"\', \'"+athleteStats[1][athleteStats[0]]["FGA"]+"\', \'"+athleteStats[1][athleteStats[0]]["FG%"]+"\', \'"+athleteStats[1][athleteStats[0]]["3P"]+"\', \'"+athleteStats[1][athleteStats[0]]["3PA"]+"\', \'"+athleteStats[1][athleteStats[0]]["3P%"]+"\', \'"+athleteStats[1][athleteStats[0]]["FT"]+"\', \'"+athleteStats[1][athleteStats[0]]["FTA"]+"\', \'"+athleteStats[1][athleteStats[0]]["FT%"]+"\', \'"+athleteStats[1][athleteStats[0]]["ORB"]+"\', \'"+athleteStats[1][athleteStats[0]]["DRB"]+"\', \'"+athleteStats[1][athleteStats[0]]["TRB"]+"\', \'"+athleteStats[1][athleteStats[0]]["AST"]+"\', \'"+athleteStats[1][athleteStats[0]]["STL"]+"\', \'"+athleteStats[1][athleteStats[0]]["BLK"]+"\', \'"+athleteStats[1][athleteStats[0]]["TOV"]+"\', \'"+athleteStats[1][athleteStats[0]]["PF"]+"\', \'"+athleteStats[1][athleteStats[0]]["PTS"]+"\')"
        c.execute(q)
    db.commit()
    db.close()

#storeStats(1, [[u'Kristaps Porzingis', {u'Kristaps Porzingis': {'FG': u'5', '+/-': u'-21', 'TRB': u'7', 'FT': u'3', 'AST': u'0', 'STL': u'1', 'PTS': u'16', '3P': u'3', 'TOV': u'2', '3P%': u'.600', 'FTA': u'6', 'FT%': u'.500', 'MP': u'32:48', 'BLK': u'2', '3PA': u'5', 'PF': u'5', 'FG%': u'.385', 'DRB': u'3', 'ORB': u'4', 'FGA': u'13'}}], [u'Carmelo Anthony', {u'Carmelo Anthony': {'FG': u'8', '+/-': u'-19', 'TRB': u'5', 'FT': u'2', 'AST': u'3', 'STL': u'1', 'PTS': u'19', '3P': u'1', 'TOV': u'4', '3P%': u'.250', 'FTA': u'2', 'FT%': u'1.000', 'MP': u'30:05', 'BLK': u'0', '3PA': u'4', 'PF': u'5', 'FG%': u'.444', 'DRB': u'4', 'ORB': u'1', 'FGA': u'18'}}]])
