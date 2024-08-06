
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/sanbid/Desktop/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1083x548")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 548,
    width = 1083,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1083.0,
    548.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    104.0,
    21.0,
    anchor="nw",
    text="Username",
    fill="#000000",
    font=("Inter", 24 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    56.0,
    44.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    55.0,
    131.0,
    image=image_image_2
)

canvas.create_rectangle(
    -1.0,
    99.0,
    254.0,
    100.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -0.5,
    158.98580130134962,
    253.9999594380206,
    160.5,
    fill="#000000",
    outline="")

canvas.create_text(
    128.0,
    117.0,
    anchor="nw",
    text="City",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    110.0,
    250.0,
    anchor="nw",
    text="Courier",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    112.0,
    189.0,
    anchor="nw",
    text="History\n\n\n",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    89.0,
    302.0,
    anchor="nw",
    text="City to City",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    79.0,
    380.0,
    anchor="nw",
    text=" Safety",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_rectangle(
    -1.0,
    227.0,
    254.0,
    228.0,
    fill="#000000",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    54.0,
    197.0,
    image=image_image_3
)

canvas.create_rectangle(
    -1.0,
    283.98804797940375,
    253.99995480407506,
    286.0,
    fill="#000000",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    54.0,
    259.0,
    image=image_image_4
)

canvas.create_rectangle(
    -1.0,
    340.9421496746654,
    255.99977110151667,
    343.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    252.0,
    -1.0,
    255.99999977364922,
    547.9999800888982,
    fill="#000000",
    outline="")

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    42.0,
    313.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    47.0,
    395.0,
    image=image_image_6
)

canvas.create_rectangle(
    -1.0,
    427.00000001414446,
    255.99999879300594,
    431.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=47.0,
    y=473.0,
    width=153.0,
    height=45.0
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    239.0,
    37.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    344.0,
    67.0,
    image=image_image_8
)

canvas.create_text(
    318.0,
    114.0,
    anchor="nw",
    text="Moto",
    fill="#000000",
    font=("Inter", 24 * -1)
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    522.0,
    68.0,
    image=image_image_9
)

canvas.create_text(
    497.0,
    114.0,
    anchor="nw",
    text="Ride",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    914.0,
    126.0,
    anchor="nw",
    text="Ride",
    fill="#000000",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    667.0,
    123.0,
    anchor="nw",
    text="Delivery",
    fill="#000000",
    font=("Inter", 24 * -1)
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    697.0,
    67.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    929.0,
    63.0,
    image=image_image_11
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    674.0,
    255.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg = "#585858",
    fg="#FFFFFF",

    highlightthickness=0
)
entry_1.place(
    x=308.0,
    y=235.0,
    width=732.0,
    height=38.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    670.0,
    309.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg = "#585858",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=304.0,
    y=291.0,
    width=732.0,
    height=34.0
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    276.0,
    249.0,
    image=image_image_12
)

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    276.0,
    307.0,
    image=image_image_13
)

image_image_14 = PhotoImage(
    file=relative_to_assets("image_14.png"))
image_14 = canvas.create_image(
    276.0,
    307.0,
    image=image_image_14
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    670.0,
    360.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg = "#585858",
    fg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=304.0,
    y=343.0,
    width=732.0,
    height=32.0
)

image_image_15 = PhotoImage(
    file=relative_to_assets("image_15.png"))
image_15 = canvas.create_image(
    274.0,
    362.0,
    image=image_image_15
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=472.0,
    y=447.0,
    width=375.0,
    height=64.0
)

image_image_16 = PhotoImage(
    file=relative_to_assets("image_16.png"))
image_16 = canvas.create_image(
    398.0,
    479.0,
    image=image_image_16
)

image_image_17 = PhotoImage(
    file=relative_to_assets("image_17.png"))
image_17 = canvas.create_image(
    952.0,
    479.0,
    image=image_image_17
)
window.resizable(False, False)
window.mainloop()