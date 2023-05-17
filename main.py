from flask import Flask, render_template

# create a website object
my_app = Flask("Website")


@my_app.route("/home")  # @ shows that this line is a decorator
def home_page():
    # return_template function is needed to return html file
    return render_template("home.html")


my_app.run(debug=True)
