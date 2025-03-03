from flask import Blueprint, jsonify, request
from db_config import mysql

# Create a Blueprint for view routes
kpi_view_bp = Blueprint('kpi_view', __name__)

@kpi_view_bp.route('/employees/kpi/<int:emp_id>', methods=['GET'])
def get_employee(emp_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM kpi WHERE emp_id = %s''', (emp_id,))
        employee = cur.fetchone()
        cur.close()

        if employee:
            return jsonify({'employee': employee}), 200
        else:
            return jsonify({'error': 'KPI not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
