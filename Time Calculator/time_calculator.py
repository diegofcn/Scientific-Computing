days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def add_time(start, duration, *args):
    [time, ending] = start.split(" ")
    [start_h, start_m] = time.split(":")
    [duration_h, duration_m] = duration.split(":")

    total_minutes = int(start_m) + int(duration_m)
    total_hours = int(start_h) + int(duration_h)
    future_days = 0

    if total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1
    if total_minutes < 10:
        total_minutes = f"{total_minutes}".zfill(2)

    if total_hours >= 12:
        t, r = divmod(total_hours, 12)
        total_hours = r if r else total_hours
        if total_hours > 12:
            total_hours = total_hours - ((t - 1) * 12)

        if ending == 'PM':
            future_days = ((t - 1) // 2) + 1
        else:
            future_days = t // 2

        if t > 0 and t % 2 != 0:
            ending = 'AM' if ending == 'PM' else 'PM'

    new_time = str(total_hours) + ":"
    new_time += str(total_minutes) + f" {ending}"

    if args:
        day = args[0].title()
        if future_days > 0:
            index = days.index(day)
            index += future_days % 7
            if index > 6:
                index = index - 7
            day = days[index]

        new_time += f", {day}"

    if future_days == 1:
        new_time += " (next day)"
    elif future_days > 1:
        new_time += f" ({future_days} days later)".rjust(11)

    return new_time
