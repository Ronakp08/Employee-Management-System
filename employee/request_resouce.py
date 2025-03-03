from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for insertion routes
resource_req_bp = Blueprint('resource_req', __name__)

@resource_req_bp.route('/employee/resource/request', methods=['POST'])
def add_data():
    try:
        data = request.json
        print("Received Data:", data)

        req_title = data['req_title']
        emp_id = data['emp_id']
        req_details = data['req_details']
        req_date = data['req_date']

 
        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO resource_req (req_title,emp_id,req_details,req_date) 
               VALUES (%s, %s, %s, %s)''',
            (req_title,emp_id,req_details,req_date)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Resource Requested'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
