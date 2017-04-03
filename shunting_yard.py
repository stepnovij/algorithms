"""
Shunting-yard algorithm by Edsger Dijkstra
"""


def evaluate(operation):
    stack_operators = []
    stack_operands = []
    for symbol in list(operation):
        if symbol == '(':
            pass
        elif symbol in ['+', '-', '*', '/']:
            stack_operators.append(symbol)
        elif symbol == ')':
            op = stack_operators.pop()
            val = stack_operands.pop()
            if op == '+':
                val = stack_operands.pop() + val
            elif op == '-':
                val = stack_operands.pop() - val
            elif op == '*':
                val = stack_operands.pop() * val
            elif op == '/':
                val = stack_operands.pop() / val
            stack_operands.append(val)
        elif symbol.isdigit():
            stack_operands.append(int(symbol))
    return stack_operands[0]


if __name__ == '__main__':
    operation = '(((1 + 2) + 3)*4)'
    assert evaluate(operation) == 24
    operation = '(((4/2)*(2+1))+((3+2)+(4*3)))'
    assert evaluate(operation) == 23, evaluate(operation)
