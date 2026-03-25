from db.connection import get_connection


def create_student(name, email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO students (name, email) VALUES (%s, %s)",
        (name, email)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Student created")


def get_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    for s in students:
        print(s)

    cur.close()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()

    cur.close()
    conn.close()
    print("🗑️ Student deleted")
