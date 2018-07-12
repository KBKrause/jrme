from weather import Weather, Unit
import smtplib

class JWeather:

    # JRME resource library: file_lib
    # Weather object:        weather
    # location, forecasts:   location
    #                        forecasts

    def __init__(self):
        self.file_lib = open("lib")
        self.weather = Weather(unit=Unit.FAHRENHEIT)
        self.initWeather()

    def initWeather(self):
        self.location = self.weather.lookup_by_location('indianapolis')
        self.location = self.weather.lookup_by_location('indianapolis')
        self.forecasts = self.location.forecast

    def printForecasts(self):      
        for forecast in self.forecasts:
            print(forecast.date + " : " + forecast.text)

class JMail:

    # Email server from SMTP: server
    # Body text for email:    bText

    def __init__(self):
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()

    # TODO
    def initSenderFromLib(self, senderAddr, senderPW):
        pass

    def initSenderFromInput(self):
        user = input("Email: ")
        pw = input("Password: ")
        if (self._tryEmailAuth(user, pw) == False):
            print("Failed!")
        else:
            print("Yay!")
    

    def prepareMessage(self, str):
        self.bText += str

    def _tryEmailAuth(self, senderAddr, senderPW):
        retval = True
        try:
            self.server.login(senderAddr, senderPW)
        # TODO this doesn't seem to be catching correctly ...
        except SMTPAuthenticationError:
            print("The email/password combination for " + senderAddr + " was not authenticated")
            retval = False
        return retval


class JFileManipulator:

    # File handle: jfmHandle

    def __init__(self):
        pass

    def openFile(self, fopen):
        try:
            self.jfmHandle = open(fopen,"r")
        except IOError:
            print("Could not open the specified file for writing: " + fopen)
            self.jfmHandle = None

#jweather = JWeather()
#jweather.printForecasts()
jmail = JMail()
#jfm = JFileManipulator()
#jfm.openFile("lib")
jmail.initSenderFromInput()

# server.login("chukareth@gmail.com", "###")

# msg = "Hello world!"

# server.sendmail("chukareth@gmail.com", "kkrause2@carthage.edu", msg)
# server.quit()