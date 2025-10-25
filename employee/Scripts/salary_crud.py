from backend import get_connection

def get_salaries():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM salaries;")
    data = cursor.fetchall()
    conn.close()
    return data
