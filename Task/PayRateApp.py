# teacher_name = input("Enter the teacher's name: ")
# period_taught_in_a_month = int(input("Enter period taught in a month: "))
# monthly_rate_per_period = 20
#
# monthly_salary = period_taught_in_a_month * monthly_rate_per_period
#
# if period_taught_in_a_month > 100:
#     over_time_period = period_taught_in_a_month - 100
#     period_taught_in_a_month_greater = period_taught_in_a_month - over_time_period
#     over_time_rate_per_period = 25
#     monthly_rate_per_period = 20
#     monthly_salary = (period_taught_in_a_month_greater * 20) + (over_time_period * 25)
#     print(f"The salary for {teacher_name} is ${monthly_salary}")
# else:
#     monthly_salary = period_taught_in_a_month * monthly_rate_per_period
#     print(f"The salary for {teacher_name} is ${monthly_salary}")


def salary_pay_rate(teachers_name, period_taught_, monthly_rate):

    if period_taught_ > 100:
        over_time_period_ = period_taught_- 100
        period_taught_in_a_month_greater_than_100 = period_taught_ - over_time_period_
        over_time_rate_per_period_ = 25
        monthly_rate = 20
        monthly_salary_paid = (period_taught_in_a_month_greater_than_100 * monthly_rate) + (over_time_period_ * over_time_rate_per_period_)
        return monthly_salary_paid
    else:
        monthly_salary_paid = period_taught_ * monthly_rate
        return monthly_salary_paid

