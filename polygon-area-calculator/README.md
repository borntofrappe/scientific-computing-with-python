# polygon-area-calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)

- [Solution](https://replit.com/@borntofrappe/boilerplate-polygon-area-calculator)

## Preface

The assignment focuses on object oriented programming with two classes: `Rectangle` and `Square`.

## Solution

### Rectangle

The class should be initialized with `width` and `height`.

```py
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

When displayed the class should highlight the width and height.

```py
def __str__(self):
  return f'Rectangle(width={self.width},height={self.height})'
```

In terms of methods the class should have:

- `set_width` and `_set_height` as setter methods, updating the width and height respective

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

The width should instruct the columns, the height the rows.

If the width or height exceed an arbitrary threshold, 50, the function should return "Too big for picture.".

TODO >>>

For `get_amount_inside` the idea is to receive a rectangle or a square as argument and return the number of times the input shape would fit in the object.

<<<

#### Square

The Square class should be a subclass of Rectangle.

```py
class Square(Rectangle):
```

In the initialization function the class should receive a single value, the length of the side, and use the value for both the width and height. [The docs](https://docs.python.org/3/library/functions.html#super) instruct to use `super()` to call the parent class.

```py
def __init__(self, side):
  super().__init__(side, side)
```

When printed, the class should override the message set for the rectangle and aptly describe the square and its side.

```py
def __str__(self):
  return f'Square(side={self.width})'
```

In terms of methods, beyond the ones inherited from the rectangle class, the square should have `set_side`, modifying both the width and height.

`set_width` and `set_height` methods should override both the width and height.
