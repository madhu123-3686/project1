from backend import get_connection

def get_departments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT department_id, department_name, manager_id, location FROM departments;")
    data = cursor.fetchall()
    conn.close()
    return data
