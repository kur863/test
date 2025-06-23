class Student:
    def __init__(self, name, high, b):
        self.name = name
        self.high = high
        self.b = b
        self.bmi = 0
        
    def say_hello(self):  # 方法，物件的行為
        print(f"Hi, I'm {self.name} and I'm {self.high} cm ,{self.b} weight")
    
    def BMI(self):
        self.bmi = self.b / ((self.high/100) **2)
        print(f"{self.name} 's BMI is {self.bmi:.2f}")
        
    def comp(self):
        if self.bmi < 18.5:
            print(f"{self.name} is too thin")
        elif self.bmi <24:
            print(f"{self.name} is normor")
        elif self.bmi <27:
            print(f"{self.name} is fat")
        elif self.bmi <30:
            print(f"{self.name} is alittle fat")
        else:
            print(f"{self.name} is too fat")


students = []
students.append(Student("aa",150,60))
students.append(Student("bb",180,80))
students.append(Student("cc",160,70))

while(1):

    try:
    
        num_students = int(input("How many students do you want to enter? "))
        
        for i in range(num_students):
            print(f"Enter details for student {i + 1}:")        
            name = input("Name: ")
            high = float(input("high: "))
            b = float(input("weight: "))            
            # 創建學生物件並將它加入陣列
            student = Student(name, high, b)
            students.append(student)
        
        search_name = input("Please enter the name of the student to search for: ")
        
        # Search logic
        found = False
        for student in students:
            if student.name == search_name:
                print(f"Found {student.name}:")
                student.say_hello()
                student.BMI()
                student.comp()
                found = True
                break
        
        if not found:
            print(f"Student with the name {search_name} not found.")
        
            
    except Exception as e:
        print(e)
        print("error")
        continue
    
    
    

# =============================================================================
# # 顯示所有學生資料
# print("\nStudent Details:")
# for student in students:
#     student.say_hello()
#     student.BMI()
#     student.comp()
#     
# total_high = sum(student.high for student in students)
# 
# print("Total height:", total_high)
# =============================================================================
    



















