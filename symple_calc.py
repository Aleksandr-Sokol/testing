def linear_function(x: float) -> float:
    """
    f(x) = x + 1
    """
    return x + 1


def quadratic_function(x: float) -> float:
    """
    f(x) = x * x
    """
    return x * x + 1


def main_calc(x: float, f) -> float:
    """"
    :param float x : abcissa
    :param f : function
    return f(x)
    """
    value = f(x)
    return value
