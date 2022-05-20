import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="movies_db")
cur = mydb.cursor()


select_query1 = """select * from movies""" # query to select from table
cur.execute(select_query1) 
result1 = cur.fetchall() # fetch all rows
print(result1)

actor="Mammootty"
select_query2 = "select * from movies where actor='"+actor+"'" # query to select from table with parameter
cur.execute(select_query2)
result2=cur.fetchall() 
print(result2)