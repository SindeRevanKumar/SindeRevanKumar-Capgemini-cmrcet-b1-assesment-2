	# 7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` 
    # has an additional method `approve_leave()`.
class Person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def display():
        print("name:{self.name}\n gender:{self.gender}\n age:{self.age}")
class Employee(Person):
    def __init__(self,employee_id,name,gender,age):
        super().__init__(name,gender,age)
        self.employee_id=employee_id
    def displayy(self):
        print(f"name:{self.name}\n gender:{self.gender}\n age:{self.age}\nemployee_id{self.employee_id}")
class Manager(Employee):
    def __init__(self,manager,employee_id,name,gender,age):
        super().__init__(employee_id,name,gender,age)
        self.manager=manager
    def displayyy(self):
        print(f"name : {self.name}\ngender : {self.gender}\nage : {self.age}\nemployee_id : {self.employee_id}\nmanager_name : {self.manager}")
    def leave_aprove(self):
        print(f"name : {self.name}\ngender : {self.gender}\nage : {self.age}\nemployee_id : {self.employee_id}\nmanager_name : {self.manager}\nthe leave is approved...")
m=Manager("REVAN","123","hulk","male","23")
m.displayyy()
m.leave_aprove()
