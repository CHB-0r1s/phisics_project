from typing import Iterable
from matplotlib.lines import Line2D


def simple_update(
    frame: int, x_list: list, y_list: list, line: Line2D
) -> Iterable[Line2D]:
    X = x_list[:frame]
    Y = y_list[:frame]
    line.set_xdata(X)
    line.set_ydata(Y)

    return [line]
