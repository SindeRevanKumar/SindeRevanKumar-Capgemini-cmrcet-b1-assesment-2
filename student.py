class School:
    def __init__(self,name,rollnumber,gender,classs):
        self.name=name
        self.rollnumber=rollnumber
        self.gender=gender
        self.classs=classs
    def display(self):
        print(f"name:{self.name}\nrollno:{self.rollnumber}\ngender:{self.gender}\nclass:{self.classs}")
name=input("enter the name of the student : ")
ro=int(input("enter the roll number of the student : "))
gen=input("enter the gender of the student : ")
clss=input("enter the class of the student : ")
s=School(name,ro,gen,clss)
s.display()