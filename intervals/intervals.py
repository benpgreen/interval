from simple import SimpleInterval


def _interval_from_list(intervals):
    output = SimpleInterval(0, 1)
    output.intervals = intervals
    return output._simplify()


class Interval:
    def __init__(self, a, b, left_open=False, right_open=False):
        self.intervals = [
            SimpleInterval(a, b, left_open=left_open, right_open=right_open)
        ]

    def _simplify(self):
        pass

    def __or__(self, other):
        return _interval_from_list(self.intervals + other.intervals)

    def size(self):
        return sum([interval.size() for interval in self.intervals])

    def __add__(self, number):
        return _interval_from_list(
            [interval + number for interval in self.intervals]
        )

    def __sub__(self, number):
        return _interval_from_list(
            [interval - number for interval in self.intervals]
        )

    def __mul__(self, number):
        return _interval_from_list(
            [interval * number for interval in self.intervals]
        )

    def __repr__(self):
        return " | ".join([interval.__repr__() for interval in self.intervals])
