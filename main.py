class student():
    def personalinformation(self):
        self.name = input("Enter Name")
        self.age = input("Enter Age")
        self.std = input("Enter Grade")
        self.rollno = input("Enter roll no")
class Marks(student):
    def subject(self):
        self.sub1 = input("Enter sub1 marks")
        self.sub2 = input("Enter sub2 marks")
        self.sub3 = input("Enter sub3 marks")
        self.sub4 = input("Enter sub4 marks")
    def show_marks(self):
        sub_total = self.sub1+self.sub2+self.sub3+self.sub4
        print("name",self.name)
        print("age",self.age)
        print("standard",self.std)
        print("rollno",self.rollno)
        print("total marks",sub_total)
class final(Marks):
        def information(self):
         self.addr = "1902,Noida"
         self.pin = "201301"
         print(self.addr)
         print(self.pin)
obj = final()
obj.personalinformation()
obj.subject()
obj.show_marks()
obj.information()
