# -*- coding: utf-8 _*_

import sys
import requests
import json

base_url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
api_key = '01e0506d39dd24c879d400bfdbb77d05'
history = {}

def prompt():
    print("Give me a city to query weather information,")
    print("For example: beijing.")
    print("Or give me ? for hints.")

def accessory():
    while True:
        user_inp  = input("Please... >").strip()
        if user_inp in ['help','h', '?']:
            print('''
                A city name: you will get weather information,
                help or h: help information,
                quit or q: exit the application,
                history:   the query history.
                ''')
        elif user_inp in ['quit', 'q']:
            exit(1)
        elif user_inp in ['history', 'his']:
            for x, y in history.items():
                print(x, y)
        else:
            get_temperature(user_inp)

def get_temperature(city):
    try:
        query = base_url + '?q=%s,CN&cnt=3&units=metric&APPID=%s' % (city, api_key)
        response = requests.get(query,timeout=1)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("We don't have the weather information for %s" % city)
        print("Please try another place.")
        return 0
    except requests.exceptions.Timeout:
        print("The server is busy, please try again later.")
        return 0
    except requests.exceptions.ConnectionError:
        print("Please check your network connection.")
        return 0
    weatherData = json.loads(response.text)
    w = weatherData['list']
    print('Current weather in %s:' % (city))
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print('and temperature is: %dºC' %(w[0]['temp']['day']))
    history[city] = w[0]['weather'][0]['main']

    '''
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tommorow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
    '''

def main():
    prompt()
    accessory()

if __name__ == '__main__':
    main()
