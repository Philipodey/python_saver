from unittest import TestCase
from Task import PayRateApp


class TestPayRateApp(TestCase):
    def test_monthly_hours_greater_than_100(self):
        teacher_name = "Ade"
        period_taught = 97
        monthly_rate = 20
        result = 1940
        expected = PayRateApp.salary_pay_rate(teacher_name, period_taught, monthly_rate)
        self.assertEqual(result, expected)
