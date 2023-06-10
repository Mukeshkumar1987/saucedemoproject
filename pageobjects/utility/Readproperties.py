import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\mukes\\PycharmProjects\\SauceDemo\\pageobjects\\configurations\\config.ini")

class Readconfig():
    @staticmethod
    def geturl():
        url = "https://www.saucedemo.com/"
        return url

    @staticmethod
    def getusername():
        username = "standard_user"
        return username

    @staticmethod
    def getpassword():
        password = "secret_sauce"
        return password




