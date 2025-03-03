from flask_mysqldb import MySQL

mysql = MySQL()

def init_app(app):
    """Initialize MySQL with the Flask app."""
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'emp_portal'
    mysql.init_app(app)  
