hourly_rate = 10


class Employee:
    emp_name = ""

    def __init__(self):
        pass

    @classmethod
    def set_emp_name(self, emp_name):
        self.emp_name = emp_name

    @classmethod
    def get_emp_name(self):
        return self.emp_name

    @classmethod
    def set_emp_department(self, emp_department):
        self.emp_department = emp_department

    def get_emp_department(self):
        return self.emp_department

    @staticmethod
    def calculate_emp_salary(self, number_of_hours_worked):
        emp_salary = hourly_rate * number_of_hours_worked
        return emp_salary

    def emp_assign_department(self):
        pass

    @classmethod
    def print_employee_detail(self):
        pass
