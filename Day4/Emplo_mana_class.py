class Employ:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name: ",self.name)
        print("salary: ",self.salary)
class Manager(Employ):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.dept=dept
    def display(self):
        print("name: ",self.name)
        print("salary: ",self.salary)
        print("dept: ",self.dept)
if __name__=="__main__":
    man=Manager("uday",30000,"r&d")
    man.display()
