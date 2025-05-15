class employee :
    def details(self):
        self.name = input("enter your name : \n")
        self.id=int(input("Enter you id : \n"))
        self.designation = input("enter your designation : \n")
        self.salary=int(input("Enter you salary : \n"))
        ta = (self.salary/100)*2.5
        da = (self.salary/100)*1.5
        self.tsalary=ta+da+self.salary
    def display(self):
        print("the name of employee",self.name)
        print("the name of id",self.id)
        print("the name of designation",self.designation)
        print("the name of salary",self.salary)
        print("the name of tsalary",self.tsalary)

emp=employee()
emp.details()
emp.display()