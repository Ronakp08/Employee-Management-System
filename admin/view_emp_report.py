from flask import Blueprint, jsonify
from db_config import mysql


emp_rec_bp = Blueprint('emp_rec', __name__)

@emp_rec_bp.route('/employees', methods=['GET'])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM employees''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)
