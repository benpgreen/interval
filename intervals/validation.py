def _validate_init_inputs(a, b, left_closed, right_closed):
    _check_is_number(a, b)
    if not isinstance(left_closed, bool):
        raise TypeError(
            f"left_closed={left_closed} should be a bool, is a {type(left_closed)}"
        )
    if not isinstance(right_closed, bool):
        raise TypeError(
            f"right_closed={right_closed} should be a bool, is a {type(right_closed)}"
        )

    # check Interval not empty
    if a > b:
        raise ValueError(
            f"Right bound cannot be less than left bound; a={a} must be <= b={b}"
        )
    elif a == b and not (left_closed and right_closed):
        raise ValueError(
            "Interval should not be empty, if a=b then interval must be closed."
        )


def _check_is_number(*numbers):
    for number in numbers:
        if not isinstance(number, (float, int)):
            raise TypeError(
                f"{number} should be an int or a float, is a {type(number)}"
            )
