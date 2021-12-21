# probability-calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

- [Work-in-progress](https://replit.com/@borntofrappe/boilerplate-probability-calculator)

## Preface

The assignment asks to estimate the probability of drawing a sequence of balls from a hat by running a series of experiments.

## Solution

> Create a `Hat` class in `prob_calculator.py`

> Each instance of the class is instantiated with a variable number of arguments that specify the number of balls of each color.

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

> A hat will always be created with at least one ball.

> In the `__init__` function create a `contents` instance variable as a list containing one item for each ball. Each item in the list should represent a single ball of the given color.
>
> For instance, the hat `{"red": 2, "blue": 1}` creates a `contents` lists `["red", "red", "blue"]`

To implement the feature first cycle through the colors:

```py
for color, number in kwargs.items():
```

Then create an additional loop to append as many colors as described by the number:

```py
for _ in range(number):
  contents.append(color)
```

> The `Hat` class should have a `draw` method which accepts an argument indicating the number of balls to draw

```py
 def draw(self, n):
   balls = []
```

> The method should remove balls at random from `contents` and return those balls as a list of strings
>
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

> If the number of balls exceeds the available quantity return all the balls

Check the length of the `contents` list before the drawing operation.

```py
if n >= len(self.contents):
  return self.contents
```

> Create an `experiment` function which accepts as arguments:

- `hat`: a hat object

- `expected_balls`: an object indicating the exact group of balls to attempt to draw for the experiment.

  For example `{"blue":2, "red":1}` indicates two blue balls, one red ball

- `num_balls_drawn`: the number of balls to draw in each experiment

- `num_experiments`: the number of experiments to perform

```py
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  # ...
```

> The `experiment` function should return a probability
>
> perform `N` experiments, count how many times `M` we get at the desired number of balls, estimate the probability as `M/N`

- [copy module](https://docs.python.org/3/library/copy.html)

- [list.count(x)](https://docs.python.org/3/tutorial/datastructures.html)

```py
def draw(self, n):
    contents = copy.copy(self.contents)
    if n >= len(contents):
        return contents

    balls = []
    for _ in range(n):
        index = random.randint(0, len(contents) - 1)
        balls.append(contents.pop(index))

    return balls

# later
balls = hat.draw(num_balls_drawn)
```

```py
def draw(self, n):
    if n >= len(self.contents):
        return self.contents

    balls = []
    for _ in range(n):
        index = random.randint(0, len(self.contents) - 1)
        balls.append(self.contents.pop(index))

    return balls

# later
balls = copy.deepcopy(hat).draw(num_balls_drawn)
```
