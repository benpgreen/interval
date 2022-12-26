from validation import _validate_init_inputs, _check_is_number


class SimpleInterval:
    def __init__(self, a, b, left_closed=True, right_closed=True):
        _validate_init_inputs(a, b, left_closed, right_closed)
        self.a = a
        self.b = b
        self.left_closed = left_closed
        self.right_closed = right_closed

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

    def __repr__(self):
        left_brace = "[" if self.left_closed else "("
        right_brace = "]" if self.right_closed else ")"
        return f"{left_brace}{self.a}, {self.b}{right_brace}"
