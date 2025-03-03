from flask import Blueprint, request, jsonify
from db_config import mysql


approve_leave_bp = Blueprint('approve_leave', __name__)

@approve_leave_bp.route('/employee/approve-leave/<int:leave_id>', methods=['PUT'])
def approve_leave(leave_id):
    try:
        data = request.json
        leave_status = data['leave_status']

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE leave_table 
               SET leave_status = %s 
               WHERE leave_id = %s''',
            (leave_status, leave_id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': f'Leave request {leave_status}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
