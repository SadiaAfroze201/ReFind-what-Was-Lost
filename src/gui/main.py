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
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from src.core.storage import loadItems

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

#resize banner whn window chng
def resize_banner(event):
    global banner_photo
    new_width=event.width
    resized_img= banner_img.resize((new_width,250))
    banner_photo=ImageTk.PhotoImage(resized_img)
    banner_canvas.itemconfig(banner_img_id,image=banner_photo)



# put the image and text together
banner_canvas = tk.Canvas(
    banner_frame,
    height=250,
    highlightthickness=0,
    bd=0
)
banner_canvas.pack(fill="both", expand=True)

# banner image
banner_photo=ImageTk.PhotoImage(banner_img.resize((820,250)))
banner_img_id=banner_canvas.create_image(0,0,image=banner_photo,anchor="nw")

#resize banner to fit canvas
banner_canvas.bind("<Configure>",resize_banner)

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

# dashboard summary cards
cards_frame = tk.Frame(main_area, bg="#F8F3F8")
cards_frame.pack(fill="x", padx=25, pady=20)

#count items
items = loadItems()
lost_count = sum(1 for item in items if item["item_type"] == "lost")
found_count = sum(1 for item in items if item["item_type"] == "found")

for title, number in [
    ("Lost Items", lost_count),
    ("Found Items", found_count),
    ("Successful Matches", 0)
]:
    card = tk.Frame(cards_frame, bg="white", padx=20, pady=15)
    card.pack(side="left", fill="both", expand=True, padx=8)

    title_label = tk.Label(
        card,
        text=title,
        font=("Goudy Old Style", 24),
        bg="white",
        fg="#777777",
        justify="left"
    )
    title_label.pack(fill="x", anchor="w")

    # adjust title width when card changs size
    card.bind(
        "<Configure>",
        lambda event, label=title_label:
            label.config(wraplength=max(100, event.width - 40))
    )

    tk.Label(
        card,
        text=number,
        font=("Goudy Old Style", 26, "bold"),
        bg="white",
        fg="#30213F"
    ).pack(anchor="w")

# rcnt items sctn
recent_frame = tk.Frame(main_area, bg="#F8F3F8")
recent_frame.pack(fill="both", expand=True, padx=33, pady=(5, 25))

# sctn heading
heading_frame = tk.Frame(recent_frame, bg="#F8F3F8")
heading_frame.pack(fill="x", pady=(0, 0))

tk.Label(
    heading_frame,
    text="Recent Items",
    font=("Goudy Old Style", 27, "bold"),
    bg="#F8F3F8",
    fg="#30213F"
).pack(anchor="w")

# heading row
title_row = tk.Frame(heading_frame, bg="#F8F3F8")
title_row.pack(fill="x")


view_all = tk.Label(
    title_row,
    text="View All →",
    font=("Segoe UI", 14, "bold"),
    bg="#F8F3F8",
    fg="#76558A",
    cursor="hand2"
)
view_all.pack(side="right", padx=10)

# white table container
table_shell = tk.Frame(
    recent_frame,
    bg="white",
    highlightbackground="#E8E0EA",
    highlightthickness=1
)
table_shell.pack(fill="both", expand=True)


# table styling
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="white",
    foreground="#403747",
    fieldbackground="white",
    font=("Segoe UI", 10),
    rowheight=38,
    borderwidth=0
)

style.configure(
    "Treeview.Heading",
    background="#30213F",
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=(10, 12),
    relief="flat"
)

style.map(
    "Treeview.Heading",
    background=[
        ("active", "#30213F"),
        ("!active", "#30213F")
    ],
    foreground=[
        ("active", "white"),
        ("!active", "white")
    ]
)

style.map(
    "Treeview",
    background=[("selected", "#E8DDF0")],
    foreground=[("selected", "#30213F")]

)


# create table
columns = ("name", "type", "category", "location", "date", "status")

recent_table = ttk.Treeview(
    table_shell,
    columns=columns,
    show="headings",
    height=6
)

recent_table.heading("name", text="ITEM NAME", anchor="w")
recent_table.heading("type", text="TYPE", anchor="center")
recent_table.heading("category", text="CATEGORY", anchor="w")
recent_table.heading("location", text="LOCATION", anchor="w")
recent_table.heading("date", text="DATE", anchor="center")
recent_table.heading("status", text="STATUS", anchor="center")

# column widths
recent_table.column("name", width=150, minwidth=110, anchor="w")
recent_table.column("type", width=90, minwidth=75, anchor="center")
recent_table.column("category", width=120, minwidth=100, anchor="w")
recent_table.column("location", width=190, minwidth=130, anchor="w")
recent_table.column("date", width=115, minwidth=100, anchor="center")
recent_table.column("status", width=90, minwidth=75, anchor="center")


# row clrs
recent_table.tag_configure(
    "lost",
    background="#FFF1F0",
    foreground="#A33D3D"
)

recent_table.tag_configure(
    "found",
    background="#EAF7F0",
    foreground="#26734D"
)


# scrollbar
scrollbar = ttk.Scrollbar(
    table_shell,
    orient="vertical",
    command=recent_table.yview
)

recent_table.configure(yscrollcommand=scrollbar.set)

recent_table.pack(side="left", fill="both", expand=True, padx=(8, 0), pady=8)
scrollbar.pack(side="right", fill="y", padx=(0, 8), pady=8)


# sort newest reports first
recent_items = sorted(
    items,
    key=lambda item: item.get("date", ""),
    reverse=True
)


# display the latest 10 reports
for item in recent_items[:10]:

    # format date
    try:
        display_date = datetime.strptime(
            item.get("date", ""),
            "%Y-%m-%d"
        ).strftime("%d %b %Y")
    except ValueError:
        display_date = item.get("date", "N/A")

    item_type = item.get("item_type", "").lower()

    recent_table.insert(
        "",
        "end",
        values=(
            item.get("item_name", "N/A"),
            item_type.capitalize(),
            item.get("category", "N/A"),
            item.get("location", "N/A"),
            display_date,
            item.get("status", "N/A")
        ),
        tags=(item_type,)
    )


# message when there are no records
if not recent_items:
    recent_table.insert(
        "",
        "end",
        values=("No items reported yet", "", "", "", "", "")
    )


#keep the app running
window.mainloop()