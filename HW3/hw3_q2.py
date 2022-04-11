class Time:
    """
    Represents the time of the day.
    Attributes: hour, minute, second
    """

    @staticmethod
    def valid_time_part(part, max_value):
        return 0 if type(part) != int or part not in range(max_value) else part

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = self.valid_time_part(hour, 24)
        self.minute = self.valid_time_part(minute, 60)
        self.second = self.valid_time_part(second, 60)

    def is_after(self, other):
        """Checks if time is after other time and returns bool"""
        if self.hour != other.hour:
            return self.hour > other.hour

        if self.minute != other.minute:
            return self.minute > other.minute

        return self.second > other.second

    def __add__(self, other):
        total_hours = self.hour + other.hour
        total_minutes = self.minute + other.minute
        total_seconds = self.second + other.second

        if total_seconds >= 60:
            total_seconds %= 60
            total_minutes += 1

        if total_minutes >= 60:
            total_minutes %= 60
            total_hours += 1

        total_hours %= 24

        return Time(hour=total_hours, minute=total_minutes, second=total_seconds)

    def __str__(self):
        return f"<{self.hour:02d}:{self.minute:02d}:{self.second:02d}>"