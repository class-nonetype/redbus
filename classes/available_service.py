from classes.bus import Bus


class AvailableService:

    """
    A class used to represent the available service

    Attributes
    ----------
    id                  : int
        bus id

    valid               : bool
        bus validation

    status_code         : int
        status code of bus station 

    status_description  : int
        description of bus services
    
    buses               : list
        the data list of available buses

    Methods
    -------
    __str__(self)                     -> str
        Return attributes

    check_available_buses(self)       -> str
        Return the available buses class
    """


    def __init__(self, available_service : dict):
        
        self.id                   = available_service['id']
        self.valid                = available_service['valid']
        self.status_description   = available_service['status_description']

        self._range               = len(available_service['buses'])
        self.available_buses      = [i for i in range(self._range)]
                
        self.buses                = available_service['buses']
            

    def __str__(self) -> str:

        if self._range == 0:
            self._range = 'No disponible'
        
        class_data = str(
            '\n'
            f'\tid                    {self.id}' + '\n'
            f'\tvalid                 {self.valid}' + '\n'
            f'\tstatus_description    {self.status_description}' + '\n'
            f'\tavailable_buses       {self._range}' + '\n'
            f'\tbuses                 {self.check_available_buses()}' + '\n'
        )

        return class_data
            
    
    def check_available_buses(self) -> str:

        try:

            for bus in self.available_buses:

                if self._range == 0:
                    return ''
                        
                elif self._range == 1:
                    return f'{Bus(self.buses[0])}\n'
                        
                elif self._range == 2:
                    return f'{Bus(self.buses[0])}\n{Bus(self.buses[1])}\n'
                        
                elif self._range == 3:
                    return f'{Bus(self.buses[0])}\n{Bus(self.buses[1])}\n{Bus(self.buses[2])}\n'
                
        except:
            return f'{Bus(self.buses[bus])}\n'
