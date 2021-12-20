# budget-app

## Links

[Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)

[Solution](https://replit.com/@borntofrappe/boilerplate-budget-app)

## Preface

The assignment asks to complete a `Category` class and a `create_spend_chart` function with specific instructions.

## Solution

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

- a `deposit` method that accepts an amount and description

  The method should append an object to the ledger list in the form of `{"amount": amount, "description": description}`, and I presume the assignment asks for a dictionary

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
  has_enough_funds = self.check_funds()
```

A similar logic can be applied to `check_funds`, in order to retrieve the balance from the `get_balance` method, and to `transfer`, in order to withdraw and deposit with the respective functions.

---

When the budget object is printed it should display:

- A title line of 30 characters where the name of the category is centered in a line of `*` characters.
- A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
- A line displaying the category total.

Here is an example of the output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

Besides the `Category` class, create a function (outside of the class) called `create_spend_chart` that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category".

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.

```
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
