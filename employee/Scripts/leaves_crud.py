from backend import get_connection

def get_leaves():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM leaves;")
    data = cursor.fetchall()
    conn.close()
    return data
