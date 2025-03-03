from flask import Blueprint, request, jsonify
from db_config import mysql
from datetime import date


assign_kpi_bp = Blueprint('kpi', __name__)

@assign_kpi_bp.route('/employee/assign-kpi', methods=['POST'])
def mark_attendance():
    try:
        data = request.json
        kpi_id = data['kpi_id']
        emp_id = data['emp_id']
        kpi_desc = data['kpi_desc']
        kpi_points = data['kpi_points']

        cur = mysql.connection.cursor()
        cur.execute(
            '''INSERT INTO kpi (kpi_id,emp_id,kpi_desc,kpi_points) 
               VALUES (%s, %s, %s, %s)''',
            (kpi_id,emp_id,kpi_desc,kpi_points)
        )
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'KPI assigned successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
