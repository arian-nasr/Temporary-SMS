import sqlite3
from sqlite3 import Error
dbname = 'temporarysms.db'

def read_messages_from_database(table):
    conn = create_connection(dbname)
    data = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM '+table)
        data = cur.fetchall()
    messages = []
    for item in data:
        messageitem = {}
        messageitem['date'] = item[0]
        messageitem['sender'] = item[1]
        messageitem['body'] = item[2]
        messages.append(messageitem)
    messages.reverse()
    return messages

def read_availability_from_database(table):
    conn = create_connection(dbname)
    data = []
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM '+table)
        data = cur.fetchall()
    numbers = []
    for item in data:
        numberitem = {}
        numberitem['digits'] = item[0]
        numberitem['region'] = item[1]
        numberitem['availability'] = item[2]
        numbers.append(numberitem)
    return numbers

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def write_to_database(table, message_date, message_sender, message_body):
    conn = create_connection(dbname)
    with conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO '+table+' VALUES (?, ?, ?);', (message_date, message_sender, message_body))
        conn.commit()