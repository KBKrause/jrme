from weather import Weather, Unit
import smtplib

class JWeather:

    # JRME resource library: file_lib
    # Weather object:        weather
    # location, forecasts:   location
    #                        forecasts

    def initWeather(self):
        self.location = self.weather.lookup_by_location('indianapolis')
        self.location = self.weather.lookup_by_location('indianapolis')
        self.forecasts = self.location.forecast

    def __init__(self):
        self.file_lib = open("lib")
        self.weather = Weather(unit=Unit.FAHRENHEIT)
        self.initWeather()

    def printForecasts(self):      
        for forecast in self.forecasts:
            print(forecast.date + " : " + forecast.text)

jweather = JWeather()
jweather.printForecasts()
#jweather.printForcasts()

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login("chukareth@gmail.com", "###")

# msg = "Hello world!"

# server.sendmail("chukareth@gmail.com", "kkrause2@carthage.edu", msg)
# server.quit()