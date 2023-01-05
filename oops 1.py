class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
        Employee.empCount +=1
    def displayCount(self):
        print("Total Employee {0} ".format(Employee.empCount))
    def displayEmployee(self):
        print("Name :",self.name, ", Salary: ",self.salary)
emp1=Employee("Nikhil",9999)
##print("Total Employee: ",Employee.empCount)
##emp2=Employee("Abinn",54000)
##emp1.displayEmployee()
##emp2.displayEmployee()
##print("Total Employee :{0}".format(Employee.empCount))
##emp3=Employee('Manu Gupta',55500)
##emp3.displayCount()
##emp2.displayCount()
##emp1.displayCount()
##print("Total Employee :{0}".format(Employee.empCount))
##


emp1.displayEmployee()
emp1.salary=17000
emp1.experience=3
emp1.displayEmployee()
emp1.name='Manoj'
emp1.displayEmployee()
print(emp1.experience)
#del emp1.salary
emp1.displayEmployee()
