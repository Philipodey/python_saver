class Employee:
    hourly_rate = 10

    emp_name = ""

    def __init__(self):
        self.__emp_name = None
        self.__emp_department = None
        self.__emp_id = None

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def get_emp_name(self):
        return self.__emp_name

    def set_emp_department(self, emp_department):
        self.__emp_department = emp_department

    def get_emp_department(self):
        return self.__emp_department

    @staticmethod
    def calculate_emp_salary(number_of_hours_worked):
        return Employee.hourly_rate * number_of_hours_worked

    def emp_assign_department(self):
        return self.__emp_department

    def print_employee_detail(self):
        pass
