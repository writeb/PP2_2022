import psycopg2
import csv
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port = '5432',
    user = 'postgres',
    password = 'Kaktusbro228'
)

current = config.cursor()

postgres_insert_query = '''insert into phonebook (username, number) values (%s,%s)'''
file = open('phonebook.csv')
csvreader = csv.reader(file)
for row in csvreader:
    current.execute(postgres_insert_query, row)

config.commit()

current.close()
config.close()