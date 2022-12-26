import os
import platform


from classes.execution import ExecutionEnvironment
from classes.bus_station import BusStation



env = ExecutionEnvironment()



###############
#    Setup    #
###############
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
    data_directory = os.getcwd() + '\\' + 'data'

    env.set_attr(
        json_directory = data_directory + '\\' + 'json'
    )

elif env.attr['os'] == 'Linux':
    data_directory = os.getcwd() + '/' + 'data'


    env.set_attr(
        json_directory = data_directory + '/' + 'json'
    )

if not os.path.exists(env.attr['json_directory']):
    os.makedirs(env.attr['json_directory'])



###############
#    Write    #
###############
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


###############
#    Read     #
###############
def read_json_file():
    
    if os.path.exists(env.attr['json_file']):

        with open(env.attr['json_file'], 'r') as json_file:

            content = json_file.read()

            global data
            data = json.loads(content)

            os.system('cls' if os.name == 'nt' else 'clear')


            services = len(data['services'])

            for index in range(services):
                yield BusStation(
                    data,
                    index
                )


###############
#    main     #
###############
def main():

    id = input(
        'ID del paradero (ejemplo: PI540)\t'
    )

    while True:

        write_json_file(id)

        for data in read_json_file():
            print(data)





if __name__ == '__main__':
    main()