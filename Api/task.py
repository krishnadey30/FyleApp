import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

def bankDetails(ifsc):
    cur = conn.cursor()
    query = "select * from branches where ifsc = '{}'".format(ifsc)
    cur.execute(query)
    rows = cur.fetchall()
    data = {}
    for row in rows:
        data['ifsc'] = row[0]
        data['branch'] = row[2]
        data['address'] = row[3]
        data['city'] = row[4]
        data['district'] = row[5]
        data['state'] = row[6]
    return data

def branchDetails(bank_name, city, limit = 20, offset = 0):
    cur = conn.cursor()
    query = "select * from bank_branches where bank_name = '{}' \
            and city = '{}' LIMIT {} OFFSET {}".format(bank_name, city, limit, offset)
    cur.execute(query)
    rows = cur.fetchall()
    branches = []
    for row in rows:
        data = {}
        data['ifsc'] = row[0]
        data['branch'] = row[2]
        data['address'] = row[3]
        data['city'] = row[4]
        data['district'] = row[5]
        data['state'] = row[6]
        branches.append(data)
    return branches