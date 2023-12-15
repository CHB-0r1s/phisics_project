from math import *


def get_x_y_ballistic(m, r, V0, alpha) -> tuple[list, list]:
    g = 9.81
    alpha *= pi / 180  # перевод в радианы
    k_alpha = 0.47  # коэф. сопротивления, по умолчанию 0.47
    po = 1.275  # плотность воздуха при ну
    k_Fc = (
        k_alpha * pi * r**2 * po / 2
    )  # коэф. при силе сопротивления F(v), равен ~ 0.3piR^2

    t = 0
    dt = 0.45  # шаг интегрирования

    x, y = 0, 0  # начальная позиция
    x_dots: list = [x]
    y_dots: list = [y]  # точки графика

    Vx = V0 * cos(alpha)  # нач. проекция скоростей
    Vy = V0 * sin(alpha)

    while y >= 0:  # численное интегрирование
        V = sqrt(Vx**2 + Vy**2)  # текущая скорость
        Vx += (
            -k_Fc / m * Vx * V
        ) * dt  # делаем шаг интегрирования проекции ускорения ax = dVx/dt
        Vy += (-k_Fc / m * Vy * V - g) * dt  # dVy/dt
        x += Vx * dt  # проекции скорости Vx = dx/dt
        y += Vy * dt  # dy/dt
        t += dt  # шаг времени

        x_dots.append(x)  # добавляем точки на графике
        y_dots.append(y)

    return x_dots, y_dots
