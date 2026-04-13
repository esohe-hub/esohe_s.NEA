#The entire UI
import tkinter as tk

window = tk.Tk()
window.title("My First App")
window.geometry("500x300")
window.resizable(False, False)

#function that runs when the button is clicked
def greet_user():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

#input field
entry = tk.Entry(window, font=("Georgia", 12))
entry.pack()

#button
button = tk.Button(window, text="Submit", font=("Georgia", 12), command=greet_user)
button.pack()

#output label
label = tk.Label(window, text="", font=("Georgia", 16))
label.pack()



'''def handle_click():
    print("Button clicked")

label = tk.Label(window, text="Click Me", font=("Georgia", 16))
label.pack()

button = tk.Button(window, text="Click Me", font=("Georgia", 12), command=handle_click)
button.pack()'''

window.mainloop()

