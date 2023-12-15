import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
from math import ceil
from typing import Callable, Iterable, Optional
from _functools import partial
from graph_updaters import simple_update

from matplotlib.lines import Line2D

matplotlib.use("agg")


async def func_animation_factory(
    x_dots: list,
    y_dots: list,
    line_update_func: Callable[
        [int, Optional[list], Optional[list], Optional[Line2D]], Iterable[Line2D]
    ] = simple_update,
    multiplicity_of_borders: int = 200,
    interval: int = 50,
):
    fig, ax = plt.subplots()

    line: Line2D = ax.plot(x_dots[0], y_dots[0])[0]
    max_x, max_y = max(y_dots), max(x_dots)

    borders = (
        ceil(max(max_x, max_y) / multiplicity_of_borders) * multiplicity_of_borders
    )
    ax.set(xlim=[0, borders], ylim=[0, borders])

    ani = animation.FuncAnimation(
        fig=fig,
        func=partial(line_update_func, x_list=x_dots, y_list=y_dots, line=line),
        interval=interval,
        frames=len(x_dots),
    )

    plt.close()

    return ani
