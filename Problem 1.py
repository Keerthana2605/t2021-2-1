#problem 1

class Calci:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    
    def add(self):
        return eval('self.n1 + self.n2')
    
    def sub(self):
        return eval('self.n1 - self.n2')
    
    def mul(self):
        return eval('self.n1 * self.n2')
    
    def div(self):
        return eval('self.n1 / self.n2')

first=float(input())
second=float(input())
cal=Calci(first,second)

result1=cal.add()
print(f"Addition: {result1}")

result2=cal.sub()
print(f"Subtraction: {result2}")

result3=cal.mul()
print(f"Multiplication: {result3}")

result4=cal.div()
print(f"Division: {result4}")