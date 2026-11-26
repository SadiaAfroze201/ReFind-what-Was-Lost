"""
GenAI Acknowledgment (Assessment 1 - Assisted Reviewer):
In compliance with Keele University academic integrity policies, I used 
generative AI (Chatgpt) strictly as an assisted code reviewer and debugger. 
I consulted the tool to help diagnose runtime exceptions (such as Tkinter TclError 
and NameError), identify subtle typographical errors that were difficult to spot 
manually (e.g.first name is found_page_label, but the second is found_pge_label. The letter a is missing from page), and check 
function execution flow. I take help to understanding git and how to commit push and pull. 
As well as, i consulted with chatgpt during project architecture work and brainstorming.
All core logic, functional decisions, 
and final code implementations were independently written, tested, and verified by me.


Student Name: Sadia Afroze Zafrin
Student ID: 26032504
"""

# importing libraries needed for GUi
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
from src.core.storage import loadItems


# managing search bar placeholder text
def setup_search_placeholder(entry):

    placeholder = "Search by item name, category or location..."

    # removing placeholder when user clicks the search bar
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="#403747")

    # showing placeholder again if search bar is empty
    def on_focus_out(event):
        if not entry.get().strip():
            entry.insert(0, placeholder)
            entry.config(fg="#777777")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)



# crting the main aplictn window
window = tk.Tk()
window.title("ReFind || Lost & Found")
window.geometry("1100x700")
window.minsize(900, 600)
window.configure(bg="#F8F3F8")


# crting sidebar left side of aplictn
# it contain logo and navigatn buttons
side_bar = tk.Frame(window, bg="#30213F", width=280)
side_bar.pack(side="left", fill="y")
side_bar.pack_propagate(False)


# crting main area where different pages will appear
main_area = tk.Frame(window, bg="#F8F3F8")
main_area.pack(side="right", fill="both", expand=True)


# setting up separate frames for dashboard and lost items pages
# this makes it easier to switch between pages without opening new windows
dashboard_frame = tk.Frame(main_area, bg="#F8F3F8")
dashboard_frame.pack(fill="both", expand=True)

lost_items_frame = tk.Frame(main_area, bg="#F8F3F8")
found_items_frame=tk.Frame(main_area, bg="#F8F3F8")
# --------------------------------------------------
# LOST ITEMS PAGE
# --------------------------------------------------
# crting banner at top of Lost Items page
lost_banner_frame = tk.Frame(
    lost_items_frame,
    height=220,
    bg="#F8F3F8"
)
lost_banner_frame.pack(fill="x")
lost_banner_frame.pack_propagate(False)


# lding the banner img used on Dashboard
lost_banner_img = Image.open("assets/dashboard_banner.jpg")


# usng Canvas so heading and subtitle can be placed over img
lost_banner_canvas = tk.Canvas(
    lost_banner_frame,
    height=220,
    highlightthickness=0,
    bd=0
)
lost_banner_canvas.pack(fill="both", expand=True)


# resizing banner img when window size chngs
# this helps img fit available space
def resize_lost_banner(event):
    global lost_banner_photo

    resized_img = lost_banner_img.resize((event.width, 220))
    lost_banner_photo = ImageTk.PhotoImage(resized_img)

    lost_banner_canvas.itemconfig(
        lost_banner_img_id,
        image=lost_banner_photo
    )


# displaying the banner img
lost_banner_photo = ImageTk.PhotoImage(
    lost_banner_img.resize((820, 220))
)

lost_banner_img_id = lost_banner_canvas.create_image(
    0, 0,
    image=lost_banner_photo,
    anchor="nw"
)

lost_banner_canvas.bind("<Configure>", resize_lost_banner)


# adding a shadow behind lost items heading 
lost_banner_canvas.create_text(
    37, 67,
    text="Lost Items",
    font=("Goudy Old Style", 38, "bold"),
    fill="#50334F",
    anchor="w"
)

# displaying lost items heading
lost_banner_canvas.create_text(
    35, 65,
    text="Lost Items",
    font=("Goudy Old Style", 38, "bold"),
    fill="white",
    anchor="w"
)


# adding a shadow behind subtitle
lost_banner_canvas.create_text(
    37, 105,
    text="Find and reconnect with your missing belongings.",
    font=("Goudy Old Style", 18, "bold"),
    fill="#50334F",
    anchor="w"
)

# displaying short dscrption below heading
lost_banner_canvas.create_text(
    35, 103,
    text="Find and reconnect with your missing belongings.",
    font=("Goudy Old Style", 18, "bold"),
    fill="white",
    anchor="w"
)
# --------------------------------------------------
# FOUND ITEMS PAGE
# --------------------------------------------------
# crting banner at top of Found Items page
found_banner_frame = tk.Frame(
    found_items_frame,
    height=220,
    bg="#F8F3F8"
)
found_banner_frame.pack(fill="x")
found_banner_frame.pack_propagate(False)

# lding same banner img used on Lost Items page
found_banner_img = Image.open("assets/dashboard_banner.jpg")

# using Canvas to place text over img
found_banner_canvas = tk.Canvas(
    found_banner_frame,
    height=220,
    highlightthickness=0,
    bd=0
)
found_banner_canvas.pack(fill="both", expand=True)

# resizing banner img when window size chngs
def resize_found_banner(event):
    global found_banner_photo

    resized_img = found_banner_img.resize((event.width, 220))
    found_banner_photo = ImageTk.PhotoImage(resized_img)

    found_banner_canvas.itemconfig(
        found_banner_img_id,
        image=found_banner_photo
    )

# displaying banner img
found_banner_photo = ImageTk.PhotoImage(
    found_banner_img.resize((820, 220))
)

found_banner_img_id = found_banner_canvas.create_image(
    0, 0,
    image=found_banner_photo,
    anchor="nw"
)

found_banner_frame.bind("<Configure>", resize_found_banner)

# adding shadow behind Found Items heading
found_banner_canvas.create_text(
    37, 67,
    text="Found Items",
    font=("Goudy Old Style", 38, "bold"),
    fill="#50334F",
    anchor="w"
)

# displaying Found Items heading
found_banner_canvas.create_text(
    35, 65,
    text="Found Items",
    font=("Goudy Old Style", 38, "bold"),
    fill="white",
    anchor="w"
)

# adding shadow behind subtitle
found_banner_canvas.create_text(
    37, 105,
    text="Help lost belongings find their way home.",
    font=("Goudy Old Style", 18, "bold"),
    fill="#50334F",
    anchor="w"
)

# displaying short dscrption below heading
found_banner_canvas.create_text(
    35, 103,
    text="Help lost belongings find their way home.",
    font=("Goudy Old Style", 18, "bold"),
    fill="white",
    anchor="w"
)

# ------------------------------------------
#           FOUND SEARCH BAR
# ------------------------------------------

# creating shadow behind found search bar
found_srch_shadow = tk.Frame(
    found_banner_frame,
    bg="#D8C9DF"
)

# creating main search box
found_srch_box = tk.Frame(
    found_banner_frame,
    bg="white",
    highlightbackground="#E8DDEA",
    highlightthickness=1
)


# adjusting search bar position when banner size changes
def resize_found_srch_bar(event):
    srch_width = min(700, max(350, event.width - 70))
    srch_x = (event.width - srch_width) // 2

    found_srch_shadow.place(
        x=srch_x + 2,
        y=143,
        width=srch_width,
        height=55
    )

    found_srch_box.place(
        x=srch_x,
        y=140,
        width=srch_width,
        height=55
    )


found_banner_frame.bind("<Configure>", resize_found_srch_bar)


# adding search icon
tk.Label(
    found_srch_box,
    text="⌕",
    font=("Segoe UI", 25),
    bg="white",
    fg="#76558A"
).pack(side="left", padx=(16, 10))


# creating input field
found_srch_entry = tk.Entry(
    found_srch_box,
    font=("Segoe UI", 12),
    bg="white",
    fg="#777777",
    insertbackground="#30213F",
    relief="flat",
    bd=0
)

found_srch_entry.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)

found_srch_entry.insert(
    0,
    "Search by item name, category or location..."
)
setup_search_placeholder(found_srch_entry)

# creating found items search button
found_srch_button = tk.Button(
    found_srch_box,
    text="Search",
    font=("Segoe UI", 10, "bold"),
    bg="#76558A",
    fg="white",
    activebackground="#50334F",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=20,
    command=lambda: search_items(found_srch_entry, "found")
)

found_srch_button.pack(side="right", padx=6, pady=6)


# allowing search by pressing Enter
found_srch_entry.bind(
    "<Return>",
    lambda event: search_items(found_srch_entry, "found")
)

#------------------------------------------
#            LOST SEARCH BAR
#---------------------------------------------

# crting srch bar on top of banner
# shadow is added behind for little depth
srch_shadow = tk.Frame(
    lost_banner_frame,
    bg="#D8C9DF"
)

# main srch box
srch_box = tk.Frame(
    lost_banner_frame,
    bg="white",
    highlightbackground="#E8DDEA",
    highlightthickness=1
)


# adjusting srch bar position when banner size chngs
def resize_srch_bar(event):
    srch_width = min(700, max(350, event.width - 70))

    srch_x = (event.width - srch_width) // 2

    srch_shadow.place(
        x=srch_x + 2,
        y=143,
        width=srch_width,
        height=55
    )

    srch_box.place(
        x=srch_x,
        y=140,
        width=srch_width,
        height=55
    )


lost_banner_frame.bind("<Configure>", resize_srch_bar)


# adding a srch icon inside search box
tk.Label(
    srch_box,
    text="⌕",
    font=("Segoe UI", 25),
    bg="white",
    fg="#76558A"
).pack(side="left", padx=(16, 10))


# crting input field to enter search text
srch_entry = tk.Entry(
    srch_box,
    font=("Segoe UI", 12),
    bg="white",
    fg="#777777",
    insertbackground="#30213F",
    relief="flat",
    bd=0
)

srch_entry.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 8)
)

# showing what users can search for
srch_entry.insert(0, "Search by item name, category or location...")
setup_search_placeholder(srch_entry)


# cnncting the Srch button to srch fnction
srch_button = tk.Button(
    srch_box,
    text="Search",
    font=("Segoe UI", 10, "bold"),
    bg="#76558A",
    fg="white",
    activebackground="#50334F",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=20,
    command=lambda: search_items(srch_entry, "lost")
)

srch_button.pack(side="right", padx=6, pady=6)


# allowing users to search by pressing Enter
srch_entry.bind(
    "<Return>",
    lambda event: search_items(srch_entry, "lost")
)

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

# keeping track of all sidebar buttons
# this helps highlight page user is currently viewing
nav_buttons = []
slctd_nav_button = None


# fnction to switch between pages sidebar button is clicked
def show_page(page, slctd_button):
    global slctd_nav_button

    # hiding crrntly displayed pages
    # hiding currently displayed pages
    dashboard_frame.pack_forget()
    lost_items_frame.pack_forget()
    found_items_frame.pack_forget()

    # displaying page selected
    page.pack(fill="both", expand=True)

    # remembering which sidebar button is currently slcted
    slctd_nav_button = slctd_button

    # resetting all sidebar buttons to their normal clr
    for button in nav_buttons:
        button.config(bg="#30213F")

    # highlighting button for currently being viewed
    slctd_button.config(bg="#76558A")


# adding applcation logo and name to sidebar
logo_img = tk.PhotoImage(file="assets/ReFind Logo.png")
logo_img = logo_img.subsample(4, 4)

brand_box = tk.Frame(side_bar, bg="#30213F")
brand_box.pack(anchor="w", padx=15, pady=(30, 35))


# displaying logo on left side 
logo_label = tk.Label(
    brand_box,
    image=logo_img,
    bg="#30213F"
)
logo_label.pack(side="left", padx=(0, 8))


#crting navigation buttons for different sctions
for name in ["Dashboard", "Lost Items", "Found Items", "Contact Request"]:

    # connecting available buttons to their page frames
    if name == "Dashboard":
        page = dashboard_frame

    elif name == "Lost Items":
        page = lost_items_frame

    elif name == "Found Items":
        page = found_items_frame
    

    else:
        # these pages will connected when developed
        page = None

    nav_button = tk.Button(
        side_bar,
        text=name,
        font=("Goudy Old Style", 15),
        bg="#30213F",
        fg="white",
        activebackground="#76558A",
        activeforeground="white",
        relief="flat",
        anchor="w",
        padx=25,
        pady=12,
        cursor="hand2",
        command=lambda p=page, b=None: None
    )

    nav_button.pack(fill="x", padx=10, pady=3)

    # saving each button so its clr can updated later
    nav_buttons.append(nav_button)

   # connecting buttons that already have working pages
    if page is not None:

        if name == "Found Items":
            nav_button.config(
                command=lambda b=nav_button: (
                    show_found_page(0),
                    show_page(found_items_frame, b)
                )
            )

        else:
            nav_button.config(
                command=lambda p=page, b=nav_button: show_page(p, b)
            )

        
    # chnging button clr when mouse moves over it
    nav_button.bind(
        "<Enter>",
        lambda event, button=nav_button:
            button.config(bg="#76558A")
    )

    # keeping the slctd page highlighted when mouse leaves
    # other buttons return to their normal colour
    nav_button.bind(
        "<Leave>",
        lambda event, button=nav_button:
            button.config(
                bg="#76558A" if button == slctd_nav_button
                else "#30213F"
            )
    )


# --------------------------------------------------
# DASHBOARD PAGE
# --------------------------------------------------

# crting the dashboard banner area
banner_frame = tk.Frame(dashboard_frame, height=250)
banner_frame.pack(fill="x")
banner_frame.pack_propagate(False)


# loading background img for dashboard
banner_img = Image.open("assets/dashboard_banner.jpg")


# resizing banner image to fit available window width
def resize_banner(event):
    global banner_photo

    new_width = event.width
    resized_img = banner_img.resize((new_width, 250))
    banner_photo = ImageTk.PhotoImage(resized_img)

    banner_canvas.itemconfig(
        banner_img_id,
        image=banner_photo
    )


# using Canvas to place text over Dashboard banner
banner_canvas = tk.Canvas(
    banner_frame,
    height=250,
    highlightthickness=0,
    bd=0
)
banner_canvas.pack(fill="both", expand=True)


# displaying Dashboard banner img
banner_photo = ImageTk.PhotoImage(banner_img.resize((820, 250)))

banner_img_id = banner_canvas.create_image(
    0, 0,
    image=banner_photo,
    anchor="nw"
)

# resizing the banner whenever the canvas size changes
banner_canvas.bind("<Configure>", resize_banner)


# adding a shadow behind Dashboard heading
banner_canvas.create_text(
    37, 67,
    text="Dashboard",
    font=("Goudy Old Style", 38, "bold"),
    fill="#50334F",
    anchor="w"
)

# displaying dashboard heading
banner_canvas.create_text(
    35, 65,
    text="Dashboard",
    font=("Goudy Old Style", 38, "bold"),
    fill="#FFFFFF",
    anchor="w"
)


# adding shadow behind wlcme msg
banner_canvas.create_text(
    37, 105,
    text="A little search can lead to a happy reunion.",
    font=("Goudy Old Style", 20, "bold"),
    fill="#50334F",
    anchor="w"
)

# displaying wlcm msg
banner_canvas.create_text(
    35, 103,
    text="A little search can lead to a happy reunion.",
    font=("Goudy Old Style", 20, "bold"),
    fill="#FFFFFF",
    anchor="w"
)


# --------------------------------------------------
# DASHBOARD SUMMARY CARDS
# --------------------------------------------------

# crting area for three summary cards
cards_frame = tk.Frame(dashboard_frame, bg="#F8F3F8")
cards_frame.pack(fill="x", padx=25, pady=20)


# loading saved item records from JSON storage
items = loadItems()

# counting lost and found items separately
lost_count = sum(1 for item in items if item["item_type"] == "lost")
found_count = sum(1 for item in items if item["item_type"] == "found")


# crting summary cards to show current item counts
for title, number in [
    ("Lost Items", lost_count),
    ("Found Items", found_count),
    ("Successful Matches", 0)
]:
    card = tk.Frame(cards_frame, bg="white", padx=20, pady=15)
    card.pack(side="left", fill="both", expand=True, padx=8)

    # displaying title of each summary card
    title_label = tk.Label(
        card,
        text=title,
        font=("Goudy Old Style", 24),
        bg="white",
        fg="#777777",
        justify="left"
    )
    title_label.pack(fill="x", anchor="w")

    # adjusting title width when card size changes
    card.bind(
        "<Configure>",
        lambda event, label=title_label:
            label.config(wraplength=max(100, event.width - 40))
    )

    # displaying nmbr for each summary card
    tk.Label(
        card,
        text=number,
        font=("Goudy Old Style", 26, "bold"),
        bg="white",
        fg="#30213F"
    ).pack(anchor="w")


# --------------------------------------------------
# RECENT ITEMS SECTION
# --------------------------------------------------

# crting Rcnt items sction on the dashboard
recent_frame = tk.Frame(dashboard_frame, bg="#F8F3F8")
recent_frame.pack(fill="both", expand=True, padx=33, pady=(5, 25))


# adding sction heading
heading_frame = tk.Frame(recent_frame, bg="#F8F3F8")
heading_frame.pack(fill="x", pady=(0, 0))

tk.Label(
    heading_frame,
    text="Recent Items",
    font=("Goudy Old Style", 27, "bold"),
    bg="#F8F3F8",
    fg="#30213F"
).pack(anchor="w")


# crting row for heading and view all label
title_row = tk.Frame(heading_frame, bg="#F8F3F8")
title_row.pack(fill="x")


# adding view all label beside sction heading
view_all = tk.Label(
    title_row,
    text="View All →",
    font=("Segoe UI", 14, "bold"),
    bg="#F8F3F8",
    fg="#76558A",
    cursor="hand2"
)
view_all.pack(side="right", padx=10)


# crting white container for rcnt items table
table_shell = tk.Frame(
    recent_frame,
    bg="white",
    highlightbackground="#E8E0EA",
    highlightthickness=1
)
table_shell.pack(fill="both", expand=True)


# Setting the appearance of the table
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

# Styling table headings
style.configure(
    "Treeview.Heading",
    background="#30213F",
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=(10, 12),
    relief="flat"
)

# Keeping heading clr same when mouse moves over it
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

# chnging row clr when user selects it
style.map(
    "Treeview",
    background=[("selected", "#E8DDF0")],
    foreground=[("selected", "#30213F")]
)


# dfining columns that will appear rcnt items table
columns = ("name", "type", "category", "location", "date", "status")

recent_table = ttk.Treeview(
    table_shell,
    columns=columns,
    show="headings",
    height=6
)


# adding headings for each clmn
recent_table.heading("name", text="ITEM NAME", anchor="w")
recent_table.heading("type", text="TYPE", anchor="center")
recent_table.heading("category", text="CATEGORY", anchor="w")
recent_table.heading("location", text="LOCATION", anchor="w")
recent_table.heading("date", text="DATE", anchor="center")
recent_table.heading("status", text="STATUS", anchor="center")


# setting width and alignment of each clmn
recent_table.column("name", width=150, minwidth=110, anchor="w")
recent_table.column("type", width=90, minwidth=75, anchor="center")
recent_table.column("category", width=120, minwidth=100, anchor="w")
recent_table.column("location", width=190, minwidth=130, anchor="w")
recent_table.column("date", width=115, minwidth=100, anchor="center")
recent_table.column("status", width=90, minwidth=75, anchor="center")


# giving lost and found records different row colours
# This makes it easier to tell two types apart
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


# adding scrollbar so users can view more records
scrollbar = ttk.Scrollbar(
    table_shell,
    orient="vertical",
    command=recent_table.yview
)

recent_table.configure(yscrollcommand=scrollbar.set)

recent_table.pack(side="left", fill="both", expand=True, padx=(8, 0), pady=8)
scrollbar.pack(side="right", fill="y", padx=(0, 8), pady=8)


# sorting records by date so newest reports appear first
recent_items = sorted(
    items,
    key=lambda item: item.get("date", ""),
    reverse=True
)


# displaying latest 10 reports in table
for item in recent_items[:10]:

    # cnverting date into more readable format
    try:
        display_date = datetime.strptime(
            item.get("date", ""),
            "%Y-%m-%d"
        ).strftime("%d %b %Y")
    except ValueError:
        # keeping original date if it cannot be formatted
        display_date = item.get("date", "N/A")

    item_type = item.get("item_type", "").lower()

    # adding item details as new row in table
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


# showing msg when there are no item records available
if not recent_items:
    recent_table.insert(
        "",
        "end",
        values=("No items reported yet", "", "", "", "", "")
    )


# --------------------------------------------------
# LOST & FOUND ITEMS CARDS AND PAGINATION
# --------------------------------------------------

# getting only lost item records from saved data
lost_records = [
    item for item in items
    if item.get("item_type", "").lower() == "lost"
]

# showing 3 item cards on each page
cards_per_page = 3
current_page = 0


# setting clrs used throughout item cards
card_bg = "#FFFFFF"
card_border = "#E8E0EA"
purple = "#30213F"
lavender = "#F0EAF4"
muted_text = "#95869F"


# creating frame that will hold lost item cards
lost_cards_frame = tk.Frame(
    lost_items_frame,
    bg="#F8F3F8"
)
lost_cards_frame.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=(15, 5)
)


# dividing available space into three equal clmns
for column in range(cards_per_page):
    lost_cards_frame.grid_columnconfigure(
        column,
        weight=1,
        uniform="lost_card"
    )


# crting page navigation controls below cards
lost_page_controls = tk.Frame(
    lost_items_frame,
    bg="#F8F3F8"
)
lost_page_controls.pack(pady=(5, 18))

# getting only found item records from saved data
found_records = [
    item for item in items
    if item.get("item_type", "").lower() == "found"
]

# crting frame that will hold found item cards
found_cards_frame = tk.Frame(
    found_items_frame,
    bg="#F8F3F8"
)
found_cards_frame.pack(
    fill="both",
    expand=True,
    padx=22,
    pady=(15, 5)
)

# dividing available space into 3 equal clmns
for column in range(cards_per_page):
    found_cards_frame.grid_columnconfigure(
        column,
        weight=1,
        uniform="found_card"
    )

# crting page navigation controls below cards
found_page_controls = tk.Frame(
    found_items_frame,
    bg="#F8F3F8"
)
found_page_controls.pack(pady=(5, 18))

# keeping track of current found items page
current_found_page = 0

#crting Previous button to move to earlier page
found_previous_button = tk.Button(
    found_page_controls,
    text="<",
    font=("Segoe UI", 11),
    bg="#E9E0EF",
    fg=purple,
    activebackground="#D9C9E5",
    relief="flat",
    width=3,
    cursor="hand2",
    command=lambda: show_found_page(current_found_page - 1)
)
found_previous_button.pack(side="left", padx=5)

# Shwing crrnt page nmbr
found_page_label = tk.Label(
    found_page_controls,
    font=("Segoe UI", 10, "bold"),
    bg="#F8F3F8",
    fg=purple
)
found_page_label.pack(side="left", padx=12)


#crting nxt button to move following page
found_next_button = tk.Button(
    found_page_controls,
    text="›",
    font=("Segoe UI", 18, "bold"),
    bg="#E9E0EF",
    fg=purple,
    activebackground="#D9C9E5",
    relief="flat",
    width=3,
    cursor="hand2",
    command=lambda: show_lost_page(current_page + 1)
)
found_next_button.pack(side="left", padx=5)

# --------------------------------------------------
# SEARCH LOST & found ITEMS
# --------------------------------------------------
# searching through lost and found item records
def search_items(search_entry, item_type):

    global lost_records, found_records

    # getting search text and converting it to lowercase
    search_text = search_entry.get().strip().lower()

    # loading latest saved records
    all_items = loadItems()

    # keeping records that match the search
    matching_records = [
        item for item in all_items
        if item.get("item_type", "").lower() == item_type
        and (
            search_text in item.get("item_name", "").lower()
            or search_text in item.get("category", "").lower()
            or search_text in item.get("location", "").lower()
        )
    ]

    # updating the correct item records
    if item_type == "lost":
        lost_records = matching_records
        show_lost_page(0)

    else:
        found_records = matching_records
        show_found_page(0)
# --------------------------------------------------
# DISPLAY ITEM CARDS
# --------------------------------------------------
# creating a reusable card for lost and found items
def create_item_card(parent, item, status):

    # main card container
    card = tk.Frame(
        parent,
        bg=card_bg,
        highlightbackground=card_border,
        highlightthickness=1,
        bd=0
    )

    # adding small purple accent at top
    tk.Frame(
        card,
        bg="#8B6AAE",
        height=5
    ).pack(fill="x")

    # photo placeholder
    photo_area = tk.Frame(
        card,
        bg=lavender,
        height=105
    )
    photo_area.pack(fill="x", padx=12, pady=(12, 5))
    photo_area.pack_propagate(False)

    tk.Label(
        photo_area,
        text="＋",
        font=("Segoe UI", 25),
        bg=lavender,
        fg="#B5A1C6"
    ).pack(pady=(12, 0))

    tk.Label(
        photo_area,
        text="PHOTO",
        font=("Segoe UI", 8, "bold"),
        bg=lavender,
        fg=muted_text
    ).pack()

    # item name and status
    heading = tk.Frame(card, bg=card_bg)
    heading.pack(fill="x", padx=13, pady=(8, 2))

    tk.Label(
        heading,
        text=item.get("item_name", "Unnamed item"),
        font=("Goudy Old Style", 18, "bold"),
        bg=card_bg,
        fg=purple,
        anchor="w",
        wraplength=175,
        justify="left"
    ).pack(side="left", fill="x", expand=True)

    # choosing status colour
    if status == "LOST":
        status_bg = "#F7E8ED"
        status_fg = "#A34D68"
    else:
        status_bg = "#E7F2E9"
        status_fg = "#477B55"

    tk.Label(
        heading,
        text=status,
        font=("Segoe UI", 8, "bold"),
        bg=status_bg,
        fg=status_fg,
        padx=7,
        pady=3
    ).pack(side="right", padx=(5, 0))

    # item description
    tk.Label(
        card,
        text=item.get("description", "No description provided"),
        font=("Segoe UI", 9),
        bg=card_bg,
        fg="#77717D",
        anchor="w",
        justify="left",
        wraplength=205
    ).pack(fill="x", padx=13, pady=(2, 10))

    # divider
    tk.Frame(
        card,
        bg="#EEE8F1",
        height=1
    ).pack(fill="x", padx=13, pady=(0, 7))

    # collecting extra item details
    details = [
        ("Category", item.get("category", "N/A")),
        ("Colour", item.get("color", "N/A")),
        ("Location", item.get("location", "N/A")),
        ("Date", item.get("date", "N/A"))
    ]

    # displaying each detail
    for label_text, value in details:
        detail_row = tk.Frame(card, bg=card_bg)
        detail_row.pack(fill="x", padx=13, pady=3)

        tk.Label(
            detail_row,
            text=label_text.upper(),
            font=("Segoe UI", 8, "bold"),
            bg=card_bg,
            fg=muted_text,
            anchor="w"
        ).pack(side="left")

        tk.Label(
            detail_row,
            text=value,
            font=("Segoe UI", 8),
            bg=card_bg,
            fg="#403747",
            anchor="e",
            wraplength=125,
            justify="right"
        ).pack(side="right")

    # changing card border colour on hover
    def card_enter(event):
        card.configure(highlightbackground="#9A7BB5")

    def card_leave(event):
        card.configure(highlightbackground=card_border)

    card.bind("<Enter>", card_enter)
    card.bind("<Leave>", card_leave)

    return card
#displaying lost item cards for slcted page
def show_lost_page(page):
    global current_page

    # calculating how many pages are needed
    #based on nmbr of lost item records
    total_pages = max(
        1,
        (len(lost_records) + cards_per_page - 1) // cards_per_page
    )

    #making sure sleted page is within available  range
    current_page = max(0, min(page, total_pages - 1))

    #removing  cards from previous page before showing new ones
    for widget in lost_cards_frame.winfo_children():
        widget.destroy()

    # Displaying a message if no lost items are available
    if not lost_records:
        tk.Label(
            lost_cards_frame,
            text="No lost items have been reported yet.",
            font=("Segoe UI", 12),
            bg="#F8F3F8",
            fg="#777777"
        ).grid(row=0, column=0, columnspan=3, pady=35)

    else:
        #finding which 3 records should appear on  crrnt page
        start_index = current_page * cards_per_page
        page_items = lost_records[start_index:start_index + cards_per_page]

        # creating cards using the shared function
        for column, item in enumerate(page_items):
            card = create_item_card(lost_cards_frame, item, "LOST")

            card.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=7,
                pady=7
            )
            
            
    # updating page number and arrow buttons
    #arrows are disabled when there are no more pages to visit
    page_label.config(text=f"{current_page + 1} / {total_pages}")

    previous_button.config(
        state="normal" if current_page > 0 else "disabled"
    )

    next_button.config(
        state="normal" if current_page < total_pages - 1 else "disabled"
    )


# displaying found item cards for slcted page
def show_found_page(page):
    global current_found_page

    # calculating how many pages are needed
    total_pages = max(
        1,
        (len(found_records) + cards_per_page - 1) // cards_per_page
    )

    # making sure selected page is within available range
    current_found_page = max(0, min(page, total_pages - 1))

    # removing cards from previous page
    for widget in found_cards_frame.winfo_children():
        widget.destroy()

    # displaying message if no found items are available
    if not found_records:
        tk.Label(
            found_cards_frame,
            text="No found items have been reported yet.",
            font=("Segoe UI", 12),
            bg="#F8F3F8",
            fg="#777777"
        ).grid(row=0, column=0, columnspan=3, pady=35)

    else:
        # finding which 3 records should appear on current page
        start_index = current_found_page * cards_per_page
        page_items = found_records[
            start_index:start_index + cards_per_page
        ]

        # creating cards using the shared function
        for column, item in enumerate(page_items):
            card = create_item_card(found_cards_frame, item, "FOUND")

            card.grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=7,
                pady=7
            )


    # updating page number and arrow buttons
    found_page_label.config(
        text=f"{current_found_page + 1} / {total_pages}"
    )

    found_previous_button.config(
        state="normal" if current_found_page > 0 else "disabled"
    )

    found_next_button.config(
        state="normal" if current_found_page < total_pages - 1 else "disabled"
    )

#crting Previous button to move to earlier page
previous_button = tk.Button(
    lost_page_controls,
    text="‹",
    font=("Segoe UI", 18, "bold"),
    bg="#E9E0EF",
    fg=purple,
    activebackground="#D9C9E5",
    relief="flat",
    width=3,
    cursor="hand2",
    command=lambda: show_lost_page(current_page - 1)
)
previous_button.pack(side="left", padx=10)


# Shwing crrnt page nmbr
page_label = tk.Label(
    lost_page_controls,
    text="1 / 1",
    font=("Segoe UI", 10, "bold"),
    bg="#F8F3F8",
    fg=purple
)
page_label.pack(side="left", padx=10)


#crting nxt button to move following page
next_button = tk.Button(
    lost_page_controls,
    text="›",
    font=("Segoe UI", 18, "bold"),
    bg="#E9E0EF",
    fg=purple,
    activebackground="#D9C9E5",
    relief="flat",
    width=3,
    cursor="hand2",
    command=lambda: show_lost_page(current_page + 1)
)
next_button.pack(side="left", padx=10)


#displaying first page of lost items when application starts
show_lost_page(0)

# displaying first page of found items
show_found_page(0)


# opening dashboard as default page
show_page(dashboard_frame, nav_buttons[0])


# keeping application running and waiting for user actions
window.mainloop()
