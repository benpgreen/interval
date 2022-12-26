from .validation import _validate_init_inputs, _check_is_number


class SimpleInterval:
    def __init__(self, a, b, left_closed=True, right_closed=True):
        _validate_init_inputs(a, b, left_closed, right_closed)
        self.a = a
        self.b = b
        self.left_closed = left_closed
        self.right_closed = right_closed
        self.is_empty_set = False

    def size(self):
        return self.b - self.a

    def __add__(self, number):
        _check_is_number(number)
        return SimpleInterval(
            self.a + number,
            self.b + number,
            left_closed=self.left_closed,
            right_closed=self.right_closed,
        )

    def __sub__(self, number):
        _check_is_number(number)
        return SimpleInterval(
            self.a - number,
            self.b - number,
            left_closed=self.left_closed,
            right_closed=self.right_closed,
        )

    def __mul__(self, number):
        _check_is_number(number)
        return SimpleInterval(
            self.a * number,
            self.b * number,
            left_closed=self.left_closed,
            right_closed=self.right_closed,
        )

    def __and__(self, other):
        if other.is_empty_set:
            return EmptySet()
        interval1, interval2 = sorted([self, other], key=lambda x: (x.a, x.b))
        if interval1.b > interval2.a:
            if interval1.b > interval2.b:
                b = interval2.b
                right_closed = interval2.right_closed
            elif interval1.b < interval2.b:
                b = interval1.b
                right_closed = interval1.right_closed
            else:
                b = interval1.b
                right_closed = (
                    interval1.right_closed and interval2.right_closed
                )

            if interval1.a == interval2.a:
                left_closed = interval1.left_closed and interval2.left_closed
            else:
                left_closed = interval2.left_closed
            return SimpleInterval(
                interval2.a,
                b,
                left_closed=left_closed,
                right_closed=right_closed,
            )
        elif interval1.b == interval2.a and (
            interval1.right_closed and interval2.left_closed
        ):
            return SimpleInterval(interval1.b, interval1.b)
        else:
            return EmptySet()

    def __repr__(self):
        left_brace = "[" if self.left_closed else "("
        right_brace = "]" if self.right_closed else ")"
        return f"{left_brace}{self.a}, {self.b}{right_brace}"


class EmptySet:
    def __init__(self):
        self.is_empty_set = True

    def size(self):
        return 0

    def __add__(self, number):
        _check_is_number(number)
        return EmptySet()

    def __sub__(self, number):
        _check_is_number(number)
        return EmptySet()

    def __mul__(self, number):
        _check_is_number(number)
        return EmptySet()

    def __or__(self, other):
        # should add validation here
        return other

    def __and__(self, other):
        return EmptySet()

    def __repr__(self):
        return "\u2205"
