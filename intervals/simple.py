from validation import _validate_init_inputs, _check_is_number


class SimpleInterval:
    def __init__(self, a, b, left_open=False, right_open=False):
        _validate_init_inputs(a, b, left_open, right_open)
        self.a = a
        self.b = b
        self.left_open = left_open
        self.right_open = right_open

    def size(self):
        return self.b - self.a

    def __add__(self, number):
        _check_is_number(number)
        return SimpleInterval(
            self.a + number,
            self.b + number,
            left_open=self.left_open,
            right_open=self.right_open,
        )

    def __sub__(self, number):
        _check_is_number(number)
        return SimpleInterval(
            self.a - number,
            self.b - number,
            left_open=self.left_open,
            right_open=self.right_open,
        )

    def __mul__(self, number):
        _check_is_number(number)
        return SimpleInterval(
            self.a * number,
            self.b * number,
            left_open=self.left_open,
            right_open=self.right_open,
        )

    def __repr__(self):
        left_brace = "(" if self.left_open else "["
        right_brace = ")" if self.right_open else "]"
        return f"{left_brace}{self.a}, {self.b}{right_brace}"
