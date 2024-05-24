import tkinter as tk
import pyautogui as pg
prev_label = None

def handle(event):
    pos_x = pg.position().x
    pos_y = pg.position().y
    global prev_label
    if prev_label:
        prev_label.destroy()
    label = tk.Label(root, text=f"X:{pos_x} Y:{pos_y}", font=("Arial", 20))
    label.pack()
    prev_label = label
    

root = tk.Tk()
root.title("Mouse Position!")
root.geometry("300x300")

text = tk.Label(root, text="Press any key for find mouse X,Y position", font=("Arial", 10))
text.pack()

root.bind("<KeyPress>",handle)




root.mainloop()
