import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook',
    port = '5432',
    user = 'bookuser',
    password = 'passw0rd'
)

current = config.cursor()

postgres_delete_query = '''delete from phonebook where username = %s'''
a = input('Enter name that you want to delete: ')
current.execute(postgres_delete_query, (a,))

config.commit()

current.close()
config.close()