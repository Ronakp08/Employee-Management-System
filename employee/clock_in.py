from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for Clock-In
clock_in_bp = Blueprint('clock_in', __name__)

@clock_in_bp.route('/employee/clock-in', methods=['POST'])
def clock_in():
    try:
        data = request.json
        print("Received Clock-In Data:", data)

        emp_id = data['emp_id']
        clock_in_time = data['clock_in']

        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO clock_tracker (emp_id, clock_in) 
               VALUES (%s, %s)''',
            (emp_id, clock_in_time)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Clock-in recorded successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
