from flask import Blueprint, request, jsonify
from db_config import mysql


view_attendance_bp = Blueprint('view_attendance', __name__)

@view_attendance_bp.route('/employee/attendance/<int:emp_id>', methods=['GET'])
def get_attendance(emp_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT attendance_date, att_status 
                       FROM attendance 
                       WHERE emp_id = %s''', (emp_id,))
        attendance_data = cur.fetchall()
        cur.close()

        if not attendance_data:
            return jsonify({'message': 'No attendance records found'}), 404

        attendance_list = []
        for record in attendance_data:
            attendance_list.append({
                'attendance_date': str(record[0]), 
                'att_status': 'Present' if record[1] == 1 else 'Absent'
            })

        return jsonify({'attendance_records': attendance_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
