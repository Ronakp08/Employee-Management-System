from flask import Blueprint, jsonify, request
from db_config import mysql

update_bp = Blueprint('update', __name__)

@update_bp.route('/employee/update/<int:id>', methods=['PUT'])
def update_data(id):
    try:
        data = request.json
        emp_name = data.get('emp_name') 
        phone = data.get('phone')
        salary = data.get('salary')

        cur = mysql.connection.cursor()


        update_fields = []
        update_values = []

        if emp_name:
            update_fields.append("emp_name = %s")
            update_values.append(emp_name)
        if phone:
            update_fields.append("phone = %s")
            update_values.append(phone)
        if salary:
            update_fields.append("salary = %s")
            update_values.append(salary)

        if not update_fields:
            return jsonify({'error': 'No valid fields provided for update'}), 400

        update_query = f"UPDATE employees SET {', '.join(update_fields)} WHERE emp_id = %s"
        update_values.append(id)

        cur.execute(update_query, tuple(update_values))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Data updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
