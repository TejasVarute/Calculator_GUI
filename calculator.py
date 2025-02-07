class Calculator():
    def __init__(self, to_calculate):
        for symbol in ('+', '-', '*', '/'):
            if symbol in to_calculate:
                n1, n2 = to_calculate.split(symbol)
                self.n1, self.n2 = int(n1), int(n2)
                self.action = symbol
                break
    
    def addition(self):
        return self.n1 + self.n2
    
    def subtraction(self):
        return self.n1 - self.n2
    
    def multiplication(self):
        return self.n1 * self.n2
    
    def division(self):
        return self.n1 / self.n2
    
    def Calculate(self):
        action_to_d = {
            '+': self.addition,
            '-': self.subtraction,
            '*': self.multiplication,
            '/': self.division
        }
        return action_to_d[self.action]()