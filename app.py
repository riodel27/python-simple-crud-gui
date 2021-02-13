from dearpygui.core import *
from dearpygui.simple import *
import psycopg2


connection = psycopg2.connect(user="postgres",
                              password="postgres",
                              host="127.0.0.1",
                              port="5432",
                              database="windels")

# Create a cursor to perform database operations
cursor = connection.cursor()

# Fetch result
cursor.execute("SELECT * from employees")
employees = cursor.fetchall()
print("Result ", employees)

# global count
count = len(employees)


def save():
    """
    INSERT INTO employees table
    :return: None
    """
    global count

    # input
    employee_name = get_value("employee_name")
    branch_name = get_value("branch_name")
    designation = get_value("designation")
    salary = get_value("salary")

    # psql insert query
    mySql_insert_query = """INSERT INTO employees (name, branch, designation, salary)
                                VALUES (%s, %s, %s, %s) """

    recordTuple = (employee_name, branch_name, designation, salary)

    cursor.execute(mySql_insert_query, recordTuple)

    connection.commit()

    print("1 Record inserted successfully")

    count += 1

    insert_row("employees_table", count, [
        count, employee_name, branch_name, designation, salary])


with window("CRUD", width=1200, height=800):
    set_window_pos("CRUD", 0, 0)
    add_text("Hello, world")
    add_spacing(count=2)
    add_text("Basic CRUD")
    add_separator()

    # employee name
    add_spacing(count=12)
    add_text("Employee Name")
    add_input_text("employee_name", default_value="name")

    # branch name
    add_spacing(count=4)
    add_text("Branch Name")
    add_input_text("branch_name", default_value="branch name")

    # designation
    add_spacing(count=4)
    add_text("Designation")
    add_input_text("designation", default_value="designation")

    # salary
    add_spacing(count=4)
    add_text("Salary")
    add_input_int("salary")

    # save button
    add_spacing(count=12)
    add_button("Save", callback=save)

    # table
    add_spacing(count=20)
    add_table("employees_table", ["id", "name",
                                  "branch", "designation", "salary"])

    # display fetched employees from db
    for idx, employee in enumerate(employees):
        insert_row("employees_table", idx, [
                   employee[0], employee[1], employee[2], employee[3], employee[4]])


start_dearpygui()
