import psycopg2
import csv

# connect to PostgreSQL
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")

#cursor
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users_using_copy(
        id serial PRIMARY KEY,
        email text,
        name text,
        phone text,
        postal_code text
    )
""")

with open(r'C:\Users\Rafi Muhammad\Documents\Bootcamp_DataEngineer\Project3\source\users_w_postal_code.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'users_using_copy', sep = ',', columns=('email', 'name', 'phone', 'postal_code'))

conn.commit()