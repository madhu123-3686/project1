create database employee_db;
use employee_db;
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(20),
    gender ENUM('Male','Female','Other'),
    department_id INT,
    job_title VARCHAR(100),
    hire_date DATE,
    status ENUM('Active','On Leave','Resigned','Terminated') DEFAULT 'Active'
);
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100),
    manager_id INT,
    location VARCHAR(100)
);
CREATE TABLE salaries (
    salary_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    basic_salary DECIMAL(10,2),
    hra DECIMAL(10,2),
    da DECIMAL(10,2),
    deductions DECIMAL(10,2),
    net_salary DECIMAL(10,2),
    pay_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    check_in TIME,
    check_out TIME,
    total_hours DECIMAL(5,2),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
CREATE TABLE leaves (
    leave_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    leave_type ENUM('Casual','Sick','Paid'),
    start_date DATE,
    end_date DATE,
    reason TEXT,
    status ENUM('Pending','Approved','Rejected') DEFAULT 'Pending',
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
ALTER TABLE employees ADD CONSTRAINT fk_department FOREIGN KEY (department_id) REFERENCES departments(department_id);
ALTER TABLE departments ADD CONSTRAINT fk_manager FOREIGN KEY (manager_id) REFERENCES employees(employee_id);
INSERT INTO departments (department_name, manager_id, location)VALUES ('Human Resources', NULL, 'New York'),('Finance', NULL, 'Chicago'),('IT', NULL, 'San Francisco');
INSERT INTO employees (first_name, last_name, email, phone_number, gender, department_id, job_title, hire_date, status)VALUES('Alice', 'Johnson', 'alice.johnson@example.com', '1234567890', 'Female', 1, 'HR Manager', '2022-03-15', 'Active'),('Bob', 'Smith', 'bob.smith@example.com', '0987654321', 'Male', 3, 'Software Engineer', '2021-06-10', 'Active'),('Charlie', 'Brown', 'charlie.brown@example.com', '5556667777', 'Male', 2, 'Accountant', '2020-03-20', 'Active');
UPDATE departments SET manager_id = 1 WHERE department_id = 1;
UPDATE departments SET manager_id = 3 WHERE department_id = 2;
UPDATE departments SET manager_id = 2 WHERE department_id = 3;
INSERT INTO salaries (employee_id, basic_salary, hra, da, deductions, net_salary, pay_date)VALUES(1, 50000.00, 12000.00, 5000.00, 2000.00, 65000.00, '2025-09-30'),(2, 70000.00, 15000.00, 7000.00, 3000.00, 89000.00, '2025-09-30'),(3, 45000.00, 10000.00, 4000.00, 1500.00, 58500.00, '2025-09-30');
INSERT INTO attendance (employee_id, date, check_in, check_out, total_hours)VALUES(1, '2025-10-20', '09:00:00', '17:00:00', 8.00),(2, '2025-10-20', '09:30:00', '18:00:00', 8.50),(3, '2025-10-20', '08:45:00', '17:15:00', 8.50);
INSERT INTO leaves (employee_id, leave_type, start_date, end_date, reason, status)VALUES(1, 'Paid', '2025-11-10', '2025-11-15', 'Family Vacation', 'Approved'),(2, 'Sick', '2025-10-05', '2025-10-07', 'Medical Leave', 'Pending');
select * from employees;
select * from departments;
select * from salaries;
select * from attendance;
select * from leaves;








