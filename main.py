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
    return get_weather('Lutsk').json()


def display():
    window = tk.Tk()
    window.title(f"Weather in {get_weather(CITY)}")
    window.geometry("400x400")
    # insert data from functions on main display
    img = ImageTk.PhotoImage(get_icon())
    icons = tk.Label(window, image=img, height=200, width=200)
    temperature = tk.Label(window, text=f"{get_temperature()} Celcium", font=("Arial", 15))
    description = tk.Label(window, text=get_description(), font=("Arial", 15))
    details = tk.Label(window, text=more_details(), wraplength=400)
    # use grid to structure data
    icons.grid(row=0, column=0)
    temperature.grid(row=0, column=1)
    description.grid(row=1, column=1)
    details.grid(row=2, column=0, columnspan=2)

    window.mainloop()


if __name__ == "__main__":
    display()
