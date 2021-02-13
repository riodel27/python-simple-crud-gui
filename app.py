from dearpygui.core import *
from dearpygui.simple import *


# TODO: setup database connection

def save_callback(sender, data):
    print("Save Clicked")

    input_value_employee_name = get_value("employee_name")
    input_value_branch_name = get_value("branch_name")
    input_value_designation = get_value("designation")
    input_value_salary = get_value("salary")

    print('employee name:', input_value_employee_name)
    print('branch name:', input_value_branch_name)
    print('designation:', input_value_designation)
    print('salary:', input_value_salary)

    # TODO: save to database


with window("CRUD", width=850, height=500):
    add_text("Hello, world")
    add_spacing(count=2)
    add_text("Basic CRUD")
    add_separator()
    add_spacing(count=12)
    add_text("Employee Name")
    add_input_text("employee_name", default_value="name")
    add_spacing(count=4)
    add_text("Branch Name")
    add_input_text("branch_name", default_value="branch name")
    add_spacing(count=4)
    add_text("Designation")
    add_input_text("designation", default_value="designation")
    add_spacing(count=4)
    add_text("Salary")
    add_input_int("salary")
    add_spacing(count=12)
    add_button("Save", callback=save_callback)


start_dearpygui()
