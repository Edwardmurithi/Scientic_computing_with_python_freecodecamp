#!/usr/bin/python3

def add_time(start, duration, starting_day=None):
    # Split the start time into components
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    
    # Convert start time to 24-hour format
    if period == 'PM' and start_hours != 12:
        start_hours += 12
    elif period == 'AM' and start_hours == 12:
        start_hours = 0

    # Split the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate the new time
    end_minutes = start_minutes + duration_minutes
    end_hours = start_hours + duration_hours + (end_minutes // 60)
    end_minutes = end_minutes % 60
    days_later = end_hours // 24
    end_hours = end_hours % 24

    # Convert back to 12-hour format
    if end_hours == 0:
        period = 'AM'
        end_hours = 12
    elif end_hours < 12:
        period = 'AM'
    elif end_hours == 12:
        period = 'PM'
    else:
        period = 'PM'
        end_hours -= 12

    # Calculate the day of the week if starting_day is provided
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        end_day_index = (starting_day_index + days_later) % 7
        end_day = days_of_week[end_day_index]
        result = f"{end_hours}:{end_minutes:02d} {period}, {end_day}"
    else:
        result = f"{end_hours}:{end_minutes:02d} {period}"

    # Append the days later information if necessary
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result
