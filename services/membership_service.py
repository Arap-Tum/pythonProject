from db.connection import get_connection


def add_student_to_club(student_id, club_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO memberships (student_id, club_id) VALUES (%s, %s)",
        (student_id, club_id)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Student added to club")


def view_club_members(club_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT students.id, students.name
    FROM students
    JOIN memberships ON students.id = memberships.student_id
    WHERE memberships.club_id = %s
    """, (club_id,))

    members = cur.fetchall()

    for m in members:
        print(m)

    cur.close()
    conn.close()
