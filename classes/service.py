from classes.available_service import AvailableService

class Service:
    """
    A class used to represent the service

    ...

    Attributes
    ----------
    AvailableService                       : class -> AvailableService
        class of buses available

    """
    def __init__(self, available_service):

        self.AvailableService = AvailableService(available_service)
