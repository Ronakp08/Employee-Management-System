from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for insertion routes
emp_register_bp = Blueprint('emp_register', __name__)

@emp_register_bp.route('/employee/register', methods=['POST'])
def add_data():
    try:
        data = request.json
        print("Received Data:", data)

        emp_id = data['emp_id']
        emp_name = data['emp_name']
        emp_position = data['emp_position']
        phone = data['phone']
        email = data['Email']
        emp_address = data['emp_address']
        emp_password = data['emp_password']
        joining_date = data['joining_date']
        salary = data['salary']
        birthdate = data['birthdate']

 
        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO employees (emp_id, emp_name, emp_position, phone, email, emp_address, emp_password, joining_date, salary, birthdate) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
            (emp_id, emp_name, emp_position, phone, email, emp_address, emp_password, joining_date, salary, birthdate)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Data added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
