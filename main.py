import asyncio
import requests
import os
import json
import platform


async def write_json_file(id):

    url = 'https://api.xor.cl/red/bus-stop/' + id

    request = requests.get(
        url,
        headers =\
            {
                "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            }
    )
            
    data = request.text

    with open('./json/data.json', 'w') as json_file:
        json_file.write(data)
    json_file.close()




async def read_json_file():
    with open('./json/data.json', 'r') as json_file:
        content = json_file.read()
        # json.dumps(_)
        data = json.loads(content)

        class Bus:

            def __init__(self, available_bus):
                self.id = available_bus['id']
                self.meters_distance = available_bus['meters_distance']
                self.min_arrival_time = available_bus['min_arrival_time']
                self.max_arrival_time = available_bus['max_arrival_time']
            
            def __str__(self):

                class_data =\
                    '\n\t\tid : {}\n\t\tmeters_distance : {}m.\n\t\tmin_arrival_time : {} minutos.\n\t\tmax_arrival_time : {} minutos.\n\t\t'.format(
                    self.id, self.meters_distance,
                    self.min_arrival_time, self.max_arrival_time
                )

                return class_data
            


        class AvailableService:

            def __init__(self, available_service):
                self.id = available_service['id']
                self.valid = available_service['valid']
                self.status_description = available_service['status_description']

                self._range = len(available_service['buses'])
                self.available_buses = [i for i in range(self._range)]
                
                self.buses = available_service['buses']
            
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

                self.id = data['id']
                self.name = data['name']
                self.status_code = data['status_code']
                self.status_description = data['status_description']
                self.services = data['services'][index]

            
            def service(self):
                
                for available_services in self.services:
                    for services in self.services[available_services]:
                        #return services -> id buses

                        return Service(self.services).AvailableService.__str__()



            def __str__(self):
                class_data =\
                    'id : {}\nname : {}\nstatus_code : {}\nstatus_description : {}\nservices : {}\n'.format(
                        self.id, self.name,
                        self.status_code, self.status_description,
                        self.service()
                )

                return class_data

        if platform.system() == 'Linux':
            os.system('clear')
        
        elif platform.system() == 'Windows':
            os.system('cls')


        buses_id = [i for i in range(0,12)]

        for index in buses_id:
            print(
                BusStation(index)
            )



async def main():

    if not os.path.exists('./json'):
        os.mkdir('./json')


    id = input('ID del paradero (ejemplo: PI540)\t')

    while True:
        await write_json_file(id)
        await read_json_file()



if __name__ == '__main__':
    asyncio.run(main())