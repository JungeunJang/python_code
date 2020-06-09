# class A:
#     def __init__(self, a):
#        self.a = a
#     def __add__(self,o):
#         return self.a * o.a
#     def __str__(self, o):
#         return super().__str__()
# a = A(8)
# b = A(3)
# c = a.__add__(b)
# c2 = a+b
# print(c , c2)

# (1,2) + (3, 4) -> (3, 6)
#t = Test(1,2)
#t2 = Test(3,4)
#t +t2  => (4,6) 으로 만들고 싶음

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, v):
        return self.a + v.a, self.b +v.b

t = Test(1,2)
t2 = Test(3,4)
t3 = t+t2
t4 = t.__add__(t2)
print(t3)
    
