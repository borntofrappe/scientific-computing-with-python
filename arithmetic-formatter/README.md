# [arithmetic-formatter](https://replit.com/@borntofrappe/boilerplate-arithmetic-formatter)

[The assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter) asks to create a function to format arithmetic problems with a specific set of rules.

## Input

A list of strings and an optional boolean.

```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

## Output

A string highlighting an error message in the following instances:

- there are more than five projects: `Error: Too many problems.`

- the operators describe multiplication or division: `Error: Operator must be '+' or '-'.`

- the operands contain non-digit characters: `Error: Numbers must only contain digits.`

- the operands have more than four digits: `Error: Numbers cannot be more than four digits.`

Outside of these cases, a string arranging the problems vertically and side by side. The problems should be solved only if the second argument resolves to `True`.

Formatting rules:

- a single space between operator and the longest of the two operands

- operator on the same line as the second operand

- operand in the order provided by the function

- numbers right aligned

- four spaces between successive problems

- dashes below the problems covering the space of each problem

```text
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

## Notes

The first step to tackle the problem is updating the `arithmetic_arranger` function to accept two arguments, the problems and the optional boolean.

```py
def arithmetic_arranger(problems, solved=False):
```

From this setup, the most immediate portion relates to the error messages:

- too many problems

  ```py
  if len(problems) > 5:
    return 'Error: Too many problems.'
  ```

- operator not describing addition or subtraction

  For this step it is first necessary to loop through the problems, break up the operation in its three components and consider the operator

  ```py
  for problem in problems:
    operation = problem.split()
    operator = operation[1]
  ```

  It's possible to check the condition in at least two ways:

  1. the operator is different from `+` and `-`

  2. the operator is not `+` or `-`

  I chose the latter since it seems to fit more the error message

  ```py
  if not(operator == '+' or operator == '-'):
    return "Error: Operator must be '+' or '-'."
  ```

- operands more than four digits long

  The `split` function returns a list of strings, so that it is immediately possible to consider the length of the string

  ```py
  operand_1 = operation[0]
  operand_2 = operation[2]

  if len(operand_1) > 4 or len(operand_2) > 4:
    return "Error: Numbers cannot be more than four digits."
  ```

  The assignment doesn't specify the order in which the error messages should be produced, so I prefer this option to first parsing the operand to numerical values and consider if they exceed `9999` in absolute terms

- operands contain non-digit characters

  Here it is possible to rely on a `try..except` block. Try to explicitly convert the strings into integers:

  ```py
  try:
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
  ```

  When an error is raised return the desired string

  ```py
  except:
    return "Error: Numbers must only contain digits."
  ```
