class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Student name: ",self.name,end='\n')
        print("Student roll: ",self.roll,end='\n')
        print("Student marks: ",self.marks,end='\n')
if __name__=="__main__":
    st1=Student("ud",101,67)
    st2=Student("manju",102,99)
    st1.display()
    st2.display()

