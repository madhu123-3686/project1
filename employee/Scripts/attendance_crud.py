from backend import get_connection

def get_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance;")
    data = cursor.fetchall()
    conn.close()
    return data
