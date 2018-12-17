class Calculator:
    def __init__(self, a, b, l):
        self.a = a
        self.b = b
        self.l = l

    def add(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def sumList(self):
        return sum(self.l)

if __name__ == '__main__':
    calc = Calculator(5,4,[1,2,3,4,5])
    print(calc.add())
    print(calc.subtraction())
    print(calc.sumList())

