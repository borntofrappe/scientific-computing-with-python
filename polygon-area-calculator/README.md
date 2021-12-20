# polygon-area-calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)

- [Solution](https://replit.com/@borntofrappe/boilerplate-polygon-area-calculator)

## Preface

The assignment focuses on object oriented programming with two classes: `Rectangle` and `Square`.

## Solution

### Rectangle

Initialize the class with a width and height.

```py
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
```

When printed highlight the dimensions in a specific format: `Rectangle(width=width, height=height)`.

```py
def __str__(self):
  return f'Rectangle(width={self.width}, height={self.height})'
```

In terms of methods define:

- `set_width` and `_set_height` as setter methods, updating the width and height respectively

- `get_area` returning the area of the rectangle

- `get_perimeter` returning the perimeter

- `get_diagonal` returning the diagonal

- `get_picture`

- `get_amount_inside`

For `get_picture` the idea is to return a string representing the shape with asterisk characters `*`.

```text
******
******
******
```

Use the width to describe the number of columns, the height the number of rows. End each row with a new line character `\n`.

```py
return f'{"*" * self.width}\n' * self.height
```

If the width or height exceed an arbitrary threshold, 50, return "Too big for picture.".

```py
if self.width > 50 or self.height > 50:
  return 'Too big for picture.'

# return f'...'
```

For `get_amount_inside` return how many times the input shape can fit in the object.

```py
def get_amount_inside(self, shape):
```

The number is computed considering the number of times can fit horizontally times the number of times vertically.

```py
return int(self.width / shape.width) * int(self.height / shape.height)
```

#### Square

Define the square class as a subclass of Rectangle.

```py
class Square(Rectangle):
```

In the initialization function the class use the single input value, the length of the side, for both the width and height.

[The docs](https://docs.python.org/3/library/functions.html#super) instruct to use `super()` to call the parent class.

```py
def __init__(self, side):
  super().__init__(side, side)
```

When printed, override the `__str__` function to describe the square and its side.

```py
def __str__(self):
  return f'Square(side={self.width})'
```

In terms of methods, beyond the ones inherited from the rectangle class, define `set_side` to modify both the width and height.

```py
def set_side(self, side):
  self.width = side
  self.height = side
```

Override `set_width` and `set_height` to update both width and height. Here it is possible to rely on `set_side` directly.

```py
def set_width(self, width):
  self.set_side(width)
```
