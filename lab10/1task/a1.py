import psycopg2

config = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook',
    port = '5432',
    user = 'bookuser',
    password = 'passw0rd'
)

current = config.cursor()

postgres_insert_query = ''' insert into phonebook (username, number) values (%s,%s) '''
a = input('enter your name: ')
b = input('enter your number: ')
current.execute(postgres_insert_query, (a,b))
config.commit()

current.close()
config.close()