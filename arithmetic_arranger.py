def arithmetic_arranger(problems, calc = False):

  operationExamples = ("+", "-")
  numberofProblems = len(problems)
  if numberofProblems > 5:
    return 'Error: Too many problems.'

  firstrow = ''
  secondrow = ''
  thirdrow = ''
  fourthrow = ''

  for problem in problems:
    lst = problem.split(" ")
    if lst[1] not in operationExamples:
      return "Error: Operator must be '+' or '-'."

    if not lst[0].isnumeric() or not lst[2].isnumeric():
      return "Error: Numbers must only contain digits."

    if len(lst[0]) > 4 or len(lst[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    left = lst[0]
    operation = lst[1]
    right = lst[2]

    if operation == "+":
      answer = int(left) + int(right)
    if operation == "-":
      answer = int(left) - int(right)
    answer = str(answer)

    width = max(len(left), len(right)) + 2

    top = left.rjust(width)
    bottom = operation + str(right).rjust(width - 1)
    line = ''
    res = answer.rjust(width)
    line = "-" * width
     
    if problem != problems[-1]:
      firstrow += top + '    '
      secondrow += bottom + '    '
      thirdrow += line + '    '
      fourthrow += res + '    '
    else:
      firstrow += top 
      secondrow += bottom
      thirdrow += line
      fourthrow += res

  
  if calc:
    arranged_problems = firstrow + '\n' + secondrow + '\n' + thirdrow + '\n' + fourthrow
  else: 
    arranged_problems = firstrow + '\n' + secondrow + '\n' + thirdrow
  
  return arranged_problems

