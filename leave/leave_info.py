from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for Viewing Leave Status
leave_status_bp = Blueprint('leave_status', __name__)

@leave_status_bp.route('/employee/leave-status/<int:emp_id>', methods=['GET'])
def view_leave_status(emp_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT leave_id, leave_title, leave_reason, start_date, end_date 
                       FROM leave_table 
                       WHERE emp_id = %s''', (emp_id,))
        leave_data = cur.fetchall()
        cur.close()

        if not leave_data:
            return jsonify({'message': 'No leave records found'}), 404

        # Convert to JSON format
        leave_list = []
        for leave in leave_data:
            leave_list.append({
                'leave_id': leave[0],
                'leave_title': leave[1],
                'leave_reason': leave[2],
                'start_date': str(leave[3]),  # Convert date to string
                'end_date': str(leave[4])
            })

        return jsonify({'leave_status': leave_list}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
