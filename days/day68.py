# hide the image and diplay the "Guess not..." text when a person is not found

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Hello")
window.geometry("300x200")

label = "Is it me you're loking for?!"


def Find():
  find = text.get("1.0", "end").lower().strip()
  if find == "charlotte":
    canvas.itemconfig(container, image=charlotte)
  elif find == "gerald":
    canvas.itemconfig(container, image=gerald)
  elif find == "katie":
    canvas.itemconfig(container, image=katie)
  elif find == "mo":
    canvas.itemconfig(container, image=mo)
  else:

    canvas.pack_forget()
    warning.pack()
    return
  warning.pack_forget()
  canvas.pack()


hello = tk.Label(text=label)
hello.pack()
warning = tk.Label(text="Guess not...")
hello.pack()
text = tk.Text(window, height=1, width=25)
text.pack()

button = tk.Button(text="Find", command=Find)
button.pack()

canvas = tk.Canvas(window, width=300, height=150)

#images
charlotte = ImageTk.PhotoImage(Image.open('.tutorial/guessWho/charlotte.jpg'))
gerald = ImageTk.PhotoImage(Image.open('.tutorial/guessWho/gerald.jpg'))
katie = ImageTk.PhotoImage(Image.open('.tutorial/guessWho/katie.jpg'))
mo = ImageTk.PhotoImage(Image.open('.tutorial/guessWho/mo.jpg'))

container = canvas.create_image(150, 1, image=charlotte)

tk.mainloop()
