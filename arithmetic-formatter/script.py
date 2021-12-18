
def arithmetic_arranger(problems, solved=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        operation = problem.split()
        operator = operation[1]
        if not(operator == '+' or operator == '-'):
            return "Error: Operator must be '+' or '-'."

        operand_1 = operation[0]
        operand_2 = operation[2]

        if len(operand_1) > 4 or len(operand_2) > 4:
            return "Error: Numbers cannot be more than four digits."

        try:
            operand_1 = int(operand_1)
            operand_2 = int(operand_2)
        except:
            return "Error: Numbers must only contain digits."


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
