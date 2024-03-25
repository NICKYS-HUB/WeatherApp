import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            city_name = data["name"]
            weather_desc = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            messagebox.showinfo(
                "Weather Information",
                f"City: {city_name}\nWeather: {weather_desc}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s"
            )
        else:
            messagebox.showerror("Error", f"City '{city}' not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def get_weather_button_click():
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        messagebox.showerror("Error", "Please enter a city!")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
label = tk.Label(root, text="Enter city:")
label.grid(row=0, column=0)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1)

get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_button_click)
get_weather_button.grid(row=1, columnspan=2)

# Start the main event loop
root.mainloop()
