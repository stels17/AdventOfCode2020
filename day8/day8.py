from copy import deepcopy


def alter_line(line : dict):
    # sample line: {'statement': 'jmp +4', 'visited': False}
    operator = line['statement'][:3]
    if operator == 'jmp':
        new_statement = 'nop'
    else:
        new_statement = 'jmp' 

    line['statement'] = new_statement + line['statement'][3:]


def execute_script(lines : list, execution_journal: list):
    if len(execution_journal) == 0:
      return [False, 0]   # something went wrong

    # Get the last operation and change it
    last_statement = execution_journal.pop()
    current_line = last_statement['line']
    accumulator = last_statement['accumulator']
    # make a copy of the original lines
    code_lines = deepcopy(lines)
    # Alter
    alter_line(code_lines[current_line])
    # mark all as not visited
    for code_line in code_lines:
        code_line['visited'] = False

    while not code_lines[current_line]['visited']:
        code_lines[current_line]['visited'] = True
        operator, operand = code_lines[current_line]['statement'].split()

        if operator == 'acc':
            accumulator += int(operand)
        elif operator == 'jmp':
            current_line += int(operand) - 1

        current_line += 1

        if current_line == len(code_lines):
            # We've reached the end!
            return [True, accumulator]
    else:
        # we faced infinite loop
        # print("Not succeeded this time. Journal:", execution_journal)
        return execute_script(lines, execution_journal)


# We go thru the lines tracking our path until we get to the line we already executed before. 
# Once there, we need to get to the last jmp/nop statement (get it from the Journal) and change it. Also, restore the accumulator value
# If doing so, we again start looping, we need to get back to the previous instruction and change it. But! We need to change it in the initial lines list (only one change in lines is accepted)


def exercise():
    f = open("ex8.txt", "rt")
    lines = f.read().splitlines()
    f.close()

    accumulator = 0
    current_line = 0
    execution_journal = []

    lines = list(map(lambda x: {'statement': x, 'visited': False}, lines))

    while not lines[current_line]['visited']:
        lines[current_line]['visited'] = True
        operator, operand = lines[current_line]['statement'].split()

        if operator in ['jmp', 'nop']:
            # record the operation and remember the acc value
            execution_journal.append({
                'line': current_line,
                'accumulator': accumulator
            })

        if operator == 'acc':
            accumulator += int(operand)
        elif operator == 'jmp':
            current_line += int(operand) - 1

        current_line += 1

    # We have all interesting operations in the journal
    
    print('Accumulator value before an inf loop:', accumulator)
    
    success, accumulator = execute_script(lines, execution_journal)
    if success:
      print("Accumulator once the instructions fixed:", accumulator)

    

exercise()


