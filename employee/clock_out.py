from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for Clock-Out
clock_out_bp = Blueprint('clock_out', __name__)

@clock_out_bp.route('/employee/clock-out', methods=['POST'])
def clock_out():
    try:
        data = request.json
        print("Received Clock-Out Data:", data)

        emp_id = data['emp_id']
        clock_out_time = data['clock_out']

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE clock_tracker 
               SET clock_out = %s 
               WHERE emp_id = %s AND clock_out IS NULL''',
            (clock_out_time, emp_id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Clock-out recorded successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
