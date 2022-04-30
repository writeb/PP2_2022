import psycopg2
config = psycopg2.connect(
    host = 'localhost',
    database = 'phonebook',
    port = '5432',
    user = 'bookuser',
    password = 'passw0rd'
)

current = config.cursor()
current.execute(
    '''
    create table phonebook(
        username varchar(20),
        number varchar(12)
    );
    '''
)
config.commit()

current.close()
config.close()