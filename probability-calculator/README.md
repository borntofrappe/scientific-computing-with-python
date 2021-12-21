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

---

Next, create an `experiment` function in `prob_calculator.py` (not inside the `Hat` class). This function should accept the following arguments:

- `hat`: A hat object containing balls that should be copied inside the function.
- `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat for the experiment. For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set `expected_balls` to `{"blue":2, "red":1}`.
- `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
- `num_experiments`: The number of experiments to perform. (The more experiments performed, the more accurate the approximate probability will be.)

The `experiment` function should return a probability.

For example, let's say that you want to determine the probability of getting at least 2 red balls and 1 green ball when you draw 5 balls from a hat containing 6 black, 4 red, and 3 green. To do this, we perform `N` experiments, count how many times `M` we get at least 2 red balls and 1 green ball, and estimate the probability as `M/N`. Each experiment consists of starting with a hat containing the specified balls, drawing a number of balls, and checking if we got the balls we were attempting to draw.

Here is how you would call the `experiment` function based on the example above with 2000 experiments:

```
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
```

Since this is based on random draws, the probability will be slightly different each time the code is run.

_Hint: Consider using the modules that are already imported at the top of `prob_calculator.py`. Do not initialize random seed within `prob_calculator.py`._
