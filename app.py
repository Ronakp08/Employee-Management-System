from flask import Flask
from flask_cors import CORS
from db_config import init_app
from onboarding.emp_register import emp_register_bp
from employee.update_profile import update_bp
from employee.profile import view_bp
from employee.request_resouce import resource_req_bp
from employee.clock_in import clock_in_bp
from employee.clock_out import clock_out_bp
from leave.apply_leave import leave_apply_bp
from leave.leave_info import leave_status_bp 
from Attendance.add_attendance import attendance_bp
from Attendance.attendance_report import view_attendance_bp
from admin.leave_approval import approve_leave_bp
from admin.res_req import approve_resource_bp
from admin.view_emp_report import emp_rec_bp
from Performance.assign_kpi import assign_kpi_bp
from Performance.view_kpi import kpi_view_bp

app = Flask(__name__)
CORS(app)

# Initialize database
init_app(app)

app.register_blueprint(emp_register_bp)

app.register_blueprint(update_bp)

app.register_blueprint(view_bp)

app.register_blueprint(resource_req_bp)

app.register_blueprint(clock_in_bp)

app.register_blueprint(clock_out_bp)

app.register_blueprint(leave_apply_bp)

app.register_blueprint(leave_status_bp)

app.register_blueprint(attendance_bp)

app.register_blueprint(view_attendance_bp)

app.register_blueprint(approve_leave_bp)

app.register_blueprint(approve_resource_bp)

app.register_blueprint(emp_rec_bp)

app.register_blueprint(assign_kpi_bp)

app.register_blueprint(kpi_view_bp)

if __name__ == "__main__":
    app.run(debug=True)
