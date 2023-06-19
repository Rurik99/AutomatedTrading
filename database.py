import sqlite3


def init_db():
    conn = sqlite3.connect('db.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS News(id            INT  PRIMARY KEY,
                                                    date          TEXT DEFAULT CURRENT_TIMESTAMP,
                                                    header        TEXT,
                                                    positive      REAL,
                                                    negative      REAL,
                                                    neutral       REAL);''')
    conn.execute('''CREATE TABLE IF NOT EXISTS Trades(id            INT  PRIMARY KEY,
                                                      date          TEXT DEFAULT CURRENT_TIMESTAMP,
                                                      currency      TEXT,
                                                      leverage      REAL,
                                                      side          TEXT,
                                                      type          TEXT,
                                                      quantity      REAL,
                                                      price         REAL);''')
    conn.commit()
    conn.close()


def insert_news(header, analyze):
    data = (header, analyze['Positive'], analyze['Negative'], analyze['Neutral'])
    conn = sqlite3.connect('db.db')
    conn.execute('''INSERT INTO News(header, positive, negative , neutral) VALUES (?, ?, ?, ?);''', data)
    conn.commit()
    conn.close()
            

def insert_trade(currency, leverage, side, type_, quantity, price):
    data = (currency, leverage, side, type_, quantity , price)
    conn = sqlite3.connect('db.db')
    conn.execute('''INSERT INTO Trades(currency, leverage, side, type, quantity, price) VALUES (?, ?, ?, ?, ?, ?);''', data)
    conn.commit()
    conn.close()



def select_all():
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM News;')
    all_ = cur.fetchall()
    print(all_)
    cur.execute('SELECT * FROM Trades;')
    all_ = cur.fetchall()
    print(all_)
    conn.commit()
    conn.close()


# select_all()
