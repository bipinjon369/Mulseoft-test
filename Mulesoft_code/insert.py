import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",password="Kronos@369",database="movies_db")
cur = mydb.cursor()

squery1 = """insert into movies value("Rappakal","Mammootty","Nayanthara",2005,"Kamal")""" # query to insert into table 
cur.execute(squery1) # execute query
mydb.commit() # commit changes
squery2 = """insert into movies value("Interstellar","Matthew McConaughey","Anne Hathaway",2014,"Christpoher Nolan")""" 
cur.execute(squery2)
mydb.commit()
squery3 = """insert into movies value("Avatar","Sam Worthington","Zoe Saldaña",2009,"James Cameron")""" 
cur.execute(squery3)
mydb.commit()