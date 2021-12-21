# probability-calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

- [Work-in-progress](https://replit.com/@borntofrappe/boilerplate-probability-calculator)

## Preface

The assignment asks to estimate the probability of drawing a sequence of balls from a hat by running a series of experiments.

## Solution

The assignment is made up of two parts: a `Hat` class and an `experiment` function.

### Hat

Each instance of the class is instantiated with a variable number of arguments which specify the number of balls of each color.

For instance:

```py
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```

The arguments in the form `key=value` are known as _keyword arguments_, one of the two types documented in the glossary explaining [arguments](https://docs.python.org/3/glossary.html#term-argument). Always in the glossary the section devoted [to parameters](https://docs.python.org/3/glossary.html#term-parameter) explains how to receive the value of a variable number of inputs.

```py
def call(**kwargs):
  print(kwargs)

call(red=5, blue=1)
call(yellow=3, blue=2, green=6)
```

The arguments are collected in a dictionary.

```py
def call(**kwargs):
  for key, value in kwargs.items():
    print(key, value)

call(red=5, blue=1)
# red 5
# blue 1
```

Past the trivial example have the hat class receive the keyword arguments in the `__init__` function.

```py
def __init__(self, **kwargs):
```

Based on the arguments create a `contents` instance variable as a list containing one item for each ball.

```py
contents = []
```

As per the assignment each item in the list should represent a single ball of the given color.

Start by cycling through the colors:

```py
for color, number in kwargs.items():
```

Then create an additional loop to append as many colors as described by the number:

```py
for _ in range(number):
  contents.append(color)
```

After the loops store the list in `self.contents`. The list is then populated with as many string for a color as described by the corresponding number.

```py
hat = Hat(red=2, blue=1)
print(hat.contents) # ['red', 'red', 'blue']
```

As per the assignment include an additional method `draw` which receives the number of balls to draw.

```py
def draw(self, n):
  balls = []
```

The method extracts balls from `self.content` and at random, to ultimately return a list of strings. Of note:

> The balls should not go back into the hat during the draw

To pick a ball at random it's possible to rely on one of the two imported modules: `random`

```py
import random
```

With the module, and for as many times as dictated by the input number, pick an index up to the length of the `contents` list.

```py
for _ in range(n):
  index = random.randint(0, len(self.contents) - 1)
```

To remove the ball from the list the `.pop` function removes the item at the chosen index.

```py
balls.append(self.contents.pop(index))
```

Past the for loop, `balls` contains the desired list of strings.

```py
return balls
```

The assignment asks to consider a specific edge case when the number of balls exceeds the number available in `self.contents`. To this end check the length of the `contents` list before the drawing operation.

```py
if n >= len(self.contents):
  return self.contents
```

### experiment

The second part of the assignment. asks to create an `experiment` function which accepts several arguments:

- `hat`: an instance of the `Hat` class

- `expected_balls`: a dictionary describing the exact group of balls to attempt to draw for the experiment

  `{"blue":2, "red":1}` would indicate two blue balls, one red ball

- `num_balls_drawn`: the number of balls to draw in each experiment

- `num_experiments`: the number of experiments to perform

```py
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # ...
```

Based on the input arguments the function computes a probability with an empirical approach:

> perform `N` experiments, count how many times `M` we get at the desired number of balls, estimate the probability as `M/N`

In the body of the function set up a loop to go through the prescribed number of experiments.

```py
for _ in range(num_experiments):
```

In the experiment draw balls from the input hat.

```py
balls = hat.draw(num_balls_drawn)
```

The methods modify the contents of the hat, so there at least two solutions to this issue, thanks to the second of the two imported modules: `copy`.

First solution: modify the `draw` methods to create a copy of the contents and extract the balls from the separate list.

```py
def draw(self, n):
  contents = copy.copy(self.contents)
```

Second solution: create a deep copy of the hat in the experiment function.

```py
balls = copy.deepcopy(hat).draw(num_balls_drawn)
```

The two approaches are equivalent, but it seems the assignment asks for the `draw` method to actually mutate the `contents` list. To pass every test create a deep copy of the object.

With the drawn balls continue the experiment by comparing the list against `expected_balls`. Since the input argument is a dictionary one possible way to iterate through its contents is with the `items()` function, which returns a list of tuples.

```py
for color, number in expected_balls.items():
```

For the purposes of the assignment, initialize a boolean to describe if the draw is successful.

```py
has_expected_balls = True
```

Update the boolean to `False` when:

1. the `balls` list does not contain a color from `expected_balls`

   ```py
   if color not in balls:
     has_expected_balls = False
   ```

2. the `balls` list includes the color, but in a smaller number

   ```py
   if color not in balls or number > balls.count(color):
     has_expected_balls = False
   ```

   The feature is implemented with the `.count` method available on list objects.

Since the first time the code is executed is enough for the experiment to fail use a `break` statement to stop cycling through the list of tuples.

```py
has_expected_balls = False
break
```

Outside of the loop `has_expected_balls` is either `False`, as per the `if` statement, or has remained `True`, as per the initial value. If `True` increment a counter variable keeping track of the number of successful draws.

```py
if has_expected_balls:
  num_experiments_success = num_experiments_success + 1
```

Past the loop setting up the experiment use the value to compute the final estimation.

```py
return num_experiments_success / num_experiments
```
