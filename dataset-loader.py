import csv
with open('data/movie-dataset.csv', mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    data = list(csv_reader)

    # print(data[:5])

database = open('data/database.sqlite', 'w')
database.close()
print("The database file was created.")
