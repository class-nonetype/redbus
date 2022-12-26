from classes.service import Service

class BusStation:
    """
    A class used to represent a bus station

    Attributes
    ----------
    id                  : int
        bus station id

    name                : str
        name of bus station

    status_code         : int
        status code of bus station 

    status_description  : int
        description of the status
    
    services            : list
        the data list of available services

    Methods
    -------
    __str__(self)       -> str
        Return attributes

    service(self)       -> dict
        Return the available services class
    """

    def __init__(self, data : dict, index : int):
        self.id                  = data['id']
        self.name                = data['name']
        self.status_code         = data['status_code']
        self.status_description  = data['status_description']
        
        self.services            = data['services'][index]


    def __str__(self) -> str:

        class_data = str(
            f'id                    {self.id}' + '\n'
            f'name                  {self.name}' + '\n'
            f'status_code           {self.status_code}' + '\n'
            f'status_description    {self.status_description}' + '\n'
            f'services              {self.service()}' + '\n'
        )

        return class_data

            
    def service(self) -> str:
                
        for available_services in self.services:
            for services in self.services[available_services]:
                return Service(self.services).AvailableService.__str__()
