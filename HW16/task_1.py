import json
import multiprocessing
import threading
import time
from json import JSONDecodeError

import requests as requests

lst_of_cities = [{"city": "Detroit", "latitude": 42.33, "longitude": -83.05},
                 {"city": "Toronto", "latitude": 43.70, "longitude": -79.42},
                 {"city": "Bilbao", "latitude": 43.26, "longitude": -2.93},
                 {"city": "Napoli", "latitude": 40.88, "longitude": 14.52},
                 {"city": "Los Angeles", "latitude": 34.05, "longitude": -118.24}]

multithread_time = []
mutliproces_time = []
def multi_threads(lst):
    result = []
    avrge_temp = []
    def request_weather(city, latitude, longitude):
        print(f"Start for {city}")
        resp = requests.get(
                url="https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": latitude,
                    "longitude": longitude,
                    "hourly": "temperature_2m",
                }
        )
        result.append(resp)
        temperature_list = resp.json()["hourly"]["temperature_2m"]
        avr_temperature = round(sum(temperature_list) / len(temperature_list), 1)
        temp = {"city": city, "avrg_temp": avr_temperature}
        avrge_temp.append(temp)
        print(f"Average temperature for {city} is {avr_temperature}")

    start = time.time()
    threads = []
    for i in lst_of_cities:
        threads.append(threading.Thread(target=request_weather,
                                        args=(i.get("city"), i.get("latitude"), i.get("longitude"), )))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()



    max_temp = {}
    for i in avrge_temp:
        if max_temp == {}:
            max_temp = i
        if i.get("avrg_temp") > max_temp.get("avrg_temp"):
            max_temp = i
    print(f"The {max_temp.get('city')} has biggest temperature {max_temp.get('avrg_temp')}")

    end = time.time()
    result = end - start
    multithread_time.append(result)
    print(f"Multi thread time is {end - start}")

def one_thread(lst):
    start = time.time()
    result = []
    for i in lst:
        resp = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": i.get("latitude"),
                "longitude": i.get("longitude"),
                "hourly": "temperature_2m",
            }
        )
        result.append(resp)
        temperature_list = resp.json()["hourly"]["temperature_2m"]
        avr_temperature = round(sum(temperature_list) / len(temperature_list), 1)
        print(f"Average temperature for {i.get('city')} is {avr_temperature}")
    end = time.time()
    print(f"One thread time is {end - start}")


# ========MULTIPROCESS===========
def request(ithem, queue):
    city = ithem.get("city")
    latitude = ithem.get("latitude")
    longitude = ithem.get("longitude")
    print(f"Start for {city}")
    resp = requests.get(
            url="https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "hourly": "temperature_2m",
            }
    )
    temperature_list = resp.json()["hourly"]["temperature_2m"]
    avr_temperature = round(sum(temperature_list) / len(temperature_list), 1)
    temp = {"city": city, "avrg_temp": avr_temperature}
    queue.put(temp)
    print(f"Average temperature for {city} is {avr_temperature}")

def max_temp(lst):
    max_temp = {}
    for i in lst:
        if max_temp == {}:
            max_temp = i
        if i.get("avrg_temp") > max_temp.get("avrg_temp"):
            max_temp = i
    print(f"The {max_temp.get('city')} has biggest temperature {max_temp.get('avrg_temp')}")

def multiproces(lst):
    processes = []
    q = multiprocessing.Queue()
    lst_temp = []
    start = time.time()
    for i in lst:
        p = multiprocessing.Process(target=request, args=(i, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    while not q.empty():
        a = q.get()
        lst_temp.append(a)

    p2 = multiprocessing.Process(target=max_temp, args=(lst_temp, ))
    p2.start()
    p2.join()
    end = time.time()
    result = end - start
    mutliproces_time.append(result)
    print(f"Multiprocessing time {end - start}")

if __name__ == "__main__":
    multi_threads(lst_of_cities)
    # one_thread(lst_of_cities)
    multiproces(lst_of_cities)
    print(f"Tread = {multithread_time}, Process = {mutliproces_time}, Result = {mutliproces_time[0] - multithread_time[0]}")
