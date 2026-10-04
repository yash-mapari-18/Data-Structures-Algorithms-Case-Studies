# Infix to Postfix and Prefix conversion using Stack

def precedence(operator):
    if operator in ("+", "-"):
        return 1
    if operator in ("*", "/"):
        return 2
    if operator == "^":
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    output = []

    for token in expression:
        if token.isalnum():
            output.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

        else:
            while (
                stack
                and stack[-1] != "("
                and precedence(stack[-1]) >= precedence(token)
            ):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        output.append(stack.pop())

    return "".join(output)


def infix_to_prefix(expression):
    reversed_expression = expression[::-1]

    swapped = ""
    for token in reversed_expression:
        if token == "(":
            swapped += ")"
        elif token == ")":
            swapped += "("
        else:
            swapped += token

    postfix = infix_to_postfix(swapped)
    return postfix[::-1]


expression = "A+B*C"

print("Infix   :", expression)
print("Postfix :", infix_to_postfix(expression))
print("Prefix  :", infix_to_prefix(expression))
