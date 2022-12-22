import os
import platform



class ExecutionEnvironment:

    def __init__(self):
        self.attr = {
            'os'         : platform.system(),
            'exceptions' : []
        }
    
    def set_attr(self, **kwargs) -> dict:
        self.attr.update(kwargs)

        return self.attr
    
    def get_attr(self) -> dict:
        return self.attr

env = ExecutionEnvironment()


try:
    import requests

except ImportError as exc:

    env.attr['exceptions'].append(exc)

    if env.attr['os'] == 'Linux':
        os.system(
            '''python3 -m pip3 install requests'''
        )
    
    elif env.attr['os'] == 'Windows':
        os.system(
            '''python -m pip install requests'''
        )

finally:    
    import requests

import json



if env.attr['os'] == 'Windows':
    
    env.set_attr(
        json_directory = os.getcwd() + '\\' + 'json'
    )

elif env.attr['os'] == 'Linux':
    env.set_attr(
        json_directory = os.getcwd() + '/' + 'json'
    )

if not os.path.exists(env.attr['json_directory']):
    os.mkdir(env.attr['json_directory'])









class Bus:
    
    def __init__(self, available_bus : dict):

        self.id                = available_bus['id']
        self.meters_distance   = available_bus['meters_distance']
        self.min_arrival_time  = available_bus['min_arrival_time']
        self.max_arrival_time  = available_bus['max_arrival_time']


    def __str__(self) -> str:
        class_data =\
            '\n\t\tid : {}\n\t\tmeters_distance : {}m.\n\t\tmin_arrival_time : {} minutos.\n\t\tmax_arrival_time : {} minutos.\n\t\t'.format(
                self.id, self.meters_distance,
                self.min_arrival_time, self.max_arrival_time
            )

        return class_data
            



class AvailableService:

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
                
        class_data =\
            '\n\tid : {}\n\tvalid : {}\n\tstatus_description : {}\n\tavailable_buses : {}\n\tbuses : {}\n\t'.format(
                self.id, self.valid, self.status_description,
                self._range, self.check_available_buses()
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

class Service:
    
    def __init__(self, available_service):

        self.AvailableService = AvailableService(available_service)


class BusStation:
    
    def __init__(self, index : int):
        self.id                  = data['id']
        self.name                = data['name']
        self.status_code         = data['status_code']
        self.status_description  = data['status_description']
        
        self.services           = data['services'][index]


    def __str__(self) -> str:
        class_data =\
            'id : {}\nname : {}\nstatus_code : {}\nstatus_description : {}\nservices : {}\n'.format(
                self.id, self.name,
                self.status_code, self.status_description,
                self.service()
            )

        
        return class_data

            
    def service(self) -> str:
                
        for available_services in self.services:
            for services in self.services[available_services]:
                return Service(self.services).AvailableService.__str__()


def write_json_file(id : str):

    api_url = 'https://api.xor.cl/red/bus-stop/' + id

    request = requests.get(
        url     = api_url,
        headers =\
            {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            }
    )
            
    data = request.text

    if env.attr['os'] == 'Windows':

        env.set_attr(
            json_file = env.attr['json_directory'] + '\\' + 'data.json'
        )
        
    
    elif env.attr['os'] == 'Linux':
        env.set_attr(
            json_file = env.attr['json_directory'] + '/' + 'data.json'
        )
    
    
    with open(env.attr['json_file'], 'w') as json_file:
        
        json_file.write(data)

    json_file.close()


def read_json_file():
    
    if os.path.exists(env.attr['json_file']):

        with open(env.attr['json_file'], 'r') as json_file:

            content = json_file.read()

            global data
            data = json.loads(content)

            if env.attr['os'] == 'Linux':
                os.system('clear')
            
            elif env.attr['os'] == 'Windows':
                os.system('cls')


            services = len(data['services'])

            for index in range(services):
                yield BusStation(index)


def main():

    id = input('ID del paradero (ejemplo: PI540)\t')

    while True:

        write_json_file(id)

        for data in read_json_file():
            print(data)





if __name__ == '__main__':
    main()