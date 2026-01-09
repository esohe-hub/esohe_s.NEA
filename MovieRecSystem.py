import sqlite3
def create_database(db_name = 'MovieRecommendationSystem.db'): #create actual database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # create Movies table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies (
            MovieId INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Duration REAL,
            Genre TEXT,
            Director TEXT,
            Actors TEXT,
            Classification TEXT,
            Metascore REAL,
            Release_Year INTEGER,
            ConciseSummary TEXT
        )
    ''')
    
    #create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            UserId INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            preferred_genres TEXT
        
        )
    ''')  

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Ratings(
                   RatingId INTEGER PRIMARY KEY AUTOINCREMENT,
                   UserId INTEGER NOT NULL,
                   Rating REAL NOT NULL,
                   Movie_Title TEXT,
                   Genre TEXT,
                   UNIQUE(UserId, Movie_Title),
                   FOREIGN KEY (UserId) REFERENCES Users(UserId)
                   )
                     ''')
    
    conn.commit()
    conn.close()

create_database()
