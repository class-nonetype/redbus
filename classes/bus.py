class Bus:
    """
    A class used to represent a bus

    ...

    Attributes
    ----------
    id                       : int
        available bus id

    meters_distance          : int
        the distance in meters

    min_arrival_time         : int
        the number of minimum arrival time

    max_arrival_time         : int
        the minimum of maximum arrival time


    Methods
    -------
    __str__(self)       -> str
        Return attributes
        
    service(self)       -> dict
        Return the available services class
    """



    def __init__(self, available_bus : dict):

        self.id                = available_bus['id']
        self.meters_distance   = available_bus['meters_distance']
        self.min_arrival_time  = available_bus['min_arrival_time']
        self.max_arrival_time  = available_bus['max_arrival_time']


    def __str__(self) -> str:

        class_data = str(
            '\n'
            f'\t\tid                    {self.id}' + '\n'
            f'\t\tmeters_distance       {self.meters_distance} metros' + '\n'
            f'\t\tmin_arrival_time      {self.min_arrival_time} minutos.' + '\n'
            f'\t\tmax_arrival_time      {self.max_arrival_time} minutos.' + '\n'
        )

        return class_data