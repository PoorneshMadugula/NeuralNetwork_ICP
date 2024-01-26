class employee:
    emp_count = 0

    def __init__(mine, name, family, salary, department):

        mine.name = name
        mine.family = family
        mine.salary = salary
        mine.department = department

        employee.emp_count +=1

    def average_salary(salary_amount):
        if not salary_amount:
            return 0

        return sum(salary_amount) / len(salary_amount)

class FullTime_employee(employee):
    def __init__(self, name, family, salary, department, employment_type):

        super(FullTime_employee, self).__init__(name, family, salary, department)
        
        self.employment_type = employment_type


empl_1 = employee("Poornesh", "Royal Family", 60000, "Telecom")
empl_2 = employee("Madugula", "Legal Family", 75000, "IT")

F_empl_1 = FullTime_employee("Alien", "Kings Family", 90000, "HR", "Full-time")
F_empl_2 = FullTime_employee("Elica", "Queen Family", 85000, "EC", "Full-time")

avr_sal_emps = employee.average_salary([empl_1.salary, empl_2.salary,
                                                        F_empl_1.salary, F_empl_2.salary])

print(f"Total no of employees: {employee.emp_count}")
print(f"Average salary of all employees: {avr_sal_emps}")



