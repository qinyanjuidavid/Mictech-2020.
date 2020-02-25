#A class is the blueprint from which specific objects are created.
#A function is basically a block of codes that perform a particular task.
class Student:
    def __init__(self,first_name,last_name,marks):
        #instanciating
        self.first_name=first_name
        self.last_name=last_name
        self.marks=marks
        self.email=f'{first_name}{last_name}@gmail.com'
    def fullname(self):
        print(f'My name is {self.first_name} {self.last_name}.')

    def mark_raise(self):
        Total_marks=self.marks*1.05
        print(f'The Final marks this year is: {Total_marks}')


student1=Student('Jane','Doe',90)
student2=Student('John','Doe',80)
#calling the function
student1.fullname()
student1.mark_raise()
student2.fullname()
student2.mark_raise()


print('==='*100)
class Employee:
    def __init__(self,first_name,last_name,age,salary,department):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.salary=salary
        self.department=department

    def employeeDetails(self):
        print(f'''My name is {self.first_name} {self.last_name}, I am {self.age} years old, I am in {self.department} department and my salary is {self.salary}''')

day=Employee('David','Kinyanjui',37,24000,'IT')
day.employeeDetails()
Doe=Employee('John','Doe',28,35000,'Human Resource')
Doe.employeeDetails()

'''class Taxation:
    def __init__(self,basic_salary,name,bonus):
        self.basic_salary=basic_salary
        self.name=name
        self.bonus=bonus
    def employeeDetails(self):
        salary=self.basic_salary+self.bonus
        tax_rate=eval(input('Enter the tax rate:'))
        tax=salary*tax_rate/100
        Employee_income=salary-tax
        print(f'{self.name}--:>\nSalary: {salary}\nTax: {tax}\nIncome After Tax: {Employee_income}')
kin=Taxation(56000,'John Doe',5000)
kin.employeeDetails()
zuri=Taxation(70000,'Zuri Murugi',11000)
zuri.employeeDetails()'''
#Class Inheritance
class BBIT3:
    def __init__(self,first_name,last_name,unit,marks):
        self.first_name=first_name
        self.last_name=last_name
        self.marks=marks
        self.unit=unit
    def StudentInfo(self):
        print(f'Name: {self.first_name} {self.last_name}\nUnit: {self.unit}\nMarks: {self.marks}')
class IT3(BBIT3):
    def __init__(self,first_name,last_name,marks,unit,hobby,language,age):
        super().__init__(first_name,last_name,unit,marks)
        self.hobby=hobby
        self.language=language
        self.age=age
    def StudentInfo(self):
        print(f'Name: {self.last_name} {self.first_name}\nUnit: {self.unit}\nMarks: {self.marks}\nHobby: {self.hobby}\nMaster Language: {self.language}\nAge: {self.age}')
jane=BBIT3('Jane','Doe','OOP 2',23)
jane.StudentInfo()
ken=IT3('Kenneth','Ngumo', 'OOP 2',27,'Boat Riding','Python',28)
ken.StudentInfo()









































































'''
#instances
student1.first="John"
student1.last="Doe"
student1.email="john@gmail.com"
student1.marks=55


student2.first="Jane"
student2.last="Doe"
student2.email='jane@gmail.com'
student2.marks=90

print(student1.email)
print(student2.email)'''