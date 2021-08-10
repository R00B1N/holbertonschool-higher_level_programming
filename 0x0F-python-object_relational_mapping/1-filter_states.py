#!/usr/bin/python3
"""
accepts 3 arguments (mysql username, password and database name)
and lists all states from that database whose names start with N
"""
import sys
import MySQLdb


def main(argv):
    """connects to a given mysql database and lists filtered states from it"""
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'\
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    pass
    cur.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 4:
        main(sys.argv)
