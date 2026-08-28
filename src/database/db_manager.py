import sqlite3

DBNAME = "leaderboard.db"
def initDB ():
    conn = sqlite3.connect(DBNAME)
    cursor = conn.cursor()

    with open("src/database/schema.sql", "r") as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close

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
