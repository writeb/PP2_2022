import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook2',
    port = '5432',
    user = 'bookuser2',
    password = 'passw0rd2'
)

cursor = conn.cursor()