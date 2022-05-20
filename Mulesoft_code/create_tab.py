import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="movies_db") #connect to mysql
cur = mydb.cursor()

squery = """create table movies(
            movie_name varchar(35) primary key,
            actor varchar(35),
            actress varchar(35),
            year integer(4),
            director varchar(35)
            )""" # query to create table    
cur.execute(squery) # execute query