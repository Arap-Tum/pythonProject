import mysql.connector

print("Hello welcome to School Managment system ")
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jamkei5242",
    database="school_system"
)

cursor = conn.cursor()

print("Database connected successfully")

# CreATE A TABLE CCALLED STUDENTS
cursor.execute("""
 CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

conn.commit()

print("Tbale has created successfully")


cursor.execute("SELECT * FROM  school_system")
for row in cursor:
    print(row)
