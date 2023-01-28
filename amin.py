import os
import subprocess
from flask import Flask
import mysql.connector





def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str
 
mydb = mysql.connector.connect(
  host="localhost",
  #user="ansible",
  #password="password",
  user="bob",
  password="12345",
  database="mysql"
)

mycursor = mydb.cursor()

#mycursor.execute("SHOW TABLES")
mycursor.execute("show variables like 'innodb%';")
mystr = ""
for x in mycursor:
  mystr = mystr +convertTuple(x) + "\n" 
#print(mystr)




app = Flask(__name__)
@app.route("/")
def hello():
    return mystr
if __name__ == "__main__":
    app.run(host='0.0.0.0')

