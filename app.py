from calculator import Calculator
import sys

#equation = "2+2*1983-20"
#print(sys.argv[1])

#calculator = Calculator(equation)

calculator = Calculator(sys.argv[1])
calculator.show_answer()