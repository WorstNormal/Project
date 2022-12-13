class A:
    def __init__(self, w=200, h=100):
        self.w = w
        self.h = h

# Наследуются аргументы по умолчанию
class B(A):
    def __init__(self):
        super().__init__()
        B.f(self)
        
    def f(self):
        print(self.w, self.h) # 200, 100

B()