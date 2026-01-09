import sqlite3
conn = sqlite3.connect('MovieRecommendationSystem.db')
cursor = conn.cursor()


print("WELCOME TO THE MOVIE RECOMMENDATION SYSTEM!")
print("Here, you can find movies based on your preferences, and easily find your next favourite film!")
print("Please log in or sign up to continue.")

def login():
    while True:
        username = input("Enter your username: ").strip()

        if len(username) == 0:
            print("Username cannot be empty.")
        elif not username.isalnum():
            print("Username can only contain letters and numbers.")
        else:
            break
    while True:
        password = input("Enter your password: ").strip()

        if len(password) == 0:
            print("Password cannot be empty.")
        elif not any(i.isdigit() for i in password):
            print("Your password must contain at least one number.")
        elif not any(i.isupper() for i in password):
            print("Your password must contain at least one uppercase letter.")
        else:
            break
  
    cursor.execute(
        "SELECT * FROM Users WHERE username=? AND password=?",
            (username, password)
    )
    user = cursor.fetchone()
     
    if user:
        print(f"Welcome back, {username} !")
        return user[0]
    else:
        print("Invalid username or password. Please try again.")
        return None

'''above we execute our command to find the rows where the user and password match, then fetch
    the first row because we know it's gonna be unique. if a matching row is found, the user exists and so print our
    welcome back message'''

''' try and except are used around database operations that could violate constraints
like inserting a duplicate username. This allows the program to handle errors gracefully
without it crashing.'''




def signup():
    while True:
        username = input("Enter your username: ").strip()

        if len(username) == 0:
            print("Username cannot be empty.")
        elif not username.isalnum():
            print("Username can only contain letters and numbers.")
        else:
            break
    while True:
        password = input("Enter your password: ").strip()

        if len(password) == 0:
            print("Password cannot be empty.")
        elif not any(i.isdigit() for i in password):
            print("Your password must contain at least one number.")
        elif not any(i.isupper() for i in password):
            print("Your password must contain at least one uppercase letter.")
        else:
            break
    try:
        cursor.execute(
            "INSERT INTO Users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        print(f"Account created successfully! Welcome, {username}!")

    except sqlite3.IntegrityError:
        print("That username is already taken. Please choose another.")

#try attempts to insert a new user. if the username already exists, SQLite raises an IntegrityError.
#except catches this and stops my program from crashing, and the user is asked to choose a different username


while True:
    loginOrSignup = input("Type 'login' to log in or 'signup' to sign up: ").strip().lower()
    if loginOrSignup == 'login':
        user_id = login()
        if user_id:
            break
conn.close()

'''The login function returns the user's ID if authentication is successful. This value is checked
before exiting the login loop, to ensure the program will only continue when a valid user has logged in.'''

#Storing passwords as plain text is insecure and passwords are visible to potential hackers. Therefore, I will implement password hashing for improved 
#security within my system.
