from flask import Flask, render_template

# create a website object
my_app = Flask(__name__)


@my_app.route("/")  # @ shows that this line is a decorator
def home_page():
    # return_template function is needed to return html file
    return render_template("home.html")


@my_app.route("/api/v1/<station>/<date>")  # @ shows that this line is a decorator
def about_page(station, date):
    temperature = 54
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    my_app.run(debug=True)
