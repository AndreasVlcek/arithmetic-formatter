def arithmetic_arranger(problems, showResult=False):

  # The function should optionally take a second argument.
  # When the second argument is set to True, the answers should be displayed.

  # First, let's handle all the Error cases

  # Error: Too many problems
  if len(problems) > 5:
    return 'Error: Too many problems.'

  # Error: Operator must be '+' or '-'
  for problem in problems:
    if '*' in problem or '/' in problem:
      return "Error: Operator must be '+' or '-'."

  # Error: Numbers must only contain digits.
  for problem in problems:
    for element in problem:
      for char in element:
        if char.isalpha():
          return 'Error: Numbers must only contain digits.'

  for problem in problems:
    split_problem = problem.split()
    for element in split_problem:
      if len(element) > 4:
        return 'Error: Numbers cannot be more than four digits.'
  """ 
  There should be a single space between the operator and the longest of the two operands, 
  the operator will be on the same line as the second operand, 
  both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
  Numbers should be right-aligned.
  There should be four spaces between each problem.
  There should be dashes at the bottom of each problem. 
  The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
  """

  first_operand_line = ""
  second_operand_line = ""
  dash_line = ""
  result_line = ""

  for problem in problems:

    # split problem and get its elements
    split_problem = problem.split()

    first_operand = split_problem[0]
    second_operand = split_problem[2]
    operator = split_problem[1]

    # calculate result
    if operator == '+':
      result = int(first_operand) + int(second_operand)
    else:
      result = int(first_operand) - int(second_operand)

    # get longer operand to calculate hwo many dashes are required
    length_first_operand = len(first_operand)
    length_second_operand = len(second_operand)

    # length of dashes = operator + ' ' + length of longest operand
    if length_first_operand > length_second_operand:
      dashes = '-' * (2 + length_first_operand)
    else:
      dashes = '-' * (2 + length_second_operand)

    # What rjust does:
    # Return a 20 characters long, right justified version of the word "banana":
    # x = txt.rjust(20)
    first_operand_line += first_operand.rjust(len(dashes)) + ' ' * 4
    second_operand_line += operator + second_operand.rjust(len(dashes) -
                                                           1) + ' ' * 4
    dash_line += dashes + ' ' * 4
    result_line += str(result).rjust(len(dashes)) + ' ' * 4

  arranged_problems = ""

  if showResult:
    arranged_problems = first_operand_line.rstrip(
    ) + '\n' + second_operand_line.rstrip() + '\n' + dash_line.rstrip(
    ) + '\n' + result_line.rstrip()
  else:
    arranged_problems = first_operand_line.rstrip(
    ) + '\n' + second_operand_line.rstrip() + '\n' + dash_line.rstrip()

  return arranged_problems
