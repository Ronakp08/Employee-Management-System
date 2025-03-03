from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for Leave Application
leave_apply_bp = Blueprint('leave_apply', __name__)

@leave_apply_bp.route('/employee/apply-leave', methods=['POST'])
def apply_leave():
    try:
        data = request.json
        print("Received Leave Request:", data)

        leave_title = data['leave_title']
        leave_reason = data['leave_reason']
        start_date = data['start_date']
        end_date = data['end_date']
        emp_id = data['emp_id']

        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO leave_table (leave_title, leave_reason, start_date, end_date, emp_id) 
               VALUES (%s, %s, %s, %s, %s)''',
            (leave_title, leave_reason, start_date, end_date, emp_id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Leave applied successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
