from PIL import Image, ImageTk  
import tkinter as tk
import requests
import time

def getWeather(event):
    city= textfield.get()
    api ="https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=afcdcea4e2133cdc87dc68f2b2ddd4ec"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp=int(json_data['main']['temp'] - 273.15)
    min_temp=int(json_data['main']['temp_min'] - 273.15)
    max_temp=int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed'] 
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(temp) + "\n" + "Min Temp: " + str(min_temp)+ "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: "+ str(humidity)+ "\n" + "Wind Speed: "+ str(wind)+ "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")


background_image = Image.open("image.jpg")  
background_photo = ImageTk.PhotoImage(background_image)


background_label = tk.Label(canvas, image=background_photo)
background_label.place(relwidth=1, relheight=1)  

f = ("Times New Roman", 20, "bold")
t = ("Times New Roman", 20, "bold")

textfield = tk.Entry(canvas, font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t, bg='#5e548e', fg='#fff') 
label1.pack()
label2 = tk.Label(canvas, font=f, bg='#5e548e', fg='#fff') 
label2.pack()

canvas.mainloop()
