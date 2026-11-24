"""
Generative AI Acknowledgement:
ChatGPT (OpenAI) was used to support the planning and development of this
project through brainstorming, explaining programming concepts, clarifying
technical questions, and providing guidance on Git setup and version control.
All application code was independently written, implemented, and tested by
the student.

Student Name: Sadia Afroze Zafrin
Student ID: 26032504
"""

import tkinter as tk
from PIL import Image, ImageTk

#main windows stuffs
window =tk.Tk()
window.title("ReFind || Lost & Found")
window.geometry("1100x700")
window.minsize(900, 600)
window.configure(bg="#F8F3F8")

#set up sidebar things
side_bar=tk.Frame(window,bg="#30213F",width=280)
side_bar.pack(side="left",fill="y")
side_bar.pack_propagate(False)

# main dashboard area
main_area = tk.Frame(window, bg="#F8F3F8")
main_area.pack(side="right", fill="both", expand=True)


#set app name and logo
logo_img = tk.PhotoImage(file="assets/ReFind Logo.png")
logo_img = logo_img.subsample(4,4)

brand_box = tk.Frame(side_bar, bg="#30213F")
brand_box.pack(anchor="w", padx=15, pady=(30, 35))

# logo on the left
logo_label = tk.Label(
    brand_box,
    image=logo_img,
    bg="#30213F"
)
logo_label.pack(side="left", padx=(0, 8))



#set sidebar button
for name in["Dashboard", "Lost Items", "Found Items","Contact Request"]:
    tk.Button(
        side_bar,
        text=name,
        font=("Goudy Old Style",15),
        bg= "#30213F",
        fg="white",
        activebackground="#50334F",
        activeforeground="white",
        relief="flat",
        anchor="w",
        padx=25,
        pady=12
    ).pack(fill="x",padx=10,pady=3)

#dashboard banner area
banner_frame = tk.Frame(main_area, height=250)
banner_frame.pack(fill="x")
banner_frame.pack_propagate(False)

# load and resize the banner image
banner_img = Image.open("assets/dashboard_banner.jpg")
banner_img = banner_img.resize((820, 250))
banner_photo = ImageTk.PhotoImage(banner_img)

# put the image and text together
banner_canvas = tk.Canvas(
    banner_frame,
    height=250,
    highlightthickness=0,
    bd=0
)
banner_canvas.pack(fill="both", expand=True)

# banner image
banner_canvas.create_image(
    0, 0,
    image=banner_photo,
    anchor="nw"
)

# dashboard heading shadow
banner_canvas.create_text(
    37, 67,
    text="Dashboard",
    font=("Goudy Old Style", 38, "bold"),
    fill="#50334F",
    anchor="w"
)

# dashboard heading
banner_canvas.create_text(
    35, 65,
    text="Dashboard",
    font=("Goudy Old Style", 38, "bold"),
    fill="#FFFFFF",
    anchor="w"
)

# welcome message shadow
banner_canvas.create_text(
    37, 105,
    text="A little search can lead to a happy reunion.",
    font=("Goudy Old Style", 20, "bold"),
    fill="#50334F",
    anchor="w"
)

# welcome message
banner_canvas.create_text(
    35, 103,
    text="A little search can lead to a happy reunion.",
    font=("Goudy Old Style", 20,"bold"),
    fill="#FFFFFF",
    anchor="w"
)
#keep the app running

window.mainloop()