from backend import get_connection

def fetch_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.employee_id, e.first_name, e.last_name, e.email, e.phone_number,
        e.gender, d.department_name, e.job_title, e.hire_date, e.status
        FROM employees e
        LEFT JOIN departments d ON e.department_id = d.department_id;
    """)
    data = cursor.fetchall()
    conn.close()
    return data

def add_employee(first_name, last_name, email, phone, gender, department_id, job_title, hire_date, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees
        (first_name, last_name, email, phone_number, gender, department_id, job_title, hire_date, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (first_name, last_name, email, phone, gender, department_id, job_title, hire_date, status))
    conn.commit()
    conn.close()
