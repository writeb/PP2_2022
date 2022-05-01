import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook',
    port = '5432',
    user = 'bookuser',
    password = 'passw0rd'
)

current = config.cursor()
#a = input('Enter username : ')
b = input('Enter number : ')
#sql = f'select * from phonebook where username = \'{a}\'' 
sql = f'select * from phonebook where number = \'{b}\''
current.execute(sql)

phonebook = current.fetchall()

print(phonebook)

current.close()
config.close()