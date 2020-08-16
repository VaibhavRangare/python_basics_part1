import psycopg2

conn = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = "password",
    host = "localhost",
    port = "5432"
)
'''
conn = conn = psycopg2.connect("dbname=postgres user=postgres password=password host=127.0.0.1 port=5432")
print("conn", conn)
'''

cur = conn.cursor()
cur.execute("SELECT * FROM college.student")
rows = cur.fetchall()
for row in rows:
    print("id:",row[0],", Name:",row[1],", Dept:",row[2])
