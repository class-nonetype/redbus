import platform



class ExecutionEnvironment:
    """
    A class used to represent the execution environment

    ...

    Attributes
    ----------
    attr                       : dict
        attributes of the execution environment

    Methods
    -------
    set_attr(self, **kwargs)       -> dict
        Return the attributes list updated
        
    get_attr(self)                 -> dict
        Return the attributes list
    """

    def __init__(self):
        self.attr : dict = {
            'os'         : platform.system(),
            'exceptions' : []
        }
    
    def set_attr(self, **kwargs) -> dict:
        self.attr.update(kwargs)

        return self.attr
    
    def get_attr(self) -> dict:
        return self.attr