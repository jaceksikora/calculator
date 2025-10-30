class Calculator:
    def __init__(self, op1: float, op2: float):
        try:
            self.op1 = float(op1)
            self.op2 = float(op2)
        except (TypeError, ValueError):
            raise TypeError(f"To muszą byś liczby")

    def sum(self) -> float:
        return self.op1 + self.op2

    def subtract(self) -> float:
        return self.op1 - self.op2

    def multiply(self) -> float:
         return self.op1 * self.op2

    # Zwracamy informację użytkownikowi ale nie rzucamy wyjątku
    def divide(self):
        if self.op2 == 0:
            return "Dzielenie przez zero"
        return self.op1 / self.op2

# if __name__ == '__main__':
        # calc = Calculator(1, 2)
    # print(calc.sum())
    # print(calc.subtract())
    # print(calc.multiply())
    # print(calc.divide())

