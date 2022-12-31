def arithmetic_arranger(problems, *args):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    for index, value in enumerate(problems):
        pieces = value.split(" ")

        if len(pieces[0]) > 4 or len(pieces[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if pieces[1] not in "+-":
            return "Error: Operator must be '+' or '-'."

        try:
            value_1 = int(pieces[0])
            value_2 = int(pieces[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        # calculate the length of each line
        value_longest = max(len(pieces[0]), len(pieces[2]))
        width = value_longest + 2

        # create rows
        row_1 = f"{pieces[0]:>{width}}"
        row_2 = pieces[1] + f"{pieces[2]:>{width - 1}}"
        row_3 = '-' * width

        try:
            arranged_problems[0] += (' ' * 4) + row_1
        except IndexError:
            arranged_problems.append(row_1)

        try:
            arranged_problems[1] += (' ' * 4) + row_2
        except IndexError:
            arranged_problems.append(row_2)

        try:
            arranged_problems[2] += (' ' * 4) + row_3
        except IndexError:
            arranged_problems.append(row_3)

        # if True or not
        if args:
            solution = int(pieces[0]) + int(pieces[2]) if pieces[1] == '+' else int(pieces[0]) - int(pieces[2])
            row_4 = f"{str(solution):>{width}}"

            try:
                arranged_problems[3] += (' ' * 4) + row_4
            except IndexError:
                arranged_problems.append(row_4)

        output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
        output = output + f"\n{arranged_problems[3]}" if args else output

    return output
