#!/usr/bin/python3
"""
accepts 4 arguments (mysql username, password, database name and a given state)
and lists all cities from that database that belong to the given state
+ injection free!
"""
import sys
import MySQLdb


def main(argv):
    """
    connects to a given mysql database and lists all 'cities' of a given state
    """
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
            ON cities.state_id = states.id\
            WHERE states.name = %s", (argv[4], ))
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i != 0:
            print(", ", end="")
        i += 1
        print(row[0], end="")
    print()
    cur.close()
    conn.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)
