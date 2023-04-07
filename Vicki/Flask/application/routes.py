# from flask import render_template, jsonify, request
# from application.models.manager import Manager
#
# from application import app, service
#
#
# @app.route('/employees', methods=['GET'])
# def show_employees():
#     error = ""
#     employees = service.get_all_employees()
#     if len(employees) == 0:
#         error = "There are no employees to display"
#     return render_template('employees.html', employees=employees, message=error)
#     #return jsonify(employees)
#
#
# # this is a ReST endpoint - only returns data
# @app.route('/employees/<int:emp_id>', methods=['GET'])
# def show_employee(emp_id):
#     error = ""
#     employee = service.get_employee_by_id(emp_id)
#     if not employee:
#         return jsonify("There is no employee with ID: " + str(emp_id))
#     else:
#         print(employee.first_name, employee.last_name)
#     return jsonify(employee)
#
#
# @app.route('/managers/<int:man_id>', methods=['GET'])
# def get_manager(man_id):