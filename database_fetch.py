import psycopg2, os
from psycopg2 import pool

class Database_Connection_Error(Exception): 
	def __init__(self, msg): 
		self.msg = msg 

	def __str__(self): 
		return(repr(self.msg))

DATABASE_URL = os.environ['DATABASE_URL']
postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,DATABASE_URL)

def get_bank(ifsc):
    ps_connection  = postgreSQL_pool.getconn()
    if(ps_connection):
        cur = ps_connection.cursor()
        query = "select * from branches where ifsc = '{}'".format(ifsc)
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        postgreSQL_pool.putconn(ps_connection)
        return rows
    else:
        raise Database_Connection_Error("Connection not found")

def get_branch(bank_name, city, limit, offset):
    ps_connection  = postgreSQL_pool.getconn()
    if(ps_connection):
        cur = ps_connection.cursor()
        query = "select * from bank_branches where bank_name = '{}' \
                and city = '{}' LIMIT {} OFFSET {}".format(bank_name, city, limit, offset)
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        postgreSQL_pool.putconn(ps_connection)
        return rows
    else:
        raise Database_Connection_Error("Connection not found")