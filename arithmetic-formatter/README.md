# arithmetic-formatter

## Links

- [Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)

- [Solution](https://replit.com/@borntofrappe/boilerplate-arithmetic-formatter)

## Preface

[The assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter) asks to create a function to format arithmetic problems following specific rules.

In terms of **input** the function receives a list of strings and an optional boolean.

```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```

In terms of **output** the function returns a string highlighting an error message in the following instances:

- there are more than five projects

- the operators describe multiplication or division

- the operands contain non-digit characters

- the operands have more than four digits

Outside of these instances, the **output** is a string arranging the problems vertically and side by side. The problems should be solved only if the second argument resolves to `True`.

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
    expression = problem.split()
    operator = expression[1]
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
  operand_1 = expression[0]
  operand_2 = expression[2]

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

Past the error messages, the output string needs to place the problems side by side. For this reason it is helpful to build a list describing the problems in their building blocks: operands, operator and even the length of the greater number. The data structure helps to then populate a string where successive problems are side by side.

Initialize a list in which to store the operations.

```py
operations = list()
```

In the for loop create a dictionary for the individual operation, populating the data structure with the relevant information.

```py
operation = dict()
operation['operand_1'] = operand_1
operation['operand_2'] = operand_2
operation['operator'] = operator
operation['width'] = width
```

`width` describes the maximum value of the length incremented by 2, to accommodate the space between operator and operand and the operator itself.

Considering the boolean `solved` the dictionary also includes the solution, adding or subtracting depending on the operator.

```py
solution = operator == '+' and operand_1 + operand_2 or operand_1 - operand_2
operation['solution'] = solution
```

Outside of the for loop `operations` contains one dictionary for each operation. To create the side by side effect, initialize `lines` as a list of three, or four, strings. Four strings to make space for the optional solution.

```py
lines = ['', '', '']
if solved:
    lines.append('')
```

The idea is to then loop through the operations and populate the different lines with the desired information:

- on the first line add the first operand

  ```py
  lines[0] = lines[0] + str(operation['operand_1'])
  ```

  To align the string use `.rjust()` function with the operation's width.

  ```py
  lines[0] = lines[0] + str(operation['operand_1']).rjust(width)
  ```

- on the second line add the operator, a space, and the second operand

  Since the space and operator occupy two characters it is necessary to decrement the width accordingly

  ```py
  lines[1] = lines[1] + operation['operator'] + ' ' + str(operation['operand_2']).rjust(width - 2)
  ```

- on the third line add as many dash characters as described by the width

  ```py
  lines[2] = lines[2] + '-' * width
  ```

- on the optional fourth line add the solution, once more aligned with `rjust`

  ```py
  lines[3] = lines[3] + str(operation['solution']).rjust(width)
  ```

To separate successive problems append also as many spaces as required by the assignment. For instance and for the dashed line.

```py
lines[2] = lines[2] + '-' * width + ' ' * 4
```

Since every line appends the spaces I preferred to store the value in a separate variable, but the logic remains the same.

```py
spaces = ' ' * 4
lines[2] = lines[2] + '-' * width + spaces
```

Past the loop `lines` includes the problems in multiple strings. There is an excess of whitespace as even the last iteration includes the spaces, but it's possible to strip the value with `rstrip`.

Initialize `arranged_problems` as an empty string, loop through the lines and append each line followed by a new line character.

```py
arranged_problems = arranged_problems + line.rstrip() + '\n'
```

Finally, return the string stripping the last new line character.

```py
return arranged_problems.rstrip()
```

## Update

Previously I included the solution on the third line checking if the solution existed in the dictionary.

```py
if 'solution' in operation:
  # append to lines[3]
```

However, I prefer to rely on the same conditional used for computing the solution and adding the line.

```py
if solved:
  # append to lines[3]
```

Other than creating a connection of meaning the approach allows to provide a fallback when no key exist, even if not possible by design.

```py
# operation['solution']
str(operation.get('solution', ''))
```

In this manner a missing solution would not compromise successive problems.
