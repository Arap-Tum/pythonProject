from db.connection import get_connection


def create_club(name, description):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clubs (name, description) VALUES (%s, %s)",
        (name, description)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Club created")
