from simple import SimpleInterval


def _interval_from_list(intervals):
    output = SimpleInterval(0, 1)
    output.intervals = intervals
    return output._simplify()


class Interval:
    def __init__(self, a, b, left_closed=True, right_closed=True):
        self.intervals = [
            SimpleInterval(
                a, b, left_closed=left_closed, right_closed=right_closed
            )
        ]

    def _simplify(self):
        self.intervals = sorted(self.intervals)

        idx = 0
        while idx < len(self.intervals) - 1:
            interval1 = self.intervals[idx]
            interval2 = self.intervals[idx + 1]

            if interval1.b > interval2.a or (
                interval1.b == interval2.a
                and not (interval1.right_open and interval2.left_open)
            ):
                if interval1.b > interval2.b:
                    b = interval1.b
                    right_open = interval1.right_open
                elif interval1.b < interval2.b:
                    b = interval2.b
                    right_open = interval2.right_open
                else:
                    pass

                # TODO

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
