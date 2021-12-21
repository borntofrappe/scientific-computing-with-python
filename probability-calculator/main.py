import random
import copy


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


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_experiments_success = 0

    for _ in range(num_experiments):
        balls = copy.deepcopy(hat).draw(num_balls_drawn)

        has_expected_balls = True

        for color, number in expected_balls.items():
            if color not in balls or number > balls.count(color):
                has_expected_balls = False
                break

        if has_expected_balls:
            num_experiments_success = num_experiments_success + 1

    return num_experiments_success / num_experiments


hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
