import psycopg2

con = psycopg2.connect(
    host = 'localhost',
    database = 'snake',
    user = 'snake_user',
    password = 'Kaktusbro228'
)

cursor = con.cursor()