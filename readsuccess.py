import mysql.connector


def checkdatabase(link):
    getdata = link
    print(getdata)
    domain_list = []
    mydb = mysql.connector.connect(
        host="192.168.123.13",
        user="fabrian",
        password="P@ssw0rd",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql_cmd = mycursor.execute("SELECT * FROM Phishtest;")
    record = mycursor.fetchall()
    
    for i in record :
        
        url_raw = i[1].split("/")
        url = url_raw[2]
        url = url.split(".")

        if 'www' in url:
            url = url[1]+"."+url[2]         
        else : url = url[0]+"."+url[1]

        domain_list.append(url)


    getdata = getdata.split("/")
    getdata = getdata[2].split(".")

    if 'www' in getdata:
            get_url = getdata[1]+"."+getdata[2]

    else : get_url = getdata[0]+"."+getdata[1]

    if get_url in domain_list :
            return "yes"
    else : return "no"

def insertdata(link):

    mydb = mysql.connector.connect(
        host="192.168.123.13",
        user="fabrian",
        password="P@ssw0rd",
        database="mydatabase"
        )

    mycursor = mydb.cursor()

    var = ""    

    try:
        mycursor.execute("INSERT INTO Phishtest VALUES (%s,%s,%s,%s,%s,%s,%s,%s)","0",link,var,var,var,var,var,var)
    except Exception as e:
        print(e)
    
    mydb.commit()
    mycursor.close()
    return "oke"