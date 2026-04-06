from DatabaseConnection import get_connection
conn = get_connection()
cursor = conn.cursor()
import random

def personalised_recommendation(user_id):
    user_input = input("Please enter: Y if you would like a personalised recommendation, N if you would like a random recommendation and E to exit the program.").upper()
    '''if user_input == "Y":
    
    elif user_input == "N":
        #what happens if they say no
    elif user_input == "E":
        print("Thank you for using my recommendation system. Goodbye!")
    else:
    print("Invalid input. Please enter Y, N, or E.")'''


def menu():
   while True:
      print("\n Movie Recommendation System ")
      print("1 - Personalised Recommendation")
      print("2 - Random Movie")
      print("3 - Exit")

      choice = input("Select an option: ")

      '''if choice == "1":
         user_id = input("Enter your User ID: ")
            if user_id.isdigit():
                personalised_recommendation(user_id)
            else:
                print("Invalid User ID. Please enter a numeric value.") 
        elif choice == "2":
            random_movie()
        elif choice == "3":
            print("Thank you for using the Movie Recommendation System. Goodbye!")
            break'''