# [arithmetic-formatter](https://replit.com/@borntofrappe/boilerplate-arithmetic-formatter)

[The assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter) asks to create a function to format arithmetic problems following specific rules.

## Input

A list of strings and an optional boolean.

```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

## Output

A string highlighting an error message in the following instances:

- there are more than five projects

- the operators describe multiplication or division

- the operands contain non-digit characters

- the operands have more than four digits

Outside of these instances, the output is a string arranging the problems vertically and side by side. The problems should be solved only if the second argument resolves to `True`.

In terms of formatting the assignment asks to follow the following rules:

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

## Solution

Define `arithmetic_arranger` as a function with two parameters: `problems` and `solved`. Give `solved` a default value of `False` to make the argument optional.

```py
def arithmetic_arranger(problems, solved=False):
```

In the body of the function, begin by considering the error messages:

- there are more than five projects

  ```py
  if len(problems) > 5:
    return 'Error: Too many problems.'
  ```

- the operators describe multiplication or division

  For this step it is first necessary to loop through the problems, break up the operation in its three components and consider the operator

  ```py
  for problem in problems:
    operation = problem.split()
    operator = operation[1]
  ```

  Check the condition in one of at least two ways:

  1. the operator is different from `+` and `-`

  2. the operator is not `+` or `-`

  I preferred the second option since it seems to fit more the error message

  ```py
  if not(operator == '+' or operator == '-'):
    return "Error: Operator must be '+' or '-'."
  ```

- the operands contain non-digit characters

  Include a `try` block to explicitly convert the strings into integers:

  ```py
  try:
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
  ```

  Return the error message in the `except` block.

  ```py
  except:
    return "Error: Numbers must only contain digits."
  ```

- the operands have more than four digits

  The `split` function returns a list of strings, so that it would be possible to consider the length of the string

  ```py
  operand_1 = operation[0]
  operand_2 = operation[2]

  if len(operand_1) > 4 or len(operand_2) > 4:
    return "Error: Numbers cannot be more than four digits."
  ```

  However, to follow the specific order of the assignment the condition is checked _after_ the operands have been converted to integer. Here there are at least two solutions: check if either number exceeds `9999` in absolute terms, retrieve the length of the string for each operand and check if either exceeds `4` characters. I choose the second option since it is helpful to have a reference to the length of the operands for formatting reasons.

  ```py
  length_1 = len(str(operand_1))
  length_2 = len(str(operand_2))
  length_max = length_1 > length_2 and length_1 or length_2
  ```

  For the error message check if `length_max` exceeds the desired threshold.

  ```py
  if length_max > 4:
    return "Error: Numbers cannot be more than four digits."
  ```

For formatting reasons it is helpful to build a list describing the problems in their building blocks: operands, operator and even the length of the greater number. The data structure helps to then populate a string where successive problems are side by side.
