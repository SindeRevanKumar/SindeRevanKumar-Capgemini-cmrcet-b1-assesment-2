#•	1. Create a class `Employee` with properties `name`, `id`, and `department`. 
# Instantiate an object and assign values dynamically.
class Employees:
    def details(self,employee_id,employee_name,employee_departmant):
        self.employee_id=employee_id
        self.employee_name=employee_name
        self.employee_department=employee_departmant
    def get_employee_details(self):
        print(f"Id:{self.employee_id}\nName:{self.employee_name}\ndepartment:{self.employee_department}")
Id=int(input("Enter the Employee Id : "))
name=input("Enter name of the employee : ")
depart=input("Enter the department : ")
employees=Employees()
employees.details(Id,name,depart)
employees.get_employee_details()