# time-calculator

## Links

[Assignment](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)

[Solution](https://replit.com/@borntofrappe/boilerplate-time-calculator)

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

Begin by extracting the relevant information from the arguments:

- break the string describing the start into hour, minutes and meridian

  This is achieved with two `split` functions, first separating the string by space, isolating the time and meridian, then separating the time by colon.

  ```py
  start_date = start.split()
  start_time = start_date[0].split(':')
  ```

- break the string describing the duration into hour and minutes

The optional day is considered later.

With the hour and minutes the first step is to add the start and duration values.

```py
end_hour = start_hour + duration_hour
end_minutes = start_minutes + duration_minutes
```

If the minutes exceed 60, the excess is added to the hours.

```py
if end_minutes >= 60:
  end_hour = end_hour + int(end_minutes / 60)
  end_minutes = end_minutes % 60
```

If the hours exceed 12 it is also necessary to consider the meridian, so begin by initializing a string to the start value.

```py
end_meridian = start_meridian
```

If the excess over 12 is odd, half a day, a day and a half and so forth, flip the meridian to the opposite value.

```py
if int(end_hour / 12) % 2 != 0:
  end_meridian = end_meridian == 'PM' and 'AM' or 'PM'
```

Past this check, round the hours to the 12 clock format. Due to the specificities of the assignment, however, display 12 instead of 0.

```py
end_hour = end_hour % 12
if end_hour == 0:
  end_hour = end_hour + 12
```

For the day and the number of days begin by computing the number of days due to the duration.

```py
day_excess = int(duration_hour / 24)
```

There is however a special case where an excess of less than 24 hours describes a day, and that is when the day goes from PM to AM.

```py
if start_meridian == 'PM' and end_meridian == 'AM':
    day_excess = day_excess + 1
```

Based on this information consider the optional day.

```py
day_suffix = ''
  if day:
    # consider excess
```

`day_suffix` is initialized with an empty string so that it's possible to append the variable without an additional conditional.

Since the day is case insensitive start by dedicating a variable in lowercase notation.

```py
start_day = day.lower()
```

From a hard-coded list describing the days then, find the index of the start day.

```py
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

day_index = -1
for index in range(len(days)):
  if days[index] == start_day:
    day_index = index
    break
```

`range` builds a list from 0 up to 7, 7 not included.

Finding the end day is then a matter of adding the excess to this index _and_ rounding the value to the length of the list.

```py
end_day = days[(day_index + day_excess) % len(days)]
```

With the day, and following the requirement of the assignment, create the suffix with a colon and the capitalized day.

```py
day_suffix = ', ' + end_day[0].upper() + end_day[1:]
```

For the final part of the string, the excess number of days, the logic is similar to the day: create a dedicated variable.

If the excess is greater than a day add the desired labels:

- next day for an excess of 1

- x days later for greater values

The final string concatenates all the values for the end hour, minutes, meridian and suffixes.

## Update

From the Python docs I discovered [formatted string literals](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings), a feature makes concatenating strings more clear.

```diff
-day_fufix = ', ' + end_day[0].upper() + end_day[1:]
+day_suffix = f', {end_day[0].upper()}{end_day[1:]}'
```

I find it definitely easier to read, at least. The difference becomes more noticeable when adding whitespace characters, or again the colon separating the hour and minutes.
