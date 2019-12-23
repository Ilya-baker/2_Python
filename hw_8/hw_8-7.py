class ComplexNumber:
# не уверен что до конца разобрался в самом понятии комплексного числа. Поэтому смущают выходные данные по умножению,
# сумма, вроде, расчитана верно.
    def __init__(self, compl_num):
        self.compl_num = compl_num

    def __add__(self, param):
        return f"Addition: {self.compl_num + param.compl_num}"

    def __mul__(self, param):
        return f"Multiplication: {self.compl_num * param.compl_num}"


com_sum = ComplexNumber(4 + 5j)
com_dif = ComplexNumber(2 - 3j)

print(com_sum + com_dif)
print(com_sum * com_dif)