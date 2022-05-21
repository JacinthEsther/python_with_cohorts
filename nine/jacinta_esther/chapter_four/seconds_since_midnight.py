def seconds_since_midnight(hour, minutes, seconds):
    hour_in_seconds = 3600 * hour
    minute_in_seconds = 60 * minutes
    return hour_in_seconds + minute_in_seconds + seconds


print(seconds_since_midnight(13, 30, 45))
