from flask import Blueprint, request, jsonify
from db_config import mysql

# Create a Blueprint for resource approval
approve_resource_bp = Blueprint('approve_resource', __name__)

@approve_resource_bp.route('/employee/resource/approve/<int:req_id>', methods=['PUT'])
def approve_resource(req_id):
    try:
        data = request.json
        req_status = data['req_status'] 

        cur = mysql.connection.cursor()
        cur.execute(
            '''UPDATE resource_req 
               SET req_status = %s 
               WHERE req_id = %s''',
            (req_status, req_id)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': f'Resource request {req_status}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
