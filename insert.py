import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="192.168.123.13",
    user="fabrian",
    password="P@ssw0rd",
    database="mydatabase"
)

mycursor = mydb.cursor()


csv_data = csv.reader(open('verified_online.csv'))
header = next(csv_data)

for row in csv_data:
    try:
        print(row)
        mycursor.execute("INSERT INTO Phishtest (phish_id,url,phish_detail_url,submission_time,verified,verification_time,online,target) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",row)
    except Exception as e:
        print(e)
    
mydb.commit()
mycursor.close()

print("done")

