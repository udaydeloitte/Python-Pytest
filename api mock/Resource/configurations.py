import configparser

def getconfig():
    config = configparser.ConfigParser()
    config.read("Resource/properties.ini")
    return config
