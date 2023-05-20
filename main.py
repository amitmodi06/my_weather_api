from flask import Flask, render_template
import pandas as pd

# create a website object
my_app = Flask(__name__)
df_stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = df_stations[["STAID", "STANAME                                 "]]

@my_app.route("/")  # @ shows that this line is a decorator
def home_page():
    # return_template function is needed to return html file
    return render_template("home.html", station_data=stations.to_html())


@my_app.route("/api/v1/<station>/<date>")  # @ shows that this line is a decorator
def about_page(station, date):
    print('date: ', date)
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    print(filename)
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == str(date)]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "__main__":
    my_app.run(debug=True)
