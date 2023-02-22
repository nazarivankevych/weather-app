# Weather app: Develop a weather app that displays the current weather for a given location using an API.
# 5cf098f5fb66d2693ac64dd801381bc7 - api openweather


import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

API = "5cf098f5fb66d2693ac64dd801381bc7"


def get_weather(city):
    request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
    return request


def display():
    window = tk.Tk()
    window.title(f"Weather in {get_weather('Lutsk')}")
    window.geometry("400x400")
    # get images by url
    url = f"http://openweathermap.org/img/w/{get_weather('Lutsk').json()['weather'][0]['icon']}.png"
    response = requests.get(url)
    data_content = response.content
    img = Image.open(BytesIO(data_content))
    img = ImageTk.PhotoImage(img)
    icon = tk.Label(window, image=img)
    # TODO: need to get a temperature from openweather by url
    temperature = tk.Label(window, text=f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={API}")
    info = tk.Label(window, text="Info")
    icon.grid(row=0, column=0)
    temperature.grid(row=0, column=1)
    # info.grid(row=1, column=0, columnspan=2)
    window.mainloop()


if __name__ == "__main__":
    display()
