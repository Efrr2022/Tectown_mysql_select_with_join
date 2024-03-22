import json
import mysql.connector 
def lambda_handler(event, context):
    body = "Python program for checking and creating a table"
    statusCode = 200

    # Credentials to connect to the database
    mydb= mysql.connector.connect(
     host="tectown-backend-q1-2024.c1s0muoa0qc4.us-east-1.rds.amazonaws.com",
     user="admin",
     password="Tectown1!",
     database="efrem_tectown"
     )

    mycursor = mydb.cursor()
    stmt = "SELECT * From users"
    mycursor.execute(stmt)
    result = mycursor.fetchall()
    if result:
      table_data = []
      for row in result:
        table_data.append({
          'name': row[1],
          'email': row[2],
          'address': row[3],
          'phone_no': row[4]
        })
      json_data = json.dumps(table_data)
    else:
      # Sql statement to create table users
      sql = " create table users ( \
          userId int auto_increment primary key, \
          full_name varchar(200) NOT NULL, \
          email varchar(200) NOT NULL UNIQUE, \
          Address  varchar(1000), \
          phone_no varchar(200) UNIQUE ) \
          "
      # Execute sql
      mycursor.execute(sql)
      # Print confirmation 
      print("New table User created")

    #Close Session. 
    mycursor.close()
    mydb.close()

  
   
    return {
      "statusCode": statusCode,
	   "body": table_data,
	   "headers": {
	     "Content-Type": "application/json"
		   }
   	}
