from math import *


async def create_anim(m, r, V0, alpha):
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import matplotlib

    matplotlib.use('agg')

    g = 9.81
    alpha *= pi / 180  # перевод в радианы
    k_alpha = 0.47  # коэф. сопротивления, по умолчанию 0.47
    po = 1.275  # плотность воздуха при ну
    k_Fc = k_alpha * pi * r ** 2 * po / 2  # коэф. при силе сопротивления F(v), равен ~ 0.3piR^2

    t = 0
    dt = 0.5  # шаг интегрирования

    x, y = 0, 0  # начальная позиция
    x_list, y_list = [x], [y]  # точки графика

    Vx = V0 * cos(alpha)  # нач. проекция скоростей
    Vy = V0 * sin(alpha)

    while y >= 0:  # численное интегрирование
        V = sqrt(Vx ** 2 + Vy ** 2)  # текущая скорость
        Vx += (- k_Fc / m * Vx * V) * dt  # делаем шаг интегрирования проекции ускорения ax = dVx/dt
        Vy += (- k_Fc / m * Vy * V - g) * dt  # dVy/dt
        x += Vx * dt  # проекции скорости Vx = dx/dt
        y += Vy * dt  # dy/dt
        t += dt  # шаг времени

        x_list.append(x)  # добавляем точки на графике
        y_list.append(y)

    fig, ax = plt.subplots()
    # scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')

    line = ax.plot(x_list[0], y_list[0])[0]


    # ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
    # ax.legend()


    def update(frame):
        # for each frame, update the data stored on each artist.
        X = x_list[:frame]
        Y = y_list[:frame]
        # update the scatter plot:
        # data = np.stack([x, y]).T
        # scat.set_offsets(data)
        # update the line plot:
        line.set_xdata(X)
        line.set_ydata(Y)
        return line

    borders = ceil(max(max(y_list), x_list[-1]) / 200) * 200
    ax.set(xlim=[0, borders], ylim=[0, borders])
    ani = animation.FuncAnimation(fig=fig, func=update, interval=50, frames=len(x_list))
    graph = ani.to_jshtml()

    return graph
