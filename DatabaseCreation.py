import sqlite3
def create_database(db_name = 'database.sqlite'): #create actual database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # create movies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            MovieId INTEGER PRIMARY KEY AUTOINCREMENT,
            Movie_Title TEXT NOT NULL UNIQUE,
            Release_Year INTEGER,
            Classification TEXT,
            Duration REAL,
            Genre TEXT,
            IMDB_Rating REAL,
            Concise_Summary TEXT,
            Metascore REAL,
            Director TEXT,
            Actor1 TEXT,
            Actor2 TEXT,
            Actor3 TEXT,
            Actor4 TEXT,
            NumOfVotes INTEGER
        )
    ''')
    
    #create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            UserId INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            preferred_genres TEXT
        
        )
    ''')  

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS user_ratings(
                   RatingId INTEGER PRIMARY KEY AUTOINCREMENT,
                   UserId INTEGER NOT NULL,
                   Rating REAL NOT NULL,
                   Movie_Title TEXT,
                   Genre TEXT,
                   UNIQUE(UserId, Movie_Title),
                   FOREIGN KEY (UserId) REFERENCES user_ratings(UserId)
                   )
                     ''')
    
    conn.commit()
    conn.close()

create_database()
