from config import conn, cursor

def checkNumber(num):
    if num.find('8707') == 0 and len(num) == 11:
        return num
    elif num.find('8702') == 0 and len(num) == 11:
        return num
    elif num.find('8777') == 0 and len(num) == 11:
        return num
    elif num.find('8778') == 0 and len(num) == 11:
        return num
    elif num.find('8776') == 0 and len(num) == 11:
        return num
    elif num.find('8747') == 0 and len(num) == 11:
        return num
    elif num.find('8708') == 0 and len(num) == 11:
        return num
    elif num.find('8705') == 0 and len(num) == 11:
        return num
    print('Sorry, you made a mistake in phone number, please write it again:')
    num = input()
    return checkNumber(num)

print("What's your query?")
query = str(input())

if query == 'insert':
    print('How many people you want to add?')
    n = int(input())
    print('Please, enter name and phonenumber:')
    for i in range(0,n):
        first_name = str(input())
        num = str(input())
        num = checkNumber(num)
        cursor.execute('call insert(%s,%s);', (first_name,num))

if query == 'update':
    print('How many people you want to update?')
    n = int(input())
    print('Please, enter name and phonenumber:')
    for i in range(0,n):
        first_name = str(input())
        num = str(input())
        cursor.execute('call update(%s, %s);',(first_name,num))

if query == 'delete':
    print('Please, enter the name or number you want to delete:')
    data = input()
    cursor.execute('call delete(%s);', [data])
       
if query == 'pagination':
    print("Type your limit and offset")
    limit = int(input())
    offset = int(input())
    pag = '''
        select * from phone offset %s limit %s;
    '''
    cursor.execute(pag ,(limit,offset))
    print(cursor.fetchall())

if query == 'query':
    pat = str(input())
    cursor.execute('select querying(%s)', ['%'+pat+'%'])
    print(cursor.fetchall())

cursor.close()
conn.commit()
conn.close()