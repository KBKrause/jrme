from weather import Weather, Unit
import smtplib

weather = Weather(unit=Unit.FAHRENHEIT)

location = weather.lookup_by_location('indianapolis')
forecasts = location.forecast
for forecast in forecasts:
    print(forecast.date + " : " + forecast.text)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("chukareth@gmail.com", "###")

msg = "Hello world!"

server.sendmail("chukareth@gmail.com", "kkrause2@carthage.edu", msg)
server.quit()