class CalorentoException(Exception):
    pass


class WeatherNotFound(ValueError, CalorentoException):
    pass
