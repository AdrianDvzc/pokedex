import requests
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Pokedex")
window.geometry("400x300")

header = tk.Label(window, text="Write the name of your pokemon: ex. ditto")
header.pack()

input = tk.Entry(window)
input.pack()

stat_labels = {}

def search():
    pokemon = input.get()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
    
    if response.status_code == 200:
        data = response.json()
        for i in data["stats"]:
            name = i["stat"]["name"]
            base_stat = i["base_stat"]
            stat_labels[name].config(text=f"base {name}: {base_stat}")

            # print(stat_labels[name], i)

    else:
        print(response.status_code, response.content)
        messagebox.showinfo(f"error {response.status_code}", response.content)


search_b = tk.Button(window, text="Search Pokedex", command=search)
search_b.pack()

stats = tk.Label(window, text="stats:", justify="left")
stats.pack()

stat_data = requests.get("https://pokeapi.co/api/v2/pokemon/ditto").json()
for x in stat_data["stats"]:
    stat_name = x["stat"]["name"]
    label = tk.Label(window, text=f"base {stat_name}: /")
    label.pack()
    stat_labels[stat_name] = label

window.mainloop()