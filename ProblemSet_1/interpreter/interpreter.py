# Prompt the user to input a mathematical expression as a string.
expression: str = input("Expression: ")

# Use the 'eval' function to evaluate the expression and convert the result to a float.
result: float = float(eval(expression))

# Print the result of the evaluated expression.
print(result)
