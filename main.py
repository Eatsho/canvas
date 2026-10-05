# import tkinter as tk

# root=tk.Tk()
# root.title("My First Canvas")

# canvas = tk.Canvas(root, width=500, height=350, bg='blue')
# canvas.pack()

# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(280, 50, 440, 190, fill="lightblue")
# canvas.create_line(50, 250, 500, 250, width=4)
# canvas.create_text(275, 310, text= "Hello Canvas", font= ("Arail", 20))

# root.mainloop()

import tkinter as tk

root=tk.Tk()
root.title("My village home")

canvas = tk.Canvas(root, width=700, height=700, bg='white')
canvas.pack()

# House Body - Rectangle

canvas.create_rectangle(
    150, 250, 450, 500,
    fill="#FFF2B2",       # Light yellow
    outline="#555555",
    width=3
)

# Roof - Triangle

canvas.create_polygon(
    120, 250,
    300, 100,
    480, 250,
    fill="#FFB3B3",       # Light pink
    outline="#555555",
    width=3
)

# Left Window - Square

canvas.create_rectangle(
    185, 300, 245, 360,
    fill="#B3E5FC",       # Light blue
    outline="#555555",
    width=3
)

# Right Window - Square

canvas.create_rectangle(
    355, 300, 415, 360,
    fill="#B3E5FC",       # Same light blue
    outline="#555555",
    width=3
)

# Door - Small Rectangle
canvas.create_rectangle(
    270, 390, 330, 500,
    fill="#D8B4E2",
    outline="#555555",
    width=3
)

root.mainloop()