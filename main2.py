class Personal:
    def write_info(self):
        self.name = input("Enter name")
        self.age = input("Enter Age")
        self.basic = float(input("Enter basic salary"))
class working(Personal):
         def working_info(self):
          self.w = int(input("Enter Working days"))
class show(working):
     def show_info(self):
        basicsalary = self.basic/26*self.w
        print("Name",self.name)
        print("Age",self.age)
        print("salary",basicsalary)
obj = show()
obj.write_info()  
obj.working_info()   
obj.show_info()