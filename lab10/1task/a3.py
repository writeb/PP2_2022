import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook',
    port = '5432',
    user = 'bookuser',
    password = 'passw0rd'
)

current = config.cursor()

postgres_select_query = '''select * from phonebook where username = %s'''
a = input('Enter name that you want to change: ')
current.execute(postgres_select_query,(a,))
postgres_update_query = '''update phonebook set number = %s where username = %s'''
b = input('Enter number that you want to change: ')
current.execute(postgres_update_query, (b, a))

config.commit()

current.close()
config.close()