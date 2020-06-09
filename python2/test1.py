class Employee:
    name = "강감찬"
    count = 0
    
    def __init__(self, name="없음"):
        # print(name, self.count)
        Employee.count += 1
        print(Employee.count) #클래스의 변수를 출력할꺼면ㅡ 
    def display(self, a = 0):
        print(self.count, a)
    def __del__(self):
        print("delete")

class Employee2(Employee):
    def __init__(self):
        print("Employee2 생성자")
    def display2(self):
        print("Employee2 Display2")
    def display(self, a=0, b =1):
        print(a, b)

e4 = Employee2()
e4.display()
e4.display2()








# e = Employee()
# e.display()
# e.display(10)
# e.b = 10

