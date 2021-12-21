import random


class Hat:
    def __init__(self, **kwargs):
        contents = []
        for color, number in kwargs.items():
            for _ in range(number):
                contents.append(color)

        self.contents = contents

    def draw(self, n):
        if n >= len(self.contents):
            return self.contents

        balls = []
        for _ in range(n):
            index = random.randint(0, len(self.contents) - 1)
            balls.append(self.contents.pop(index))

        return balls


hat = Hat(red=5, blue=3, green=2)
print(hat.draw(10))
