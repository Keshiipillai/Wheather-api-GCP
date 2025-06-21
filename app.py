from flask import Flask, request
import requests
import os

app = Flask(__name__)

@app.route("/weather")
def get_weather():
    city = request.args.get("city", "Mumbai")
    api_key = os.environ.get("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# ✅ This part tells Cloud Run to use port 8080
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

