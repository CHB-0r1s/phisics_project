from flask import Flask, render_template, request
from anim_creator import create_anim

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
async def index():
    mass = 0.1
    radius = 0.02
    start_speed = 100
    alpha = 60

    if request.method == 'POST':
        alpha = float(request.form['number1'])
        radius = float(request.form['number2'])
        start_speed = float(request.form['number3'])
        mass = float(request.form['number4'])
        # print('Угол:', alpha)
        # print('Радиус:', radius)
        # print('Начальная скорость:', start_speed)
        # print('Масса:', mass)
    graph = await create_anim(mass, radius, start_speed, alpha)
    return render_template('index.html', graph=graph, r=radius, m=mass, a=alpha, v0=start_speed)


if __name__ == '__main__':
    #print(graph)
    app.run()
