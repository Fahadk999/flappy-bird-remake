import sqlite3
import os
from abs_path import absPath


DBNAME = os.path.join(os.getcwd(), "leaderboard.db")
def initDB ():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()
    path = absPath("src/database/schema.sql")
    with open(path, "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()

def saveScore (score):
    name = "YOU"
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    sql = "INSERT INTO leaderboard (name, score) VALUES (?, ?);"
    cursor.execute(sql, (name, score))
    conn.commit()
    conn.close()

def getScores(limit=5):
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    sql = """
    SELECT name, score
    FROM leaderboard
    ORDER BY score DESC
    LIMIT ?
    """ 
    cursor.execute(sql, (limit,))
    topScores = cursor.fetchall()
    conn.close()
    
    return topScores
