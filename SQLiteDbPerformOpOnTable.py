import sqlite3
conn=sqlite3.connect('std1.db')
cursor=conn.cursor()
table="CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255));"
cursor.execute(table)

cursor.execute("INSERT INTO STUDENT VALUES('ishan','7th','A')")
cursor.execute("INSERT INTO STUDENT VALUES('Aahil','8th','B')")
cursor.execute("INSERT INTO STUDENT VALUES('Aliya','5th','C')")
cursor.execute("INSERT INTO STUDENT VALUES('Hassan','9th','D')")

print("Data inserted in the table: ")
data=cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)
    conn.commit()
    conn.close()
    
    
    
                    # OUTPUT ERROR