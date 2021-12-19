# [time-calculator](https://replit.com/@borntofrappe/boilerplate-time-calculator)

## Preface

[The assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator) asks to create a function to compute a deadline with a start data and a lapse in time.

In terms of **input** the function receives three arguments:

1. a start time in the 12-hour clock format. The string includes the AM, PM suffix

2. a duration in hour and minutes. Hour can describe any whole number, while minutes is ensured to be a number less than 60

3. an optional starting day of the week. The string is case insensitive

```py
add_time("3:00 PM", "3:10")
add_time("11:43 PM", "24:20", "tueSday")
```

In terms of **output** the function returns a string adding the lapse to the start date, with the same 12-hour clock format of the input date. Following the hour and minutes the string should include additional information with strict rules:

- the day if passed as third argument, capitalized

- `(next day)` if the date falls on the following day

- `(x days later)` for any day exceeding the next one

```text
6:10 PM
12:03 AM, Thursday (2 days later)
```

## Solution
