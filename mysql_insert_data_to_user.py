import mysql.connector
# mysql Credentials to connect to the database
mydb= mysql.connector.connect(
    host="tectown-backend-q1-2024.c1s0muoa0qc4.us-east-1.rds.amazonaws.com",
    user="admin",
    password="Tectown1!",
    database="efrem_tectown"
    )
mycursor = mydb.cursor()

# sql statement to insert data to the table users
sql="Insert into users (full_name,email,Address,phone_no) values (%s, %s, %s, %s)"
val= [
  ('Filimon', 'filimon@gmail.com','US', '+21111111'),
  ('Aron', 'aron@gmail.com', 'Uganda', '+22222222' ),
  ('Natnael', 'natnael@gmail.com', 'Uganda', '+33333333'),
  ('Efrem', 'efrem@gmail.com', 'South Sudan', '+44444444')
 ]

# save changes made
mycursor.executemany(sql,val)
mydb.commit()

# print number of records inserted
print(mycursor.rowcount,"row insterted.")

#Close Session. 
mycursor.close()
mydb.close()
