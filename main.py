import requests
from twilio.rest import Client
import os

account_sid = os.environ.get("SID")
auth_token = os.environ.get("AUTH")

end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "915405c6ad72c496ed3beb2494ecaab8"
PARAMETERS = {
    "lat": 41.902782,
    "lon": 12.496365,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url=end_point, params=PARAMETERS)
response.raise_for_status()
data = response.json()

will_rain = False
for i in data["list"]:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) <= 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, so remember to bring an Umbrella ☔️",
        from_="+12516518829",
        to="+393312504573"
    )
    print(message.sid)



















