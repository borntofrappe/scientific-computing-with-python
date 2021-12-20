# budget-app

## Links

[Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)

[Solution](https://replit.com/@borntofrappe/boilerplate-budget-app)

## Preface

The assignment asks to complete a `Category` class and a `create_spend_chart` function with specific instructions.

## Solution

### Class

Following the project's `README.md` the class should have:

- an instance variable called `ledger`

  [The python docs](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables) describe an instance variable as unique to each instance of the class, declared in the `__init__` function. This is opposed to class variables, shared by all instances and initialized outside of the method.

  ```py
  def __init__(self):
      self.ledger = []
  ```

  Since the importing script initializes the categories with a name the method stores the value as well.

  ```py
  def __init__(self, name):
      self.name = name
  ```

- a `deposit` method that accepts an amount and an optional description

  The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`. I presume the assignment asks for a dictionary.

  ```py
  self.ledger.append({
      'amount': amount,
      'description': description,
  })
  ```

- a `withdraw` method that is similar to the `deposit` method, but should store the amount as a negative number

  ```py
  self.ledger.append({
      'amount': amount * -1,
      'description': description,
  })
  ```

  The operation is conditioned to the presence of sufficient funds.

  ```py
  funds = 0
  for operation in self.ledger:
      funds = funds + operation['amount']

  if funds >= amount:
    # operation
  ```

  The method also returns `True` or `False` depending on whether or not the withdrawal took place.

  ```py
  has_enough_funds = funds >= amount

  # operation

  return has_enough_funds
  ```

- a `get_balance` method that returns the current balance

  The method repeats the logic for the withdrawal. Out of preference `funds` is renamed to `balance`

- a `transfer` method that accepts an amount and another budget category

  ```py
  def transfer(self, amount, category):
  ```

  The method withdraws funds from the current class and deposits a matching value in the input class, with a precise description for both operations

  ```py
  self.ledger.append({
    'amount': amount * -1,
    'description': f"Transfer to {category.name}",
  })

  category.ledger.append({
    'amount': amount,
    'description': f"Transfer from {self.name}",
  })
  ```

  Once again the method checks for the presence of sufficient funds and returns a boolean if the transfer took place

- a `check_funds` method that accepts an amount as an argument

  The function returns a boolean describing whether or not the balance is greater than the amount.

With the last method the assignment suggests the use of `check_funds` in the withdraw and transfer methods. It is therefore possible to refactor the code accordingly.

```py
def withdraw(self, amount, description=""):
  has_enough_funds = self.check_funds(amount)
```

A similar refactor happens to `check_funds`, to retrieve the balance with the `get_balance` method, and to `transfer`, to perform the operations with `self.withdraw` and `category.deposit`.

### str

The assignment asks to display a specific string through the `print` function. This is in place of the default string detailing the name of the object.

```py
food = Category('Food')
print(food)
# <__main__.Category object>
```

Following [the python docs](https://docs.python.org/3/reference/datamodel.html#object.__str__) the output is customized with the `__str__` method.

```py
class Category:
  def __str__(self):
    return self.name
```

The assignment asks to produce a string specifying:

- a title line of 30 characters where the name of the category is centered in `*` characters

  ```py
  output = self.name.center(30, '*')
  ```

- a line for each operation in the ledger

  The line displays the description for the first 23 characters

  ```py
  f'{operation["description"][:23].ljust(23)}'
  ```

  The remaining 7 characters are dedicated to the amount, with two decimal places and right aligned.

  The alignment mirrors that of the description.

  ```py
  f'{str(operation["amount"])[:7].rjust(7)}'
  ```

  For the decimal places [the docs](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals) provide a solution in using a specific directive: `:.2f`.

  ```py
  amount = f'{str(operation["amount"]):.2f}'
  ```

  I prefer to first create the decimal version and then align the value in the output string, but the logic remains the same.

  The entire line is appended to the output string with an additional new line character.

  ```py
  output = f'{output}...\n'
  ```

  The output itself is however updated _before_ the ledger loop to add a new line character between title and operations.

  ```py
  output = f'{self.name.center(30, "*")}\n'
  ```

- a line displaying the total

  ```py
  output = f'{output}Total: {self.get_balance()}'
  ```

  There's no need to add a new line character to separate the total, since it's already included in the last iteration of the for loop

With this setup the operations:

```py
food = Category('Food')
clothing = Category('Clothing')
food.deposit(1000, 'Initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food items')
food.transfer(50, clothing)
print(food)
```

Produce the following sequence of characters:

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

### Function

The second part of the assignment asks to create a function which takes a list of categories as an argument and returns a string representing a rudimentary bar chart.

```text
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
```

In terms of content the string should:

- begin with the title 'Percentage spent by category'

- display percentage points on the left side: 100, 90 and so forth in decrements of 10

- separate the percentage points from the data with a pipe character `|`

- display the percentage spent in each category with the letter `o`. Each category should spread over three spaces and the value should be centered

- separate the percentage spent from the name of the categories with dash characters `-`. There should be one more dash than there are for the columns

- display the name of the category vertically and below the respective `o` character

I split the logic of the function in two parts:

- creating data structures to describe percentages and names

- format the information of the data structure following the requirements of the assignment

For the data structures, the percentages need to describe the value spent in the category relative to the value spent in _all_ categories. Looping through the categories `amounts` keeps track of the individual expenditures, `total_amount` keeps track of the total.

```py
amounts.append(amount)
total_amount = total_amount + amount
```

After the loop, it's possible to loop through the amounts to compute the percentages. The information is rounded down to an integer and stored in another list.

```py
percentage = int(amount / total_amount * 100)
percentages.append(percentage)
```

Past the percentages, `names` and `max_length` name are defined to keep track of the list of names and the length of the longest string. The length is necessary to ensure that there are enough rows at the bottom of the bar chart.

The information is extracted in the same loop used for the amounts, cycling through the categories.

```py
names.append(name)
length_name = len(name)
if length_name > max_length_name:
    max_length_name = length_name
```

With this setup the biggest challenge is in terms of spacing. The assignment asks to include a space after each category, padding in other words. The extra character is to ensure that each row is long as the dashed line, beginning four characters in and ending one character past the category.

In trying to find a clean solution I decided to describe the width of the different parts of the chart with a series of variables.

```py
percentage_width = 3
pipe_width = 1
category_width = 3
categories_width = category_width * len(categories)
padding_width = 1
```

The idea is to use the variables with the `rjust`, `ljust` and `center` functions to achieve the desired alignment. For instance, the percentages are right-aligned to occupy three characters, the pipe is left-aligned in the only space dedicated to it. It's unnecessary to align the pipe, but this makes for a more flexible solution where you could add a space between the pipe and the rest of the chart.

The rows center the characters for the categories, the `o` for the percentage and the letter for the name, in three spaces. Moreover, each row dedicates one space for the padding.

For the dashes add as many characters as described by the categories plus the padding. Align the string to follow the percentages and pipe.

Note that the output string has one superfluous new line character

```py
return output[:-1]
```

It's not possible to rely on `rstrip` since the function would also remove the padding.
