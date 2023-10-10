import psycopg2
import csv

# connect to PostgreSQL
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=postgres")

#cursor
cur = conn.cursor()

# Create Table
cur.execute("""
    CREATE TABLE IF NOT EXISTS latihan_users(
        id serial PRIMARY KEY,
        email text,
        name text,
        phone text,
        postal_code text
    )
""")

with open(r'C:\Users\Rafi Muhammad\Documents\Bootcamp_DataEngineer\Project3\source\users_w_postal_code.csv') as f:
    csv_reader = csv.reader(f, delimiter = ",")
    next(csv_reader)
    for row in csv_reader:
        cur.execute('INSERT INTO latihan_users VALUES (default, %s, %s, %s, %s) ON CONFLICT DO NOTHING', row)

conn.commit()