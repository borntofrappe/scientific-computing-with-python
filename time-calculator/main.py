def add_time(start, duration, day=""):
    start_date = start.split()
    start_time = start_date[0].split(':')
    start_hour = int(start_time[0])
    start_minutes = int(start_time[1])
    start_meridian = start_date[1]

    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_minutes = int(duration_time[1])

    end_hour = start_hour + duration_hour
    end_minutes = start_minutes + duration_minutes
    if end_minutes >= 60:
        end_hour = end_hour + int(end_minutes / 60)
        end_minutes = end_minutes % 60

    end_meridian = start_meridian
    if end_hour >= 12:
        if int(end_hour / 12) % 2 != 0:
            end_meridian = end_meridian == 'PM' and 'AM' or 'PM'
        end_hour = end_hour % 12
        if end_hour == 0:
            end_hour = end_hour + 12

    day_excess = int(duration_hour / 24)
    if start_meridian == 'PM' and end_meridian == 'AM':
        day_excess = day_excess + 1

    day_suffix = ''
    if day:
        start_day = day.lower()
        days = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        day_index = -1
        for index in range(len(days)):
            if days[index] == start_day:
                day_index = index
                break

        end_day = days[(day_index + day_excess) % len(days)]

        day_suffix = f', {end_day[0].upper()}{end_day[1:]}'

    excess_suffix = ''
    if day_excess > 0:
        if day_excess == 1:
            excess_suffix = ' (next day)'
        else:
            excess_suffix = f' ({str(day_excess)} days later)'

    end = f'{str(end_hour)}:{str(end_minutes).rjust(2, "0")} {end_meridian}{day_suffix}{excess_suffix}'

    return end


print(add_time("3:00 AM", "24:00", 'saturday'))
print()
print(add_time("11:30 AM", "2:32", "Monday"))
print()
print(add_time("11:43 AM", "00:20"))
print()
print(add_time("10:10 PM", "3:30"))
print()
print(add_time("11:43 PM", "24:20", "tueSday"))
print()
print(add_time("6:30 PM", "205:12"))
print()
