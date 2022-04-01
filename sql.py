# This gist contains a direct connection to a local PostgreSQL database
# called "suppliers" where the
# This code is adapted from the tutorial hosted below:
# http://www.postgresqltutorial.com/postgresql-python/connect/

import psycopg2
import time
# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

def select(): # Or:
    conn = psycopg2.connect(host="94.26.237.102", port=5432, database="habrdb", user="habrpguser",
                            password="pgpwd4habr")

    i = 0
    # Create a cursor object
    cur = conn.cursor()

    #try:
        #cur.execute("CREATE TABLE public.data (id bigserial primary key,data varchar(20));")
    #except:
        #print("table already exists")
    # A sample query of all data from the "vendors" table in the "suppliers" database
    #while i < 1:
        #cur.execute("""SELECT * FROM ddata WHERE list='1'""")
        #query_results = cur.fetchall()
        #print(query_results)
        #i = i + 1
        #time.sleep(0.01)

    cur.execute("SELECT data FROM public.data ORDER BY id DESC LIMIT 5")
    query_results = cur.fetchall()
    print(query_results)
    return query_results

    # Close the cursor and connection to so the server can allocate
    # bandwidth to other requests
    conn.commit()
    cur.close()
    conn.close()
    print("test end")

def insert(v1):
    conn = psycopg2.connect(host="94.26.237.102", port=5432, database="habrdb", user="habrpguser",
                            password="pgpwd4habr")

    i = 0
    # Create a cursor object
    cur = conn.cursor()
    x = "INSERT INTO data (data) VALUES ('"+v1+"')"
    cur.execute(x)
    print(x)
    print(v1)
    conn.commit()
    cur.close()
    conn.close()