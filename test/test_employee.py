from unittest import TestCase

from Task.employee import Employee


class TestEmployee(TestCase):
    # def setUp(self) -> None:

    def test_calculate_emp_salary(self):
        employee = Employee()
        number_of_hours_worked = 10
        expected = employee.calculate_emp_salary(number_of_hours_worked)
        self.assertEqual(100, expected)

    def test_emp_assign_department(self):
        self.fail()

    def test_print_employee_detail(self):
        self.fail()
