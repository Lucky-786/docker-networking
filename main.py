import psycopg2
from decouple import config

conn = psycopg2.connect(dbname=config("DB_NAME"), user=config("DB_USER"), password=config("DB_PASS"), host=config("DB_HOST"), port=config("Port"))

cur = conn.cursor()

cur.execute("SELECT * from public.user;")
rows = cur.fetchall()
for row in rows:
    print("FIRST NAME =", row[0])
    print("LAST NAME =", row[1])
    print("AGE =", row[2])
    print("PHONE =", row[3])
    print("ADDRESS =", row[4], "\n")

cur.close()

conn.close()