import sqlite3
conn = sqlite3.connect('MovieRecommendationSystem.db')
cursor = conn.cursor()

user_input = input("Please enter: Y if you would like a personalised recommendation, N if you would like a random recommendation and E to exit the program.").upper()
if user_input == "Y":
    #blah blah
    cursor.execute
elif user_input == "N":
    #blah blah
elif user_input == "E":
    print("Thank you for using my recommendation system. Goodbye!")
else:
print("Invalid input. Please enter Y, N, or E.")