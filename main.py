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

# ==============================
# CREATE WINDOW
# ==============================
root = tk.Tk()
root.title("My Village Home")
root.geometry("900x700")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=900,
    height=700,
    bg="#DFF3FF"
)
canvas.pack()


# ==============================
# SKY
# ==============================

# Sun
canvas.create_oval(
    700, 60, 790, 150,
    fill="#FFD700",
    outline="#F39C12",
    width=3
)

# Clouds
canvas.create_oval(100, 80, 170, 125, fill="white", outline="")
canvas.create_oval(140, 65, 220, 125, fill="white", outline="")
canvas.create_oval(190, 80, 260, 125, fill="white", outline="")

canvas.create_oval(430, 100, 500, 140, fill="white", outline="")
canvas.create_oval(470, 80, 550, 140, fill="white", outline="")
canvas.create_oval(520, 100, 590, 140, fill="white", outline="")


# ==============================
# MOUNTAINS
# ==============================

canvas.create_polygon(
    0, 420,
    180, 200,
    330, 420,
    fill="#8FB89A",
    outline="#6E8F78"
)

canvas.create_polygon(
    250, 420,
    480, 170,
    700, 420,
    fill="#789C86",
    outline="#5D7D69"
)

canvas.create_polygon(
    560, 420,
    750, 210,
    900, 420,
    fill="#91B69B",
    outline="#6E8F78"
)


# Snow caps
canvas.create_polygon(
    180, 200,
    145, 245,
    180, 230,
    205, 255,
    230, 240,
    fill="white",
    outline=""
)

canvas.create_polygon(
    480, 170,
    435, 220,
    480, 205,
    515, 240,
    545, 225,
    fill="white",
    outline=""
)


# ==============================
# GROUND
# ==============================

canvas.create_rectangle(
    0, 420, 900, 700,
    fill="#8FDD8F",
    outline=""
)

# Small pathway
canvas.create_polygon(
    390, 500,
    510, 500,
    620, 700,
    270, 700,
    fill="#D8C19F",
    outline="#B89F7B"
)


# ==============================
# MAIN HOUSE
# ==============================

# House body
canvas.create_rectangle(
    180, 270, 520, 520,
    fill="#FFF0B3",
    outline="#555555",
    width=3
)

# Main roof
canvas.create_polygon(
    140, 270,
    350, 100,
    560, 270,
    fill="#EFA3A3",
    outline="#555555",
    width=3
)

# Roof lower border
canvas.create_line(
    140, 270, 560, 270,
    fill="#555555",
    width=4
)


# ==============================
# MAIN HOUSE WINDOWS
# ==============================

# Left window
canvas.create_rectangle(
    215, 320, 285, 390,
    fill="#A9DDF5",
    outline="#555555",
    width=3
)

# Right window
canvas.create_rectangle(
    415, 320, 485, 390,
    fill="#A9DDF5",
    outline="#555555",
    width=3
)

# Window divisions
canvas.create_line(
    250, 320, 250, 390,
    fill="#555555",
    width=2
)

canvas.create_line(
    215, 355, 285, 355,
    fill="#555555",
    width=2
)

canvas.create_line(
    450, 320, 450, 390,
    fill="#555555",
    width=2
)

canvas.create_line(
    415, 355, 485, 355,
    fill="#555555",
    width=2
)


# ==============================
# MAIN DOOR
# ==============================

canvas.create_rectangle(
    315, 395, 385, 520,
    fill="#C9A0DC",
    outline="#555555",
    width=3
)

# Door handle
canvas.create_oval(
    365, 455, 372, 462,
    fill="#8B5A2B",
    outline=""
)


# ==============================
# DOG HOUSE
# ==============================

# Dog house body
canvas.create_rectangle(
    620, 430, 760, 520,
    fill="#B63B3B",
    outline="#663333",
    width=3
)

# Dog house roof
canvas.create_polygon(
    590, 430,
    690, 345,
    790, 430,
    fill="#8B0000",
    outline="#663333",
    width=3
)


# Dog house entrance
canvas.create_oval(
    655, 455, 725, 530,
    fill="#241A17",
    outline="#663333",
    width=2
)


# ==============================
# DOG
# ==============================

# Dog body
canvas.create_oval(
    775, 520, 850, 575,
    fill="#A86F42",
    outline="#633F27",
    width=2
)

# Dog head
canvas.create_oval(
    750, 485, 815, 545,
    fill="#A86F42",
    outline="#633F27",
    width=2
)

# Dog ears
canvas.create_polygon(
    755, 495,
    735, 475,
    745, 515,
    fill="#70452D",
    outline="#633F27"
)

canvas.create_polygon(
    800, 495,
    820, 475,
    815, 520,
    fill="#70452D",
    outline="#633F27"
)

# Dog eyes
canvas.create_oval(
    765, 505, 772, 512,
    fill="black"
)

canvas.create_oval(
    795, 505, 802, 512,
    fill="black"
)

# Dog nose
canvas.create_oval(
    780, 520, 790, 530,
    fill="black"
)

# Dog tail
canvas.create_arc(
    830, 500, 875, 550,
    start=260,
    extent=180,
    style=tk.ARC,
    outline="#70452D",
    width=6
)


# ==============================
# TREES
# ==============================

# Tree 1 trunk
canvas.create_rectangle(
    70, 390, 95, 520,
    fill="#795548",
    outline=""
)

# Tree 1 leaves
canvas.create_oval(
    35, 330, 130, 420,
    fill="#3E8E41",
    outline="#2E6E32"
)

canvas.create_oval(
    65, 300, 155, 400,
    fill="#4CAF50",
    outline="#2E6E32"
)

# Tree 2 trunk
canvas.create_rectangle(
    830, 370, 850, 500,
    fill="#795548",
    outline=""
)

# Tree 2 leaves
canvas.create_oval(
    790, 310, 880, 400,
    fill="#3E8E41",
    outline="#2E6E32"
)

canvas.create_oval(
    820, 280, 900, 390,
    fill="#4CAF50",
    outline="#2E6E32"
)


# ==============================
# FLOWERS
# ==============================

def flower(x, y, color):
    # Stem
    canvas.create_line(
        x, y, x, y + 25,
        fill="green",
        width=2
    )

    # Petals
    canvas.create_oval(
        x - 8, y - 8,
        x, y,
        fill=color,
        outline=""
    )

    canvas.create_oval(
        x, y - 8,
        x + 8, y,
        fill=color,
        outline=""
    )

    canvas.create_oval(
        x - 8, y,
        x, y + 8,
        fill=color,
        outline=""
    )

    canvas.create_oval(
        x, y,
        x + 8, y + 8,
        fill=color,
        outline=""
    )

    # Center
    canvas.create_oval(
        x - 3, y - 3,
        x + 3, y + 3,
        fill="yellow",
        outline=""
    )


flower(120, 560, "#FF69B4")
flower(170, 600, "#9C27B0")
flower(730, 590, "#FF5252")
flower(820, 620, "#FF9800")


# ==============================
# TITLE
# ==============================

canvas.create_text(
    450, 35,
    text="My Beautiful Village Home",
    font=("Arial", 24, "bold"),
    fill="#2F4F4F"
)


root.mainloop()