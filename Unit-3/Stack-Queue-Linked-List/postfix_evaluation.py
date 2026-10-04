# Postfix expression evaluation using Stack

def evaluate_postfix(expression):
    stack = []

    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            else:
                raise ValueError("Unsupported operator")

            stack.append(result)

    return stack.pop()


expression = "2 3 4 * +"

print("Postfix Expression:", expression)
print("Result:", evaluate_postfix(expression))
