from flask import Blueprint, request, jsonify
from db_config import mysql
from datetime import date


attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/employee/mark-attendance', methods=['POST'])
def mark_attendance():
    try:
        data = request.json
        emp_id = data['emp_id']
        att_status = data['att_status']
        attendance_date = date.today() 

        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO attendance (emp_id, attendance_date, att_status) 
               VALUES (%s, %s, %s)''',
            (emp_id, attendance_date, att_status)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Attendance marked successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
