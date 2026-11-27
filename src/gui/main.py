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
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from datetime import datetime
from src.core.storage import loadItems, saveItems
from src.core.item_manager import registerItem
import os
from src.core.item_search import searchItems


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

found_banner_canvas.bind("<Configure>", resize_found_banner)

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

# function to open item registration form
def open_registration_form():

    # creating a new window for item registration
    registration_window = tk.Toplevel(window)
    registration_window.title("Register Lost or Found Item")
    registration_window.geometry("650x700")
    registration_window.configure(bg="#F8F3F8")

    # keeping the registration window above the main window
    registration_window.transient(window)
    registration_window.grab_set()

    # creating canvas for scrollable form
    form_canvas = tk.Canvas(
        registration_window,
        bg="#F8F3F8",
        highlightthickness=0
    )
    form_canvas.pack(side="left", fill="both", expand=True)

    # adding vertical scrollbar
    form_scrollbar = ttk.Scrollbar(
        registration_window,
        orient="vertical",
        command=form_canvas.yview
    )
    form_scrollbar.pack(side="right", fill="y")

    form_canvas.configure(
        yscrollcommand=form_scrollbar.set
    )

    # crting frame inside the canvas
    form_frame = tk.Frame(
        form_canvas,
        bg="#F8F3F8"
    )

    form_canvas_window = form_canvas.create_window(
        (0, 0),
        window=form_frame,
        anchor="nw"
    )
    # adding space around form content
    form_frame.configure(padx=40, pady=10)

    # updating scroll area whenform content changes

    def update_scroll_region(event):
        form_canvas.configure(
            scrollregion=form_canvas.bbox("all")
        )

    form_frame.bind("<Configure>", update_scroll_region)

    # making form frame match canvas width
    def resize_form(event):
        form_canvas.itemconfig(
            form_canvas_window,
            width=event.width
        )

    form_canvas.bind("<Configure>", resize_form)

    # creating the main heading
    tk.Label(
        form_frame,
        text="Report a Lost or Found Item",
        font=("Goudy Old Style", 25, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(pady=(25, 5))

    # adding a short description
    tk.Label(
        form_frame,
        text="Please provide the details of the item below.",
        font=("Segoe UI", 10),
        bg="#F8F3F8",
        fg="#76558A"
    ).pack(pady=(0, 20))

    # item type label
    tk.Label(
        form_frame,
        text="Item Type *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(5, 5))

    # dropdown for selecting lost or found
    item_type_entry = ttk.Combobox(
        form_frame,
        values=["Lost", "Found"],
        state="readonly",
        font=("Segoe UI", 11)
    )
    item_type_entry.pack(fill="x", ipady=7)
    item_type_entry.set("Select Item Type")

    # item name label
    tk.Label(
        form_frame,
        text="Item Name *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # entry field for item name
    item_name_entry = tk.Entry(
        form_frame,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    )
    item_name_entry.pack(fill="x", ipady=7)

    # category label
    tk.Label(
        form_frame,
        text="Category *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # dropdown for selecting item category
    category_entry = ttk.Combobox(
        form_frame,
        values=[
            "Electronics",
            "Clothing",
            "Bags",
            "Accessories",
            "Documents",
            "Keys",
            "Other"
        ],
        state="readonly",
        font=("Segoe UI", 11)
    )
    category_entry.pack(fill="x", ipady=7)
    category_entry.set("Select Category")

    # colour label
    tk.Label(
        form_frame,
        text="Colour *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # entry field for item colour
    color_entry = tk.Entry(
        form_frame,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    )
    color_entry.pack(fill="x", ipady=7)

    # brand label
    tk.Label(
        form_frame,
        text="Brand (Optional)",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # entry field for item brand
    brand_entry = tk.Entry(
        form_frame,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    )
    brand_entry.pack(fill="x", ipady=7)
    # location label
    tk.Label(
        form_frame,
        text="Location *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # entry field for item location
    location_entry = tk.Entry(
        form_frame,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    )
    location_entry.pack(fill="x", ipady=7)

    # date label
    tk.Label(
        form_frame,
        text="Date (YYYY-MM-DD) *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # entry field with today's date as the default
    date_entry = tk.Entry(
        form_frame,
        font=("Segoe UI", 11),
        relief="solid",
        bd=1
    )
    date_entry.pack(fill="x", ipady=7)
    date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

    # variable to store the selected photo path
    selected_photo = tk.StringVar(value="")

    # photo section heading
    tk.Label(
        form_frame,
        text="Item Photo (Optional)",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # label to display selected photo name
    photo_name_label = tk.Label(
        form_frame,
        text="No photo selected",
        font=("Segoe UI", 9),
        bg="#F8F3F8",
        fg="#76558A"
    )
    photo_name_label.pack(anchor="w", pady=3)

    # image preview label
    photo_preview_label = tk.Label(
        form_frame,
        text="Photo Preview",
        font=("Segoe UI", 9),
        bg="white",
        fg="#76558A",
        width=25,
        height=6
    )
    photo_preview_label.pack(anchor="w", pady=5)

    # function to upload and preview an item photo
    def upload_photo():

        photo_path = filedialog.askopenfilename(
            parent=registration_window,
            title="Select Item Photo",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")
            ]
        )

        # checking whether a photo was selected
        if not photo_path:
            return

        try:
            # opening and resizing the selected image
            image = Image.open(photo_path)
            image.thumbnail((180, 120))

            # converting image for Tkinter
            photo_image = ImageTk.PhotoImage(image)

            # displaying the image preview
            photo_preview_label.config(
                image=photo_image,
                text="",
                width=180,
                height=120
            )

            # keeping a reference to prevent the image disappearing
            photo_preview_label.image = photo_image

            # storing the selected photo path
            selected_photo.set(photo_path)

            # displaying the selected filename
            photo_name_label.config(
                text=photo_path.replace("\\", "/").split("/")[-1]
            )

        except Exception:
            messagebox.showerror(
                "Invalid Photo",
                "Unable to open this image. Please select another photo.",
                parent=registration_window
            )

    # button to upload an item photo
    tk.Button(
        form_frame,
        text="Upload Photo",
        font=("Segoe UI", 10, "bold"),
        bg="#76558A",
        fg="white",
        activebackground="#30213F",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=upload_photo
    ).pack(anchor="w", pady=8)

    # description label
    tk.Label(
        form_frame,
        text="Description *",
        font=("Segoe UI", 11, "bold"),
        bg="#F8F3F8",
        fg="#30213F"
    ).pack(anchor="w", pady=(15, 5))

    # text area for item description
    description_entry = tk.Text(
        form_frame,
        font=("Segoe UI", 11),
        height=4,
        relief="solid",
        bd=1,
        wrap="word"
    )
    description_entry.pack(fill="x")
    # function to submit the registered item
    def submit_item():

        # collecting information from the form
        item_type = item_type_entry.get().strip().lower()
        item_name = item_name_entry.get().strip()
        category = category_entry.get().strip()
        color = color_entry.get().strip()
        brand = brand_entry.get().strip()
        location = location_entry.get().strip()
        date = date_entry.get().strip()
        description = description_entry.get("1.0", "end").strip()

        # loading existing records
        items = loadItems()

        # registering the new item using the core function
        new_item = registerItem(
            items,
            item_type,
            item_name,
            category,
            color,
            brand,
            location,
            date,
            description,
            selected_photo.get() or None
        )

        # checking whether registration was successful
        if new_item is None:
            messagebox.showerror(
                "Registration Failed",
                "Please check all required fields and enter a valid date in YYYY-MM-DD format.",
                parent=registration_window
            )
            return

        # saving the updated records
        saveItems(items)

        # refreshing dashboard and item pages
        refresh_item_records()

        # showing successful registration message
        messagebox.showinfo(
            "Registration Successful",
            f"Your item has been registered successfully!\nItem ID: {new_item['item_ID']}",
            parent=registration_window
        )

        # closing the registration window
        registration_window.destroy()

    # creating the register button
    tk.Button(
        form_frame,
        text="Register Item",
        font=("Segoe UI", 12, "bold"),
        bg="#30213F",
        fg="white",
        activebackground="#76558A",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        command=submit_item
    ).pack(fill="x", pady=25, ipady=10)

# ----------------------------------------------------
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



# creating navigation buttons for different sections
for name in ["Dashboard","Register Lost or Found Item","Lost Items","Found Items","Contact Request"]:
    # connecting available buttons to their page frames
    if name == "Dashboard":
        page = dashboard_frame

    elif name == "Lost Items":
        page = lost_items_frame

    elif name == "Found Items":
        page = found_items_frame

    else:
        page = None

    # creating sidebar button
    nav_button = tk.Button(
        side_bar,
        text=name,
        font=("Goudy Old Style", 15, "bold" if name == "Register Lost or Found Item" else "normal"),
        bg="#30213F",
        fg="white",
        activebackground="#8D6AA3",
        activeforeground="white",
        relief="flat",
        anchor="w",
        padx=25,
        pady=12,
        cursor="hand2"
    )

    nav_button.pack(fill="x", padx=10, pady=3)

    # saving page navigation buttons for highlighting
    if page is not None:
        nav_buttons.append(nav_button)

    # connecting the registration button
    if name == "Register Lost or Found Item":
        nav_button.config(
            command=lambda: open_registration_form()
        )

    # connecting buttons that already have working pages
    elif page is not None:

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

    # changing button colour when mouse moves over it
    nav_button.bind(
        "<Enter>",
        lambda event, button=nav_button:
            button.config(bg="#8D6AA3")
    )

    # restoring the correct colour when mouse leaves
    nav_button.bind(
        "<Leave>",
        lambda event, button=nav_button:
            button.config(
                bg=(
                    "#76558A"
                    if button == slctd_nav_button
                    else "#30213F"
                )
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
summary_count_labels = {}
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

    # displaying number for each summary card
    number_label = tk.Label(
        card,
        text=number,
        font=("Goudy Old Style", 26, "bold"),
        bg="white",
        fg="#30213F"
    )
    number_label.pack(anchor="w")

    # keeping a reference so the number can be updated later
    summary_count_labels[title] = number_label


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

# refreshing dashboard information using the latest saved records
def refresh_dashboard():

    # loading the latest records from JSON storage
    latest_items = loadItems()

    # updating lost and found item counts
    lost_count = sum(
        1 for item in latest_items
        if item.get("item_type", "").lower() == "lost"
    )

    found_count = sum(
        1 for item in latest_items
        if item.get("item_type", "").lower() == "found"
    )

    # updating the summary card numbers
    summary_count_labels["Lost Items"].config(text=lost_count)
    summary_count_labels["Found Items"].config(text=found_count)

    # removing old rows from the recent items table
    for row in recent_table.get_children():
        recent_table.delete(row)

    # sorting the latest records by date
    latest_recent_items = sorted(
        latest_items,
        key=lambda item: item.get("date", ""),
        reverse=True
    )

    # displaying the latest 10 records
    for item in latest_recent_items[:10]:

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

    # showing a message when no records are available
    if not latest_recent_items:
        recent_table.insert(
            "",
            "end",
            values=("No items reported yet", "", "", "", "", "")
        )

# refreshing all item records and pages
def refresh_item_records():

    global items, lost_records, found_records

    # loading the latest saved records
    items = loadItems()

    # separating lost and found records
    lost_records = [
        item for item in items
        if item.get("item_type", "").lower() == "lost"
    ]

    found_records = [
        item for item in items
        if item.get("item_type", "").lower() == "found"
    ]

    # refreshing both item pages
    show_lost_page(0)
    show_found_page(0)

    # refreshing dashboard counts and recent items
    refresh_dashboard()
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
    command=lambda: show_found_page(current_found_page + 1)
)
found_next_button.pack(side="left", padx=5)

# --------------------------------------------------
# SEARCH LOST & found ITEMS
# --------------------------------------------------
# srching lost and found item using item rcrd

def search_items(search_entry, item_type):
    global lost_records, found_records

    search_text = search_entry.get().strip().lower()
    if search_text == "search by item name, category or location...":
        search_text = ""
    search_words = search_text.split()


    all_items = loadItems()
    searchable_fields = [
        "item_ID",
        "item_name",
        "category",
        "color",
        "brand",
        "location",
        "date"
    ]

    matching_records = []
    for item in all_items:
        if str(item.get("item_type") or "").lower() != item_type:
            continue

        item_details = " ".join(
            str(item.get(field) or "").lower()
            for field in searchable_fields
        )
        if all(word in item_details for word in search_words):
            matching_records.append(item)

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
    
    # photo display area
    photo_area = tk.Frame(
        card,
        bg=lavender,
        height=105
    )
    photo_area.pack(fill="x", padx=12, pady=(12, 5))
    photo_area.pack_propagate(False)

    # getting the saved photo path
    photo_path = item.get("photo")

    # checking whether a photo exists
    if photo_path and os.path.isfile(photo_path):

        try:
            # opening and resizing the saved photo
            image = Image.open(photo_path)
            image.thumbnail((200, 95))

            # converting the image for Tkinter
            photo_image = ImageTk.PhotoImage(image)

            # displaying the photo
            photo_label = tk.Label(
                photo_area,
                image=photo_image,
                bg=lavender
            )
            photo_label.pack(expand=True)

            # keeping the image reference
            photo_label.image = photo_image

        except Exception:
            photo_path = None

    # displaying placeholder if no valid photo exists
    if not photo_path or not os.path.isfile(photo_path):

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

    # displaying item ID
    tk.Label(
        card,
        text=f"ITEM ID: {item.get('item_ID', 'N/A')}",
        font=("Segoe UI", 8, "bold"),
        bg=card_bg,
        fg=muted_text,
        anchor="w"
    ).pack(fill="x", padx=13, pady=(3, 5))

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
