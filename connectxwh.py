import psycopg2
conn = psycopg2.connect(
    host="147.8.125.118",
    port="5432",
    database="stpretrain_grid",
    user="mob",
    password="hkumob"
)

cur = conn.cursor()
cur.execute("SELECT COUNT (*) FROM nyc.nyc_taxi_2014")


conn.commit()

count = cur.fetchone()[0]
print(count)
