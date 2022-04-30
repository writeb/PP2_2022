import config

config.cursor.execute(
    '''
    insert into users (id, username) values (1, 'student1');
    insert into user_score (user_name, score) values ('student1', 15);
    '''
)
config.con.commit()