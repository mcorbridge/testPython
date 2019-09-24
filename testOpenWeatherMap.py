import logging
import time
import datetime
import openweathermapy.core as owm

units = 'imperial'
settings = {"APPID":"5aead618eb034cfd535ab9331ee4ec05", "units":units, "lang":"US"}
data = owm.get_current("Denver,US", **settings)
fahrenheit_degrees = u'\N{DEGREE SIGN}' + "F"
celcius_degrees = u'\N{DEGREE SIGN}' + "C"
doIteration = False

def convertDegreesToCompassDirection(deg):
	compass =["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW","N"]
	ndx = int(round(deg / 22.5) + 1)
	return compass[ndx]

print(data)
views = {"summary": ["main.temp", "main.pressure", "main.humidity","main.temp_min","main.temp_max","main.humidity"]}
metData = data.get_dict(views["summary"])

print("---------------------------------------------")

getDateStr = '%Y/%m/%d'
getTimeStr = '%#I:%M:%S %p'
dateTimeNow = datetime.datetime.now()

if units == "imperial":
	currentTemp = str(metData['main.temp']) + fahrenheit_degrees
	dailyHigh = str(metData['main.temp_max']) + fahrenheit_degrees
	dailyLow = str(metData['main.temp_min']) + fahrenheit_degrees
else:
	currentTemp = str(metData['main.temp']) + celcius_degrees
	dailyHigh = str(metData['main.temp_max']) + celcius_degrees
	dailyLow = str(metData['main.temp_min']) + celcius_degrees
	
print 

sys = data("sys.country","sys.sunset","sys.message","sys.type","sys.id","sys.sunrise")
sunrise = time.strftime('%#I:%M:%S %p ', time.localtime(data("sys.sunrise")))
sunset = time.strftime('%#I:%M:%S %p ', time.localtime(data("sys.sunset")))
print("current weather info on " + dateTimeNow.strftime(getDateStr) + " at " + dateTimeNow.strftime(getTimeStr))
print("location: " + data("name") + ", " + data("sys.country"))
print("sunrise: " + sunrise)
print("sunset: " + sunset)
print("clouds: " + str(data("clouds.all")) + "%")
print("visibility: " + str(data("visibility") / 1760) + " miles")
print("main: " + data("weather")[0]["main"])
print("id: " + str(data("weather")[0]["id"]))
print("icon: " + data("weather")[0]["icon"])
print("description: " + data("weather")[0]["description"])
print("pressure: " + str(data("main.pressure")) + " hpa")
print("temp_min: " + str(data("main.temp_min")) + fahrenheit_degrees)
print("temp_max: " + str(data("main.temp_max")) + fahrenheit_degrees)
print("temp: " + str(data("main.temp")) + fahrenheit_degrees)
print("humidity: " + str(data("main.humidity")) + "%")
print("wind speed: " + str(data("wind.speed")) + " mph")

try:
	print("wind direction: " + convertDegreesToCompassDirection(data("wind.deg")))
except:
	print("variable wind direction")
	
try:
	print("wind gusts up to: " + str(data("wind.gust")) + " mph")
except:
	print("no wind gusts")

if doIteration:
	for var in data:
		print(" ------------------------ ")
		print(var)
		print(type(data[var]))
		if isinstance(data[var], dict):
			for item in data[var]:
				print(" ==================== ")
				print(item)
				print(data[var][item])
		elif isinstance(data[var], list):
			for liteim in data[var]:
				if isinstance(liteim, dict):
					for i in liteim:
						print(" ==================== ")
						print(i)
						print(liteim[i])
				else:
					print(liteim)
		else:
			print(data[var])