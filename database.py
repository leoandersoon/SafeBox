import sqlite3
from sqlite3 import Error


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


def create_passwd(conn, passwd):
    """
    Create a new passwd into the passwds table
    :param conn:
    :param passwd:
    :return: passwd id
    """
    sql = ''' INSERT INTO passwd(websites,usernames,passwords)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, passwd)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"/home/leo/Documents/dev-proj/passwd manager/data.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new passwd
        passwd = ('python.org', 'admin', 'vodafone6969');
        passwd_id = create_passwd(conn, passwd)


if __name__ == '__main__':
    main()