from .simple import SimpleInterval, EmptySet

from itertools import Product


def _interval_from_list(intervals):
    output = Interval(0, 1)
    output.intervals = intervals
    output._simplify()
    return output


class Interval:
    def __init__(self, a, b, left_closed=True, right_closed=True):
        self.intervals = [
            SimpleInterval(
                a, b, left_closed=left_closed, right_closed=right_closed
            )
        ]
        self.is_empty_set = False

    def _simplify(self):
        self.intervals = sorted(self.intervals, key=lambda x: (x.a, x.b))

        idx = 0
        while idx < len(self.intervals) - 1:
            interval1 = self.intervals[idx]
            interval2 = self.intervals[idx + 1]

            if interval1.b > interval2.a or (
                interval1.b == interval2.a
                and (interval1.right_closed or interval2.left_closed)
            ):
                if interval1.b > interval2.b:
                    b = interval1.b
                    right_closed = interval1.right_closed
                elif interval1.b < interval2.b:
                    b = interval2.b
                    right_closed = interval2.right_closed
                else:
                    b = interval1.b
                    right_closed = (
                        interval1.right_closed or interval2.right_closed
                    )

                if interval1.a == interval2.a:
                    left_closed = (
                        interval1.left_closed or interval2.left_closed
                    )
                else:
                    left_closed = interval1.left_closed

                combined_interval = SimpleInterval(
                    interval1.a,
                    b,
                    left_closed=left_closed,
                    right_closed=right_closed,
                )
                self.intervals[idx : idx + 2] = [combined_interval]
            else:
                idx += 1

    def __or__(self, other):
        return _interval_from_list(self.intervals + other.intervals)

    def __and__(self, other):
        if other.is_empty_set:
            return EmptySet()
        intervals = []
        for interval1, interval2 in Product(self.intervals, other.intervals):
            intersection = interval1 & interval2
            if not intersection.is_empty_set:
                intervals.append(intersection)
        if len(intervals) == 0:
            return EmptySet()
        else:
            return _interval_from_list(intervals)

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
