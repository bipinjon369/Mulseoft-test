import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369") #connect to mysql
cur = mydb.cursor() #create cursor
cur.execute("create database movies_db") #create database