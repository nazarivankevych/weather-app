import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests
from PIL.Image import Resampling

API_KEY = "5cf098f5fb66d2693ac64dd801381bc7"
CITY = "Lutsk"
LATITUDE = "50.7593"
LONGITUDE = "25.3424"


def get_weather(city):
    request = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    )
    return request


def get_icon():
    url = f"https://openweathermap.org/img/w/{get_weather(CITY).json()['weather'][0]['icon']}.png"
    response = requests.get(url)
    icon_data = response.content
    img = Image.open(BytesIO(icon_data))
    img = img.resize((150, 150), Resampling.LANCZOS)
    return img


def get_temperature():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={LATITUDE}&lon={LONGITUDE}&exclude=daily&units=metric&appid={API_KEY}"
    response = requests.get(url)
    temp = response.json()["current"]["temp"]
    return round(temp)


def get_description():
    return get_weather(CITY).json()["weather"][0]["description"]


def get_details():
    """Get additional weather details

    Returns:
        str: Additional weather details
    """
    info = ""
    for key, value in get_weather(CITY).json().items():
        if key == "main":
            info += f'Humidity: {value["humidity"]}\nPressure: {value["pressure"]}\n'
        elif key == "wind":
            info += f'{key.title()}: {value["speed"]} m/s\n'
    return info


def update_data():
    """Update the displayed data"""
    temperature.config(text=f"{get_temperature()} °C")
    description.config(text=get_description())
    details.config(text=get_details())
    img = ImageTk.PhotoImage(get_icon())
    icons.config(image=img)
    icons.image = img  # prevent garbage collection of image object


def display():
    window = tk.Tk()
    window.title(f"Weather in {CITY}")
    window.geometry("550x380")
    window.resizable(False, False)
    # window.configure(bg="#3d3d3d")

    # Insert data from functions on main display
    img = ImageTk.PhotoImage(get_icon())
    icons = tk.Label(window, image=img, height=200, width=200)
    temperature = tk.Label(
        window,
        text=f"{get_temperature()} °C",
        font=("Helvetica", 40, "bold"),
        fg="#ffffff",
        bg="#3d3d3d"
    )
    description = tk.Label(
        window,
        text=get_description(),
        font=("Helvetica", 20),
        fg="#ffffff",
        bg="#3d3d3d"
    )
    details = tk.Label(
        window,
        text=get_details(),
        wraplength=400,
        font=("Helvetica", 12),
        fg="#ffffff",
        bg="#3d3d3d",
        justify="left",
        anchor="w"
    )
    icons.grid(column=0, rowspan=2)
    temperature.grid(row=0, column=1, pady=5)
    description.grid(row=1, column=1, pady=5)
    details.place(x=430, y=300)
    # Schedule next update
    window.after(600000, update_data)  # update every 10 minutes

    window.mainloop()


if __name__ == "__main__":
    display()
