import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_dpbo_tp3",
)

dbcursor = mydb.cursor()

sql_insert_person = "INSERT INTO person (name, age, photo, race_id, religion_id) VALUES (%s, %s, %s, %s, %s)"
val_person = ("Abdul", 24, "noPhoto.png", 1, 1,)
dbcursor.execute(sql_insert_person, val_person)
mydb.commit()
print(dbcursor.rowcount, "person inserted.")

dbcursor.execute("SELECT * FROM person")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)

sql_delete_person = "DELETE FROM person WHERE name = %s"
val_delete_person = ("Abdul",)
dbcursor.execute(sql_delete_person, val_delete_person)
mydb.commit()
print(dbcursor.rowcount, "person deleted.")

print("\nSetelah delete :")
dbcursor.execute("SELECT * FROM person")
myresult=dbcursor.fetchall()
for x in myresult:
    print(x)
