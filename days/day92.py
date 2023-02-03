import requests, json

timezone = "GMT"
latitude = 53.3498
longitude = -6.2603


def weathercode(code):
  if code == 0:
    return "Clear sky"
  elif code in range(1, 4):
    return "Mainly clear, partly cloudy, and overcast"
  elif code == 45 or code == 48:
    return "Fog and depositing rime fog"
  elif code in range(51, 56, 2):
    return "Drizzle: Light, moderate, and dense intensity"
  elif code in range(56, 58):
    return "Freezing Drizzle: Light and dense intensity"
  elif code in range(61, 66, 2):
    return "Freezing Drizzle: Light and dense intensity"
  elif code in range(66, 68):
    return "Freezing Rain: Light and heavy intensity"
  elif code in range(71, 76, 2):
    return "Freezing Drizzle: Light and dense intensity"
  elif code == 77:
    return "Snow grains"
  elif code in range(80, 83):
    return "Rain showers: Slight, moderate, and violent"
  elif code in range(85, 87):
    return "Snow showers slight and heavy"
  elif code == 95:
    return "Thunderstorm: Slight or moderate"
  elif code in range(96, 100, 3):
    return "Thunderstorm with slight and heavy hail"


result = requests.get(
  f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}"
)

weather = result.json()
#print(json.dumps(weather, indent=2))

# get today's forecast only, with min and max temps + weathercode
today = weather["daily"]["time"][0]
min_temp = weather["daily"]["temperature_2m_min"][0]
max_temp = weather["daily"]["temperature_2m_max"][0]
w_code = weathercode(int(weather["daily"]["weathercode"][0]))
# Celcius sign
celc = u"\u00b0"

# print output
out = f"""The weather for today, {today}:\n{w_code}.\nMin: {min_temp}{celc}C\t\tMax: {max_temp}{celc}C"""
print(out)
