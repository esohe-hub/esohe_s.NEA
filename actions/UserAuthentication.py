from user_ratings import rate_movie_ui
from core.user_manager import UserManager
user_manager = UserManager()


def show_welcome():
    print("WELCOME TO THE MOVIE RECOMMENDATION SYSTEM!")
    print("Here, you can find movies based on your preferences, and easily find your next favourite film!")


def get_valid_username():
    while True:
        username = input("Enter your username: ").strip()

        if len(username) == 0:
            print("Username cannot be empty.")
        elif not username.isalnum():
            print("Username can only contain letters and numbers.")
        else:
            return username

def get_valid_password():
    while True:
        password = input("Enter your password: ").strip()

        if len(password) == 0:
            print("Password cannot be empty.")
        elif not any(i.isdigit() for i in password):
            print("Your password must contain at least one number.")
        elif not any(i.isupper() for i in password):
            print("Your password must contain at least one uppercase letter.")
        else:
            return password


def login():
    username = get_valid_username()
    password = get_valid_password()

    user = user_manager.get_user_by_username(username)

    if user and user[2] == password:
        print(f"Welcome back, {username}!")
        return user[0]
    else:
        print("Invalid username or password. Please try again.")
        return None



def signup():
    username = get_valid_username()
    password = get_valid_password()

    success = user_manager.create_user(username, password)

    if success:
        print(f"Account created successfully! Welcome, {username}!")
        return user_manager.get_user_by_username(username)[0]
    else:
        print("That username is already taken. Please choose another.")
        return None

user_id = None
while True:
    auth_choice = input("Type 'login' to log in or 'signup' to sign up: ").strip().lower()

    if auth_choice == 'login':
        user_id = login()
        if user_id:
            break
    elif auth_choice == "signup":
        user_id = signup()
        if user_id:
            break
    else:
        print("Invalid option. Please type 'login' or 'signup'.")

    if user_id is None:
        print("Something went wrong.")
        exit()

while True:
    print("\n1. Rate a movie")
    print("2. Exit")

    menu_choice = input("Choose an option: ").strip()

    if menu_choice == "1":
        rate_movie_ui(user_id)

    elif menu_choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose an option.")

