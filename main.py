class one:
    def self_info(self):
        self.na = []  # Declare as instance variable
        self.ag = []  # Declare as instance variable
        self.no = int(input("Enter number of students: "))  # Corrected indentation
        for i in range(self.no):
            name = input("Name: ")  # Removed global, now local within the loop
            age = int(input("Age: "))
            self.na.append(name)  # Append to instance list, not global
            self.ag.append(age)
        
class two(one):
    def set_marks(self):
        self.s1 = []  # Declare as instance variable
        self.s2 = []  # Declare as instance variable
        self.s3 = []  # Declare as instance variable

        for i in range(self.no):  # Use the self.no from the parent class
            ss1 = int(input("Sub1: "))
            ss2 = int(input("Sub2: "))
            ss3 = int(input("Sub3: "))
            self.s1.append(ss1)
            self.s2.append(ss2)
            self.s3.append(ss3)

class three(two):
    def show_data(self):
        for i in range(self.no):
            print("Name:", self.na[i])  # Use self.na from parent class
            print("Age:", self.ag[i])  # Use self.ag from parent class
            total = self.s1[i] + self.s2[i] + self.s3[i]  # Calculate total
            print("Total marks:", total)

# Instantiate and call methods
obj = three()
obj.self_info()
obj.set_marks()
obj.show_data()
