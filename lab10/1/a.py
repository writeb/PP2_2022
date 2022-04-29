import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port = '5432',
    user = 'postgres',
    password = 'Kaktusbro228'
)

current = config.cursor()
current.execute(
    '''
    create table phonebook(
        username varchar(20),
        number varchar(12)
    )
    '''
)
config.commit()

current.close()
config.close()