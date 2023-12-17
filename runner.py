from flask import Flask, render_template, request
from dots_creators import get_x_y_ballistic
from factories import func_animation_factory

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
async def index():
    mass = 0.1
    radius = 0.02
    start_speed = 100
    alpha = 60

    if request.method == "POST":
        alpha = float(request.form["number1"])
        radius = float(request.form["number2"])
        start_speed = float(request.form["number3"])
        mass = float(request.form["number4"])

    x_dots, y_dots = get_x_y_ballistic(mass, radius, start_speed, alpha)

    animation = await func_animation_factory(x_dots, y_dots)

    return render_template(
        "index.html",
        graph=animation.to_jshtml(),
        r=radius,
        m=mass,
        a=alpha,
        v0=start_speed,
    )


if __name__ == "__main__":
    app.run()
