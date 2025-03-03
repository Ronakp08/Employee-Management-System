from flask import Blueprint, jsonify, request
from db_config import mysql

# Create a Blueprint for view routes
view_bp = Blueprint('view', __name__)

@view_bp.route('/employees/profile/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM employees WHERE emp_id = %s''', (emp_id,))
        employee = cur.fetchone()
        cur.close()

        if employee:
            return jsonify({'employee': employee}), 200
        else:
            return jsonify({'error': 'Employee not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
