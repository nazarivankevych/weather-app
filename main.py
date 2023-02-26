# Weather app: Develop a weather app that displays the current weather for a given location using an API.
# 5cf098f5fb66d2693ac64dd801381bc7 - api openweather


import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import logging

API = "5cf098f5fb66d2693ac64dd801381bc7"
CITY = 'Lutsk'


def get_weather(city):
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
    return request


def get_icon():
    # get images by url
    url = f"https://openweathermap.org/img/w/{get_weather('Lutsk').json()['weather'][0]['icon']}.png"
    response = requests.get(url)
    icon_data = response.content
    img = Image.open(BytesIO(icon_data))
    img = img.resize((150, 150), Image.LANCZOS)
    return img


def get_temperature():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat=50.7593&lon=25.3424&exclude=daily&units=metric&appid={API}"
    response = requests.get(url)
    temp = response.json()['current']['temp']
    return round(temp)

def get_description():
    return get_weather('Lutsk').json()['weather'][0]['description']


def more_details():
    """_summary_

    Returns:
        json: dict(),
        main: ['humidity', 'pressure'],
        wind: ['speed']
    """
    info = ''
    for key, value in get_weather('Lutsk').json().items():
        if key == 'main':
            info += f'Humidity: {value["humidity"]}\nPressure: {value["pressure"]}\n'
        elif key == 'Wind':
            info += f'{key}: {value["speed"]} m/s\n'
    return info


def display():
    window = tk.Tk()
    window.title(f"Weather in {CITY}")
    window.geometry('550x380')
    # insert data from functions on main display
    img = ImageTk.PhotoImage(get_icon())
    icons = tk.Label(window, image=img, height=200, width=200)
    temperature = tk.Label(window, text=f"{get_temperature()} °C", font=("Arial", 30))
    description = tk.Label(window, text=get_description(), font=("Arial", 30))
    details = tk.Label(window, text=more_details(), wraplength=400, font=("Arial", 15))
    # need to change from grid into place
    icons.grid(column=0, rowspan=2)
    temperature.grid(row = 0, column = 1, pady=5)
    description.grid(row=1, column=1, pady=5)
    details.place(x=550/2, y=300, width=380, height=100)

    window.mainloop()


if __name__ == "__main__":
    display()
