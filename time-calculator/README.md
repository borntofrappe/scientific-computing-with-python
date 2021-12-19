# [time-calculator](https://replit.com/@borntofrappe/boilerplate-time-calculator)

## Preface

[The assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator) asks to create a function to describe the gap between two dates.

In terms of **input** the function receives three arguments:

1. a start time in the 12-hour clock format

2. a duration in hour and minutes

3. an optional starting day of the week

In terms of **output** the function returns a string adding the duration to the start time. After the end time in the 12-hour clock format the should include additional information following strict rules:

- the day if passed as third argument

- `(next day)` if the date falls on the following day

- `(x days later)` for any following day
