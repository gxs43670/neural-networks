class Employee:
    employee_count = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1

    @staticmethod
    def average_salary(employee_list):
        return sum(emp.salary for emp in employee_list) / len(employee_list) if employee_list else 0

class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department, work_hours):
        super().__init__(name, family, salary, department)
        self.work_hours = work_hours

employee1 = Employee("Karthik", "Family1", 50000, "HR")
employee2 = Employee("Karthik", "Family2", 60000, "Finance")
full_time_employee = FullTimeEmployee("Rahul", "Family3", 70000, "IT", 40)

employee_list = [employee1, employee2, full_time_employee]

average_salary = Employee.average_salary(employee_list)
print(f"Average Salary: {average_salary}")
print(f"Number of Employees: {Employee.employee_count}")
