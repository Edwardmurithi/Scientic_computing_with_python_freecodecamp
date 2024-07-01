def arithmetic_arranger(problems, display_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []

    for problem in problems:
        parts = problem.split()
        first_operand, operator, second_operand = parts

        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Validate digits and length
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)

    # Prepare lists to store the arranged problems
    top_row = []
    bottom_row = []
    lines = []
    results = []

    for i in range(len(problems)):
        first_operand = first_operands[i]
        operator = operators[i]
        second_operand = second_operands[i]

        max_width = max(len(first_operand), len(second_operand)) + 2
        top_row.append(first_operand.rjust(max_width))
        bottom_row.append(operator + second_operand.rjust(max_width - 1))
        lines.append('-' * max_width)

        if display_answers:
            if operator == '+':
                result = str(int(first_operand) + int(second_operand))
            else:
                result = str(int(first_operand) - int(second_operand))
            results.append(result.rjust(max_width))

    arranged_problems = '    '.join(top_row) + '\n' + '    '.join(bottom_row) + '\n' + '    '.join(lines)
    if display_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems