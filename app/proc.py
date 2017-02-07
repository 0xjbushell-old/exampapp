#!/usr/bin/python2.7.6

#modules
import sys
import psycopg2

#create query class to connect to postgres DB and randomly select a row from coloumn name
def connect():
    try:
        conn = psycopg2.connect("dbname='exampapp' user='dbadmin' host='localhost' password='PASSWORDGOESHERE'")
    except:
        return str("Can't connect to DB, something broke!")
    cur = conn.cursor()
    cur.execute("""SELECT name FROM quotes
                   ORDER BY RANDOM()
                   LIMIT 1""")
    rows = cur.fetchone()
    return str(rows[0])

#call functions
#get = query()
#connect()
#get.spitout()
