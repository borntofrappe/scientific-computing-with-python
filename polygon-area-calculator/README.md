# polygon-area-calculator

## Links

- [Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)

- [Solution](https://replit.com/@borntofrappe/boilerplate-polygon-area-calculator)

## Preface

The assignment focuses on object oriented programming with two classes: `Rectangle` and `Square`.

## Solution

The Square class should be a subclass of Rectangle.

```py
class Rectangle:

class Square(Rectangle):
```

The rectangle class should be initialized with `width` and `height`.

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

#### Square class

The Square class should be a subclass of Rectangle. When a Square object is created, a single side length is passed in. The `__init__` method should store the side length in both the `width` and `height` attributes from the Rectangle class.

The Square class should be able to access the Rectangle class methods but should also contain a `set_side` method. If an instance of a Square is represented as a string, it should look like: `Square(side=9)`

Additionally, the `set_width` and `set_height` methods on the Square class should set both the width and height.

#### Usage example

```py
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
```

That code should return:

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```
