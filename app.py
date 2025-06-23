from flask import Flask, request, render_template
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "Mumbai")
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        weather = response.json()
        return render_template("index.html", weather=weather)
    else:
        error_message = "❌ City not found. Please try again."
        return render_template("index.html", error=error_message)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
