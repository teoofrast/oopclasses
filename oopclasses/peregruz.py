class Calculator:
    def sum(self, x, y):
        return x + y


class StringCalculator(Calculator):
    def sum(self, x, y):
        return str(x) + str(y)


calc = Calculator()
print(calc.sum(5, 7))
str_calc = StringCalculator()
print(str_calc.sum("Hello ", "world!"))
