def arithmetic_arranger(problems, solved=False):
    operations = list()

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        expression = problem.split()
        operator = expression[1]
        if not(operator == '+' or operator == '-'):
            return "Error: Operator must be '+' or '-'."

        operand_1 = expression[0]
        operand_2 = expression[2]

        try:
            operand_1 = int(operand_1)
            operand_2 = int(operand_2)
        except:
            return "Error: Numbers must only contain digits."

        length_1 = len(str(operand_1))
        length_2 = len(str(operand_2))
        length_max = length_1 > length_2 and length_1 or length_2

        if length_max > 4:
            return "Error: Numbers cannot be more than four digits."

        width = length_max + 2

        operation = dict()
        operation['operand_1'] = operand_1
        operation['operand_2'] = operand_2
        operation['operator'] = operator
        operation['width'] = width

        if solved:
            solution = operator == '+' and operand_1 + operand_2 or operand_1 - operand_2
            operation['solution'] = solution

        operations.append(operation)

    spaces = ' ' * 4
    lines = ['', '', '']
    if solved:
        lines.append('')

    for operation in operations:
        width = operation['width']
        lines[0] = lines[0] + str(operation['operand_1']).rjust(width) + spaces
        lines[1] = lines[1] + operation['operator'] + ' ' + \
            str(operation['operand_2']).rjust(width - 2) + spaces

        lines[2] = lines[2] + '-' * width + spaces

        if solved:
            lines[3] = lines[3] + \
                str(operation.get('solution', '')).rjust(width) + spaces

    arranged_problems = ''
    for line in lines:
        arranged_problems = arranged_problems + line.rstrip() + '\n'

    return arranged_problems.rstrip()


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
