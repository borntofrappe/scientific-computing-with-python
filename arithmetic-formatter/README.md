# [arithmetic-formatter](https://replit.com/@borntofrappe/boilerplate-arithmetic-formatter)

[The assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter) asks to create a function to format arithmetic problems with a specific set of rules.

## Input

A list of strings and an optional boolean.

```py
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```

## Output

A string highlighting an error message in the following instances:

- there are more than five projects: `Error: Too many problems.`

- the operators describe multiplication or division: `Error: Operator must be '+' or '-'.`

- the operands contain non-digit characters: `Error: Numbers must only contain digits.`

- the operands have more than four digits: `Error: Numbers cannot be more than four digits.`

Outside of these cases, a string arranging the problems vertically and side by side. The problems should be solved only if the second argument resolves to `True`.

```text
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Formatting rules:

- a single space between operator and the longest of the two operands

- operator on the same line as the second operand

- operand in the order provided by the function

- numbers right aligned

- four spaces between successive problems

- dashes below the problems covering the space of each problem
